# -*- coding: utf-8 -*-

"""Console script for doi2cff."""
import sys
import re
from datetime import datetime
from typing import Any, Tuple

import click
from nameparser import HumanName
import ruamel.yaml

from doi2cff.fetchers import fetch_zenodo_by_doiurl, fetch_zenodo_by_doi, fetch_csljson


@click.group()
@click.version_option()
def main():
    """Console script to generate/update CITATION.cff

    Current supported DOI types:

        * Zenodo upload of a GitHub release (https://guides.github.com/activities/citable-code/)
        * Any DOIs with suitable metadata (experimental).

    """
    pass


def is_software_zenodo(zenodo_record):
    return zenodo_record['metadata']['resource_type']['type'] == 'software'


def zenodo_record_to_cff_yaml(zenodo_record: dict, template) -> Tuple[ruamel.yaml.YAML, Any]:
    yaml = ruamel.yaml.YAML()
    data = yaml.load(template)
    data['title'] = zenodo_record['metadata']['title']
    data['doi'] = zenodo_record['doi']
    tagurl = tagurl_of_zenodo(zenodo_record)
    if 'version' in zenodo_record['metadata']:
        data['version'] = re.sub('^(v)', '', zenodo_record['metadata']['version'])
    else:
        data['version'] = tagurl2version(tagurl)
    data['license'] = zenodo_record['metadata']['license']['id']
    data['date-released'] = datetime.strptime(zenodo_record['metadata']['publication_date'], "%Y-%m-%d").date()
    data['repository-code'] = tagurl2repo(tagurl)
    data['authors'] = authors_of_zenodo(zenodo_record)
    references = references_of_zenodo(zenodo_record)
    fixme = 'FIXME generic is too generic, ' \
            'see https://citation-file-format.github.io/1.2.0/specifications/#/reference-types for more specific types'
    if references:
        data['references'] = yaml.seq(references)
        for idx, r in enumerate(references):
            if r['type'] == 'generic':
                data['references'].yaml_add_eol_comment(fixme, idx)

    return yaml, data


def csljson_to_cff_yaml(cffjson: dict, template) -> Tuple[ruamel.yaml.YAML, Any]:
    yaml = ruamel.yaml.YAML()
    data = yaml.load(template)

    data['title'] = cffjson['title']
    if '\n' in data['title']:
        data.yaml_add_eol_comment("FIXME: title contains new line: this is strange", "title")

    data['doi'] = cffjson['DOI']
    data['license'] = cffjson['license']
    data['date-released'] = datetime(*cffjson['published']['date-parts'][0], 1).date()
    data['authors'] = authors_of_csl(cffjson)

    references = cffjson.get('reference', None)
    fixme = 'FIXME generic is too generic, ' \
            'see https://citation-file-format.github.io/1.2.0/specifications/#/reference-types for more specific types'
    if references:
        data['references'] = yaml.seq(references)
        for idx, r in enumerate(references):
            if r.get('type', 'generic') == 'generic':
                data['references'].yaml_add_eol_comment(fixme, idx)

    # In CFF 1.2.0 these fields are optional
    # https://github.com/citation-file-format/citation-file-format/releases/tag/1.2.0
    del data['version']
    del data['repository-code']    

    return yaml, data


@main.command()
@click.argument('doi')
@click.option('--cff_fn',
              type=click.File('x'),
              default='CITATION.cff',
              help='Name of citation formatted output file',
              show_default=True)
@click.option('--experimental/--no-experimental',
              is_flag=True,
              default=False,
              help='experimental parsing of non-zenodo links',
              show_default=True)
