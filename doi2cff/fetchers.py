import re

import requests


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


def fetch_csljson(doi):
    doiurl = 'https://doi.org/' + doi
    headers = {'Accept': 'application/vnd.citationstyles.csl+json'}
    response = requests.get(doiurl, headers=headers)
    response.raise_for_status()
    return response.json()
