# -*- coding: utf-8 -*-

"""Console script for release2cff."""
import sys
import re

import click
from nameparser import HumanName
import requests
import ruamel.yaml


@click.group()
@click.version_option()
def main():
    """Console script to generate/update CITATION.cff"""
    pass


@main.command()
@click.argument('doi')
@click.option('--cff_fn',
              type=click.File('x'),
              default='CITATION.cff',
              help='Name of citation formatted output file',
              show_default=True)
def init(doi, cff_fn):
    """Generate CITATION.cff file based on a Zenodo DOI of a Github release.

    * DOI, The Zenodo DOI url of a GitHub release
    """
    template = '''# YAML 1.2
# Metadata for citation of this software according to the CFF format (https://citation-file-format.github.io/)
cff-version: 1.0.3
message: If you use this software, please cite it as below.
# FIXME title as repository name might not be the best name, please make human readable
title: x
doi: 10.5281/zenodo.xxxxxx
# FIXME splitting of full names is error prone, please check if given/family name are correct
authors: []
version: x
date-released: yyyy-mm-dd
repository-code: x
license: x
    '''

    yaml = ruamel.yaml.YAML()
    data = yaml.load(template)

    zenodo_record = fetch_zenodo_by_doiurl(doi)

    data['title'] = clean_zenodo_title(zenodo_record['metadata']['title'])
    data['doi'] = zenodo_record['doi']
    tagurl = tagurl_of_zenodo(zenodo_record)
    if 'version' in zenodo_record['metadata']:
        data['version'] = re.sub('^(v)', '', zenodo_record['metadata']['version'])
    else:
        data['version'] = tagurl2version(tagurl)
    data['license'] = zenodo_record['metadata']['license']['id']
    data['date-released'] = zenodo_record['metadata']['publication_date']
    data['repository-code'] = tagurl2repo(tagurl)
    data['authors'] = authors_of_zenodo(zenodo_record)
    references = references_of_zenodo(zenodo_record)
    if references:
        data['references'] = yaml.seq(references)
        for idx, r in enumerate(references):
            if r['type'] == 'generic':
                data['references'].yaml_add_eol_comment('FIXME generic is too generic, see https://citation-file-format.github.io/1.0.3/specifications/#/reference-types for more specific types', idx)

    yaml.dump(data, cff_fn)

    click.echo('{0} file has been written'.format(cff_fn.name))


@main.command()
@click.argument('doi')
def update(doi):
    """Update CITATION.cff with doi of a new release

    * DOI, The Zenodo DOI url of a GitHub release
    """
    raise NotImplementedError('Update command has not been implemented')


def fetch_zenodo_by_doiurl(doiurl):
    zenodo_id = re.sub('https?://doi.org/', '', doiurl)
    return fetch_zenodo_by_doi(zenodo_id)


def fetch_zenodo_by_doi(doi):
    zenodo_id = doi.replace('10.5281/zenodo.', '')
    return fetch_zenodo_by_id(zenodo_id)


def fetch_zenodo_by_id(zenodo_id):
    zenodo_json_url = 'https://zenodo.org/api/records/' + zenodo_id

    response = requests.get(zenodo_json_url)

    response.raise_for_status()

    return response.json()


def tagurl_of_zenodo(record):
    for related_identifier in record['metadata']['related_identifiers']:
        if related_identifier['relation'] == 'isSupplementTo':

            return related_identifier['identifier']
    raise KeyError('Zenodo record does not contain a related identifier with isSupplementTo relation ')


def tagurl2repo(tagurl):
    return re.sub('(/tree/.*)$', '', tagurl)


def tagurl2version(tagurl):
    return re.sub('^.*(/tree/v?)', '', tagurl)


def clean_zenodo_title(title):
    title_without_version = re.sub(': .*$', '', title)
    title_without_organization = re.sub('^.*/', '', title_without_version)
    return title_without_organization


def authors_of_zenodo(zenodo_record):
    authors = []
    for a in zenodo_record['metadata']['creators']:
        name = HumanName(a['name'])
        author = {
            'given-names': name.first,
            'family-names': name.last,
        }
        if name.middle:
            author['name-particle'] = name.middle
        if name.suffix:
            author['name-suffix'] = name.suffix
        if 'affiliation' in a:
            author['affiliation'] = a['affiliation']
        if 'orcid' in a:
            author['orcid'] = 'https://orcid.org/' + a['orcid']
        authors.append(author)

    return authors


def references_of_zenodo(record):
    refs = []
    for related_identifier in record['metadata']['related_identifiers']:
        ref = reference_of_zenodo(related_identifier)
        if ref:
            refs.append(ref)
    return refs


def reference_of_zenodo(related_identifier):
    identifier = related_identifier['identifier']
    relation = related_identifier['relation']
    scheme = related_identifier['scheme']
    relation_blacklist = {'isSupplementTo', 'isPartOf', 'isReferencedBy'}
    if relation in relation_blacklist:
        return None
    if relation == 'compiles' and scheme == 'doi':
        zenodo_record = fetch_zenodo_by_doi(identifier)
        return {
            'type': 'software',
            'doi': identifier,
            'title': clean_zenodo_title(zenodo_record['metadata']['title']),
            'authors': authors_of_zenodo(zenodo_record),
            'notes': 'is compiled/created by this citation',
        }
    if relation in {'cites', 'references'} and scheme == 'doi':
        if dois_is_from_zenodo(identifier):
            zenodo_record = fetch_zenodo_by_doi(identifier)
            return {
                'type': 'generic',
                'doi': identifier,
                'title': clean_zenodo_title(zenodo_record['metadata']['title']),
                'authors': authors_of_zenodo(zenodo_record),
            }
        else:
            csl_record = fetch_csljson(identifier)
            return {
                'type': 'generic',
                'doi': identifier,
                'title': csl_record['title'],
                'authors': authors_of_csl(csl_record)
            }

    return None


def dois_is_from_zenodo(doi):
    return '10.5281/zenodo.' in doi


def fetch_csljson(doi):
    doiurl = 'https://doi.org/' + doi
    headers = {'Accept': 'application/vnd.citationstyles.csl+json'}
    response = requests.get(doiurl, headers=headers)
    response.raise_for_status()
    return response.json()


def authors_of_csl(record):
    authors = []
    for a in record['author']:
        author = {
            'given-names': a['given'],
            'family-names': a['family'],
        }
        authors.append(author)
    return authors


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