def init(doi, cff_fn, experimental):
    """Generate CITATION.cff file based on a Zenodo DOI of a Github release.

    * DOI, The Digital Object Identifier (DOI) name of a Zenodo upload of a GitHub release
    """
    template = '''# YAML 1.2
# Metadata for citation of this software according to the CFF format (https://citation-file-format.github.io/)
cff-version: 1.2.0
message: If you use this software, please cite it using these metadata.
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

    if doi_is_from_zenodo(doi):
        zenodo_record = fetch_zenodo_by_doiurl(doi)

        if not is_software_zenodo(zenodo_record):
            raise click.UsageError('Unable to process DOI name, only accept DOI name '
                                   'which is a Zenodo upload of type software')

        yaml, data = zenodo_record_to_cff_yaml(zenodo_record, template)
    else:
        if experimental:
            click.echo("Trying experimental parsing of arbitrary DOI")
            csljson = fetch_csljson(doi)
            yaml, data = csljson_to_cff_yaml(csljson, template)
        else:
            raise click.UsageError('Unable to process DOI name, normally we only accept DOI name '
                                   'which is a Zenodo upload'
                                   'You can try experimental parsing of other DOIs '
                                   '(see --experimental option).')

    yaml.dump(data, cff_fn)

    click.echo('{0} file has been written'.format(cff_fn.name))


@main.command()
@click.argument('doi')
@click.option('--cff_fn',
              type=click.File('r+'),
              default='CITATION.cff',
              help='Name of citation formatted output file',
              show_default=True)
def update(doi, cff_fn):
    """Update CITATION.cff with doi, version and release date of a new release

    * DOI, The Digital Object Identifier (DOI) name of a Zenodo upload of a GitHub release
    """

    if not doi_is_from_zenodo(doi):
        raise click.UsageError('CITATION.cff update is only possible with Zenodo DOI. '
                               'For non-Zenodo DOIs, please consider recreating the citation, enabling experimental features: '
                               '`doi2cff init <doi> --experimental`')

    update_version(doi, cff_fn)


def update_version(doi, cff_file_handle):
    yaml = ruamel.yaml.YAML()
    data = yaml.load(cff_file_handle)

    zenodo_record = fetch_zenodo_by_doiurl(doi)
    data['doi'] = zenodo_record['doi']
    tagurl = tagurl_of_zenodo(zenodo_record)
    if 'version' in zenodo_record['metadata']:
        data['version'] = re.sub('^(v)', '', zenodo_record['metadata']['version'])
    else:
        data['version'] = tagurl2version(tagurl)
    data['date-released'] = datetime.strptime(zenodo_record['metadata']['publication_date'], "%Y-%m-%d").date()

    cff_file_handle.seek(0)
    yaml.dump(data, cff_file_handle)
    cff_file_handle.flush()


def tagurl_of_zenodo(record):
    for related_identifier in record['metadata']['related_identifiers']:
        if related_identifier['relation'] == 'isSupplementTo':

            return related_identifier['identifier']
    msg = 'Unable to process DOI name, Zenodo upload does not contain a related identifier ' \
          'with isSupplementTo relation, which is expected for DOI generated by GitHub'
    raise click.UsageError(msg)


def tagurl2repo(tagurl):
    return re.sub('(/tree/.*)$', '', tagurl)


def tagurl2version(tagurl):
    return re.sub('^.*(/tree/v?)', '', tagurl)


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
            'title': zenodo_record['metadata']['title'],
            'authors': authors_of_zenodo(zenodo_record),
            'notes': 'is compiled/created by this citation',
        }
    if relation in {'cites', 'references'} and scheme == 'doi':
        if doi_is_from_zenodo(identifier):
            zenodo_record = fetch_zenodo_by_doi(identifier)
            return {
                'type': 'generic',
                'doi': identifier,
                'title': zenodo_record['metadata']['title'],
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


def doi_is_from_zenodo(doi):
    return '10.5281/zenodo.' in doi


def authors_of_csl(record):
    authors = []
    for a in record['author']:
        if 'given' in a and 'family' in a:
            author = {
                'given-names': a['given'],
                'family-names': a['family'],
            }
        elif 'literal' in a:
            name = HumanName(a['literal'])
            author = {
                'given-names': name.first,
                'family-names': name.last,
            }
        else:
            raise click.UsageError('Unable to process DOI name, do not understand author field: {}'.format(a))
        authors.append(author)
    return authors


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
