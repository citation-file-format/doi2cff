import pytest

# flake8: noqa: E501


@pytest.fixture
def zenodo_1200251():
    return {
        'conceptdoi': '10.5281/zenodo.597993',
        'conceptrecid': '597993',
        'created': '2018-03-16T11:33:28.867718+00:00',
        'doi': '10.5281/zenodo.1200251',
        'id': 1200251,
        'links': {
            'badge': 'https://zenodo.org/badge/doi/10.5281/zenodo.1200251.svg',
            'conceptbadge': 'https://zenodo.org/badge/doi/10.5281/zenodo.597993.svg',
            'conceptdoi': 'https://doi.org/10.5281/zenodo.597993',
            'doi': 'https://doi.org/10.5281/zenodo.1200251'
        },
        'metadata': {
            'access_right': 'open',
            'access_right_category': 'success',
            'creators': [
                {
                    'affiliation': 'Netherlands eScience Center',
                    'name': 'Maassen, Jason'
                },
                {
                    'affiliation': 'Netherlands eScience Center',
                    'name': 'Verhoeven, Stefan'
                },
                {
                    'affiliation': 'Netherlands eScience Center',
                    'name': 'Borgdorff, Joris'
                },
                {
                    'affiliation': 'Netherlands eScience Center',
                    'name': 'Spaaks, Jurriaan H.'
                },
                {
                    'affiliation': 'Netherlands eScience Center',
                    'name': 'Drost, Niels'
                },
                {
                    'affiliation': 'Netherlands eScience Center',
                    'name': 'Meijer, Christiaan'
                },
                {
                    'affiliation': 'Netherlands eScience Center',
                    'name': 'van der Ploeg, Atze'
                },
                {
                    'affiliation': 'Netherlands eScience Center',
                    'name': 'de Boer, Piter T.'
                },
                {
                    'affiliation': 'Netherlands eScience Center',
                    'name': 'van Nieuwpoort, Rob'
                },
                {
                    'affiliation': 'Netherlands eScience Center',
                    'name': 'van Werkhoven, Ben'
                },
                {
                    'affiliation': 'Netherlands eScience Center',
                    'name': 'Kuzniar, Arnold',
                    'orcid': '0000-0003-1711-7961'
                }
            ],
            'description': 'A middleware abstraction library that provides a simple programming interface to various compute and storage resources.',
            'doi': '10.5281/zenodo.1200251',
            'keywords': [
                'Java',
                'batch-job',
                'middleware',
                'library',
                'FTP',
                'S3',
                'SFTP',
                'WebDAV',
                'HDFS',
                'SGE',
                'SLURM',
                'SSH',
                'Torque',
                'distributed computing'
            ],
            'license': {
                'id': 'Apache-2.0'
            },
            'publication_date': '2018-03-16',
            'related_identifiers': [
                {
                    'identifier': 'https://github.com/NLeSC/Xenon/tree/2.6.1',
                    'relation': 'isSupplementTo',
                    'scheme': 'url'
                },
                {
                    'identifier': '10.5281/zenodo.597993',
                    'relation': 'isPartOf',
                    'scheme': 'doi'
                }
            ],
            'relations': {
                'version': [
                    {
                        'count': 18,
                        'index': 17,
                        'is_last': True,
                        'last_child': {
                            'pid_type': 'recid',
                            'pid_value': '1200251'
                        },
                        'parent': {
                            'pid_type': 'recid',
                            'pid_value': '597993'
                        }
                    }
                ]
            },
            'resource_type': {
                'title': 'Software',
                'type': 'software'
            },
            'title': 'Xenon',
            'version': '2.6.1'
        },
        'owners': [
            19643
        ],
        'revision': 4,
        'updated': '2018-03-16T11:41:53.616626+00:00'
    }


@pytest.fixture
def zenodo_1194353():
    return {
      'conceptdoi': '10.5281/zenodo.597993',
      'conceptrecid': '597993',
      'created': '2018-03-08T17:02:42.230256+00:00',
      'doi': '10.5281/zenodo.1194353',
      'id': 1194353,
      'links': {
        'badge': 'https://zenodo.org/badge/doi/10.5281/zenodo.1194353.svg',
        'conceptbadge': 'https://zenodo.org/badge/doi/10.5281/zenodo.597993.svg',
        'conceptdoi': 'https://doi.org/10.5281/zenodo.597993',
        'doi': 'https://doi.org/10.5281/zenodo.1194353'
      },
      'metadata': {
        'access_right': 'open',
        'access_right_category': 'success',
        'creators': [
          {
            'affiliation': 'Netherlands eScience Center',
            'name': 'Jason Maassen'
          },
          {
            'affiliation': 'Nederlands eScience Center',
            'name': 'Stefan Verhoeven'
          },
          {
            'affiliation': '@thehyve',
            'name': 'Joris Borgdorff'
          },
          {
            'affiliation': 'Netherlands eScience Center',
            'name': 'Niels Drost'
          },
          {
            'affiliation': 'Netherlands eScience Center',
            'name': 'Jurriaan H. Spaaks'
          },
          {
            'affiliation': 'Netherlands eScience Center',
            'name': 'Christiaan Meijer'
          },
          {
            'affiliation': 'Netherlands eScience Center',
            'name': 'Rob V. van Nieuwpoort'
          },
          {
            'affiliation': 'Netherlands eScience Center',
            'name': 'Atze van der Ploeg'
          },
          {
            'affiliation': 'Netherlands eScience Center',
            'name': 'Piter T. de Boer'
          },
          {
            'affiliation': 'Netherlands eScience Center',
            'name': 'Ben van Werkhoven'
          },
          {
            'affiliation': 'Netherlands eScience Center',
            'name': 'Arnold Kuzniar'
          }
        ],
        'description': '<p>What problem does Xenon solve?</p>\n\n<p>Many applications use remote storage and compute resources. To do so, they need to include code to interact with the scheduling systems and file transfer protocols used on those remote machines.</p>\n\n<p>Unfortunately, many different scheduler systems and file transfer protocols exist, often with completely different programming interfaces. This makes it hard for applications to switch to a different system or support multiple remote systems simultaneously.</p>\n\n<p>Xenon solves this problem by providing a single programming interface to many different types of remote resources, allowing applications to switch without changing a single line of code.</p>\n\n<p>Notable changes compared to v2.5.0:</p>\n\n<ul>\n\t<li>added support for scheduler specific arguments to JobDescription</li>\n\t<li>fixed specification of runtime limit in gridengine adaptor</li>\n</ul>',
        'doi': '10.5281/zenodo.1194353',
        'license': {
          'id': 'other-open'
        },
        'publication_date': '2018-03-08',
        'related_identifiers': [
          {
            'identifier': 'https://github.com/NLeSC/Xenon/tree/2.6.0',
            'relation': 'isSupplementTo',
            'scheme': 'url'
          },
          {
            'identifier': '10.5281/zenodo.597993',
            'relation': 'isPartOf',
            'scheme': 'doi'
          }
        ],
        'relations': {
          'version': [
            {
              'count': 18,
              'index': 16,
              'is_last': False,
              'last_child': {
                'pid_type': 'recid',
                'pid_value': '1200251'
              },
              'parent': {
                'pid_type': 'recid',
                'pid_value': '597993'
              }
            }
          ]
        },
        'resource_type': {
          'title': 'Software',
          'type': 'software'
        },
        'title': 'NLeSC/Xenon: This is release 2.6.0 of Xenon.',
        'version': '2.6.0'
      },
      'owners': [
        19643
      ],
      'revision': 6,
      'updated': '2018-03-16T11:34:21.807079+00:00'
    }


@pytest.fixture
def cff_1200251():
    return '''# YAML 1.2
# Metadata for citation of this software according to the CFF format (https://citation-file-format.github.io/)
cff-version: 1.2.0
message: If you use this software, please cite it using these metadata.
# FIXME title as repository name might not be the best name, please make human readable
title: Xenon
doi: 10.5281/zenodo.1200251
# FIXME splitting of full names is error prone, please check if given/family name are correct
authors:
- given-names: Jason
  family-names: Maassen
  affiliation: Netherlands eScience Center
- given-names: Stefan
  family-names: Verhoeven
  affiliation: Netherlands eScience Center
- given-names: Joris
  family-names: Borgdorff
  affiliation: Netherlands eScience Center
- given-names: Jurriaan
  family-names: Spaaks
  name-particle: H.
  affiliation: Netherlands eScience Center
- given-names: Niels
  family-names: Drost
  affiliation: Netherlands eScience Center
- given-names: Christiaan
  family-names: Meijer
  affiliation: Netherlands eScience Center
- given-names: Atze
  family-names: van der Ploeg
  affiliation: Netherlands eScience Center
- given-names: Piter
  family-names: de Boer
  name-particle: T.
  affiliation: Netherlands eScience Center
- given-names: Rob
  family-names: van Nieuwpoort
  affiliation: Netherlands eScience Center
- given-names: Ben
  family-names: van Werkhoven
  affiliation: Netherlands eScience Center
- given-names: Arnold
  family-names: Kuzniar
  affiliation: Netherlands eScience Center
  orcid: https://orcid.org/0000-0003-1711-7961
version: 2.6.1
date-released: 2018-03-16
repository-code: https://github.com/NLeSC/Xenon
license: Apache-2.0
'''


@pytest.fixture
def cff_1194353():
    return '''# YAML 1.2
# Metadata for citation of this software according to the CFF format (https://citation-file-format.github.io/)
cff-version: 1.2.0
message: If you use this software, please cite it using these metadata.
# FIXME title as repository name might not be the best name, please make human readable
title: 'NLeSC/Xenon: This is release 2.6.0 of Xenon.'
doi: 10.5281/zenodo.1194353
# FIXME splitting of full names is error prone, please check if given/family name are correct
authors:
- given-names: Jason
  family-names: Maassen
  affiliation: Netherlands eScience Center
- given-names: Stefan
  family-names: Verhoeven
  affiliation: Netherlands eScience Center
- given-names: Joris
  family-names: Borgdorff
  affiliation: '@thehyve'
- given-names: Jurriaan
  family-names: Spaaks
  name-particle: H.
  affiliation: Netherlands eScience Center
- given-names: Niels
  family-names: Drost
  affiliation: Netherlands eScience Center
- given-names: Christiaan
  family-names: Meijer
  affiliation: Netherlands eScience Center
- given-names: Atze
  family-names: van der Ploeg
  affiliation: Netherlands eScience Center
- given-names: Piter
  family-names: de Boer
  name-particle: T.
  affiliation: Netherlands eScience Center
- given-names: Rob
  family-names: van Nieuwpoort
  affiliation: Netherlands eScience Center
- given-names: Ben
  family-names: van Werkhoven
  affiliation: Netherlands eScience Center
- given-names: Arnold
  family-names: Kuzniar
  affiliation: Netherlands eScience Center
version: 2.6.0
date-released: 2018-03-08
repository-code: https://github.com/NLeSC/Xenon
license: Apache-2.0
'''


@pytest.fixture
def cff_1194353_updated_1200251():
    return '''# YAML 1.2
# Metadata for citation of this software according to the CFF format (https://citation-file-format.github.io/)
cff-version: 1.2.0
message: If you use this software, please cite it using these metadata.
# FIXME title as repository name might not be the best name, please make human readable
title: 'NLeSC/Xenon: This is release 2.6.0 of Xenon.'
doi: 10.5281/zenodo.1200251
# FIXME splitting of full names is error prone, please check if given/family name are correct
authors:
- given-names: Jason
  family-names: Maassen
  affiliation: Netherlands eScience Center
- given-names: Stefan
  family-names: Verhoeven
  affiliation: Netherlands eScience Center
- given-names: Joris
  family-names: Borgdorff
  affiliation: '@thehyve'
- given-names: Jurriaan
  family-names: Spaaks
  name-particle: H.
  affiliation: Netherlands eScience Center
- given-names: Niels
  family-names: Drost
  affiliation: Netherlands eScience Center
- given-names: Christiaan
  family-names: Meijer
  affiliation: Netherlands eScience Center
- given-names: Atze
  family-names: van der Ploeg
  affiliation: Netherlands eScience Center
- given-names: Piter
  family-names: de Boer
  name-particle: T.
  affiliation: Netherlands eScience Center
- given-names: Rob
  family-names: van Nieuwpoort
  affiliation: Netherlands eScience Center
- given-names: Ben
  family-names: van Werkhoven
  affiliation: Netherlands eScience Center
- given-names: Arnold
  family-names: Kuzniar
  affiliation: Netherlands eScience Center
version: 2.6.1
date-released: 2018-03-16
repository-code: https://github.com/NLeSC/Xenon
license: Apache-2.0
'''


@pytest.fixture
def zenodo_1197761():
    return {
      "conceptdoi": "10.5281/zenodo.1043481",
      "conceptrecid": "1043481",
      "created": "2018-03-14T11:20:14.518901+00:00",
      "doi": "10.5281/zenodo.1197761",
      "id": 1197761,
      "links": {
        "badge": "https://zenodo.org/badge/doi/10.5281/zenodo.1197761.svg",
        "conceptbadge": "https://zenodo.org/badge/doi/10.5281/zenodo.1043481.svg",
        "conceptdoi": "https://doi.org/10.5281/zenodo.1043481",
        "doi": "https://doi.org/10.5281/zenodo.1197761"
      },
      "metadata": {
        "access_right": "open",
        "access_right_category": "success",
        "creators": [
          {
            "affiliation": "Nederlands eScience Center",
            "name": "Stefan Verhoeven"
          },
          {
            "affiliation": "Netherlands eScience Center",
            "name": "Jason Maassen"
          },
          {
            "affiliation": "Netherlands eScience Center",
            "name": "Atze van der Ploeg"
          }
        ],
        "description": "<p>gRPC (<a href=\"http://www.grpc.io/\">http://www.grpc.io/</a>) server for Xenon (<a href=\"https://nlesc.github.io/Xenon/\">https://nlesc.github.io/Xenon/</a>).</p>\n\n<p>Can be used to use Xenon in a non-java based language. For example pyxenon (<a href=\"https://github.com/NLeSC/pyxenon\">https://github.com/NLeSC/pyxenon</a>) uses the Xenon gRPC server.</p>\n\n<p>The server tries to mimic the Xenon library API as much as possible, differences are described in the proto file (src/main/proto/xenon.proto).</p>\n\n<p>Added</p>\n\n<ul>\n\t<li>scheduler argument for job description (#38)</li>\n</ul>\n\n<p>Changed</p>\n\n<ul>\n\t<li>Depends on Xenon 2.6.0</li>\n</ul>",
        "doi": "10.5281/zenodo.1197761",
        "license": {
          "id": "Apache-2.0"
        },
        "publication_date": "2018-03-14",
        "related_identifiers": [
          {
            "identifier": "https://github.com/NLeSC/xenon-grpc/tree/v2.3.0",
            "relation": "isSupplementTo",
            "scheme": "url"
          },
          {
            "identifier": "10.5281/zenodo.597993",
            "relation": "references",
            "scheme": "doi"
          },
          {
            "identifier": "10.5281/zenodo.1043481",
            "relation": "isPartOf",
            "scheme": "doi"
          }
        ],
        "relations": {
          "version": [
            {
              "count": 6,
              "index": 5,
              "is_last": True,
              "last_child": {
                "pid_type": "recid",
                "pid_value": "1197761"
              },
              "parent": {
                "pid_type": "recid",
                "pid_value": "1043481"
              }
            }
          ]
        },
        "resource_type": {
          "title": "Software",
          "type": "software"
        },
        "title": "Xenon gRPC server",
        "version": "v2.3.0"
      },
      "owners": [
        19641
      ],
      "revision": 5,
      "updated": "2018-03-16T12:22:05.773487+00:00"
    }


@pytest.fixture
def cff_1197761():
    return '''# YAML 1.2
# Metadata for citation of this software according to the CFF format (https://citation-file-format.github.io/)
cff-version: 1.2.0
message: If you use this software, please cite it using these metadata.
# FIXME title as repository name might not be the best name, please make human readable
title: Xenon gRPC server
doi: 10.5281/zenodo.1197761
# FIXME splitting of full names is error prone, please check if given/family name are correct
authors:
- given-names: Stefan
  family-names: Verhoeven
  affiliation: Nederlands eScience Center
- given-names: Jason
  family-names: Maassen
  affiliation: Netherlands eScience Center
- given-names: Atze
  family-names: van der Ploeg
  affiliation: Netherlands eScience Center
version: 2.3.0
date-released: 2018-03-14
repository-code: https://github.com/NLeSC/xenon-grpc
license: Apache-2.0
references:
-  # FIXME generic is too generic, see https://citation-file-format.github.io/1.2.0/specifications/#/reference-types for more specific types
  type: generic
  doi: 10.5281/zenodo.597993
  title: Xenon
  authors:
  - given-names: Jason
    family-names: Maassen
    affiliation: Netherlands eScience Center
  - given-names: Stefan
    family-names: Verhoeven
    affiliation: Netherlands eScience Center
  - given-names: Joris
    family-names: Borgdorff
    affiliation: Netherlands eScience Center
  - given-names: Jurriaan
    family-names: Spaaks
    name-particle: H.
    affiliation: Netherlands eScience Center
  - given-names: Niels
    family-names: Drost
    affiliation: Netherlands eScience Center
  - given-names: Christiaan
    family-names: Meijer
    affiliation: Netherlands eScience Center
  - given-names: Atze
    family-names: van der Ploeg
    affiliation: Netherlands eScience Center
  - given-names: Piter
    family-names: de Boer
    name-particle: T.
    affiliation: Netherlands eScience Center
  - given-names: Rob
    family-names: van Nieuwpoort
    affiliation: Netherlands eScience Center
  - given-names: Ben
    family-names: van Werkhoven
    affiliation: Netherlands eScience Center
  - given-names: Arnold
    family-names: Kuzniar
    affiliation: Netherlands eScience Center
    orcid: https://orcid.org/0000-0003-1711-7961
'''


@pytest.fixture()
def zenodo_58369():
    return {
      "conceptdoi": "10.5281/zenodo.597241",
      "conceptrecid": "597241",
      "created": "2016-07-26T07:42:08+00:00",
      "doi": "10.5281/zenodo.58369",
      "id": 58369,
      "links": {
        "badge": "https://zenodo.org/badge/doi/10.5281/zenodo.58369.svg",
        "conceptbadge": "https://zenodo.org/badge/doi/10.5281/zenodo.597241.svg",
        "conceptdoi": "https://doi.org/10.5281/zenodo.597241",
        "doi": "https://doi.org/10.5281/zenodo.58369"
      },
      "metadata": {
        "access_right": "open",
        "access_right_category": "success",
        "creators": [
          {
            "affiliation": "Nederlands eScience Center",
            "name": "Stefan Verhoeven",
            "orcid": "0000-0002-5821-2060"
          }
        ],
        "description": "<p>Knime node to calculate subfamily specific two entropy analysis (ss-TEA) score.</p>\n\n<p>The ss-TEA can identify specific ligand binding residue positions for any receptor, predicated on high quality sequence information.</p>\n\n<p>The Knime node can be installed from <a href=\"https://3d-e-chem.github.io/updates\">https://3d-e-chem.github.io/updates</a> update site.</p>\n\n<p>Added</p>\n\n<ul>\n\t<li>Integration tests, by running workflows</li>\n</ul>\n\n<p>Changed</p>\n\n<ul>\n\t<li>Nested Sygma node under 3D-e-chem category (#10)</li>\n</ul>\n\n<p>Removed</p>\n\n<ul>\n\t<li>Node views</li>\n</ul>",
        "doi": "10.5281/zenodo.58369",
        "license": {
          "id": "Apache-2.0"
        },
        "publication_date": "2016-07-21",
        "related_identifiers": [
          {
            "identifier": "https://github.com/3D-e-Chem/knime-sstea/tree/v1.0.5",
            "relation": "isSupplementTo",
            "scheme": "url"
          },
          {
            "identifier": "10.1186/1471-2105-12-332",
            "relation": "references",
            "scheme": "doi"
          },
          {
            "identifier": "10.5281/zenodo.597241",
            "relation": "isPartOf",
            "scheme": "doi"
          }
        ],
        "relations": {
          "version": [
            {
              "count": 4,
              "index": 3,
              "is_last": True,
              "last_child": {
                "pid_type": "recid",
                "pid_value": "58369"
              },
              "parent": {
                "pid_type": "recid",
                "pid_value": "597241"
              }
            }
          ]
        },
        "resource_type": {
          "title": "Software",
          "type": "software"
        },
        "title": "knime-sstea: v1.0.5",
        "version": "v1.0.5"
      },
      "owners": [
        19641
      ],
      "revision": 9,
      "updated": "2018-03-05T11:00:00.709228+00:00"
    }


@pytest.fixture
def cslfor_58369():
    """Content was generated with:

    curl -L -H 'Accept: application/vnd.citationstyles.csl+json' \
    https://doi.org/10.1186/1471-2105-12-332
    """
    return {
      "indexed": {
        "date-parts": [
          [
            2017,
            11,
            29
          ]
        ],
        "date-time": "2017-11-29T11:42:12Z",
        "timestamp": 1511955732839
      },
      "reference-count": 42,
      "publisher": "Springer Nature",
      "issue": "1",
      "content-domain": {
        "domain": [],
        "crossmark-restriction": False
      },
      "published-print": {
        "date-parts": [
          [
            2011
          ]
        ]
      },
      "DOI": "10.1186/1471-2105-12-332",
      "type": "article-journal",
      "created": {
        "date-parts": [
          [
            2011,
            8,
            10
          ]
        ],
        "date-time": "2011-08-10T18:16:00Z",
        "timestamp": 1313000160000
      },
      "page": "332",
      "source": "Crossref",
      "is-referenced-by-count": 12,
      "title": "ss-TEA: Entropy based identification of receptor specific ligand binding residues from a multiple sequence alignment of class A GPCRs",
      "prefix": "10.1186",
      "volume": "12",
      "author": [
        {
          "given": "Marijn PA",
          "family": "Sanders",
          "affiliation": []
        },
        {
          "given": "Wilco WM",
          "family": "Fleuren",
          "affiliation": []
        },
        {
          "given": "Stefan",
          "family": "Verhoeven",
          "affiliation": []
        },
        {
          "given": "Sven",
          "family": "van den Beld",
          "affiliation": []
        },
        {
          "given": "Wynand",
          "family": "Alkema",
          "affiliation": []
        },
        {
          "given": "Jacob",
          "family": "de Vlieg",
          "affiliation": []
        },
        {
          "given": "Jan PG",
          "family": "Klomp",
          "affiliation": []
        }
      ],
      "member": "297",
      "reference": [
        {
          "key": "10.1186/1471-2105-12-332-B1",
          "DOI": "10.1002/1439-7633(20021004)3:10<928::AID-CBIC928>3.0.CO;2-5",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B2",
          "DOI": "10.1038/nrd892",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B3",
          "DOI": "10.1093/protein/7.2.195",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B5",
          "DOI": "10.1093/nar/gkg103",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B7",
          "DOI": "10.1124/pr.57.2.5",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B8",
          "DOI": "10.1038/nrd722",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B9",
          "DOI": "10.1038/nrd746",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B10",
          "DOI": "10.1124/pr.57.2.2",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B11",
          "DOI": "10.1124/jpet.105.083121",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B13",
          "DOI": "10.1016/S0968-0004(01)01799-6",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B14",
          "DOI": "10.1016/S0165-6147(00)89078-1",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B17",
          "DOI": "10.1016/S1359-6101(01)00014-4",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B18",
          "DOI": "10.1089/dna.2005.24.54",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B19",
          "DOI": "10.1124/pr.54.2.265",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B20",
          "DOI": "10.1124/pr.56.1.4",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B21",
          "DOI": "10.1016/j.pharmthera.2004.04.005",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B22",
          "DOI": "10.1038/sj.bjp.0707308",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B23",
          "DOI": "10.1007/s00210-008-0318-3",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B24",
          "DOI": "10.1074/jbc.270.43.25771",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B25",
          "DOI": "10.1126/science.289.5480.739",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B26",
          "DOI": "10.1038/nature06925",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B27",
          "DOI": "10.1126/science.1150577",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B28",
          "DOI": "10.1038/nature07101",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B29",
          "DOI": "10.1126/science.1164772",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B33",
          "DOI": "10.1002/prot.10489",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B34",
          "DOI": "10.1002/prot.20899",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B35",
          "DOI": "10.1016/j.ygeno.2006.04.001",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B37",
          "DOI": "10.1093/bioinformatics/btm537",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B38",
          "DOI": "10.1021/jm0300431",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B42",
          "DOI": "10.1186/1471-2105-10-136",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B45",
          "DOI": "10.1093/bioinformatics/btm404",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B46",
          "DOI": "10.1126/science.1150609",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B47",
          "DOI": "10.1074/jbc.M207420200",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B48",
          "DOI": "10.1074/jbc.M007748200",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B49",
          "DOI": "10.1038/sj.bjp.0707567",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B50",
          "DOI": "10.2174/0929867053764617",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B51",
          "DOI": "10.1210/er.2003-0002",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B52",
          "DOI": "10.1074/jbc.M705077200",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B53",
          "DOI": "10.1016/S0006-3495(02)75307-1",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B54",
          "DOI": "10.1021/jm049914c",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B56",
          "DOI": "10.1021/jm900319e",
          "doi-asserted-by": "publisher"
        },
        {
          "key": "10.1186/1471-2105-12-332-B57",
          "DOI": "10.1007/s10822-008-9181-z",
          "doi-asserted-by": "publisher"
        }
      ],
      "container-title": "BMC Bioinformatics",
      "original-title": [],
      "deposited": {
        "date-parts": [
          [
            2016,
            5,
            16
          ]
        ],
        "date-time": "2016-05-16T12:52:37Z",
        "timestamp": 1463403157000
      },
      "score": 1,
      "subtitle": [],
      "short-title": [],
      "issued": {
        "date-parts": [
          [
            2011
          ]
        ]
      },
      "references-count": 42,
      "alternative-id": [
        "1471-2105-12-332"
      ],
      "URL": "http://dx.doi.org/10.1186/1471-2105-12-332",
      "relation": {
        "cites": []
      },
      "ISSN": [
        "1471-2105"
      ],
      "subject": [
        "Biochemistry",
        "Applied Mathematics",
        "Molecular Biology",
        "Structural Biology",
        "Computer Science Applications"
      ],
      "container-title-short": "BMC Bioinformatics"
    }


@pytest.fixture
def cff_58369():
    return '''# YAML 1.2
# Metadata for citation of this software according to the CFF format (https://citation-file-format.github.io/)
cff-version: 1.2.0
message: If you use this software, please cite it using these metadata.
# FIXME title as repository name might not be the best name, please make human readable
title: 'knime-sstea: v1.0.5'
doi: 10.5281/zenodo.58369
# FIXME splitting of full names is error prone, please check if given/family name are correct
authors:
- given-names: Stefan
  family-names: Verhoeven
  affiliation: Nederlands eScience Center
  orcid: https://orcid.org/0000-0002-5821-2060
version: 1.0.5
date-released: 2016-07-21
repository-code: https://github.com/3D-e-Chem/knime-sstea
license: Apache-2.0
references:
-  # FIXME generic is too generic, see https://citation-file-format.github.io/1.2.0/specifications/#/reference-types for more specific types
  type: generic
  doi: 10.1186/1471-2105-12-332
  title: 'ss-TEA: Entropy based identification of receptor specific ligand binding
    residues from a multiple sequence alignment of class A GPCRs'
  authors:
  - given-names: Marijn PA
    family-names: Sanders
  - given-names: Wilco WM
    family-names: Fleuren
  - given-names: Stefan
    family-names: Verhoeven
  - given-names: Sven
    family-names: van den Beld
  - given-names: Wynand
    family-names: Alkema
  - given-names: Jacob
    family-names: de Vlieg
  - given-names: Jan PG
    family-names: Klomp
'''


@pytest.fixture
def cff_202037850():
  return '''# YAML 1.2
# Metadata for citation of this software according to the CFF format (https://citation-file-format.github.io/)
cff-version: 1.2.0
message: If you use this software, please cite it using these metadata.
# FIXME title as repository name might not be the best name, please make human readable
title: Online data analysis system of the INTEGRAL telescope
doi: 10.1051/0004-6361/202037850
# FIXME splitting of full names is error prone, please check if given/family name are correct
authors:
- given-names: A.
  family-names: Neronov
- given-names: V.
  family-names: Savchenko
- given-names: A.
  family-names: Tramacere
- given-names: M.
  family-names: Meharga
- given-names: C.
  family-names: Ferrigno
- given-names: S.
  family-names: Paltani
date-released: 2021-04-27
license:
- start:
    date-parts:
    - - 2021
      - 4
      - 27
    date-time: '2021-04-27T00:00:00Z'
    timestamp: 1619481600000
  content-version: vor
  delay-in-days: 0
  URL: https://www.edpsciences.org/en/authors/copyright-and-licensing
'''


@pytest.fixture
def cslfor_202037850():
    """Content was generated with:

    curl -L -H 'Accept: application/vnd.citationstyles.csl+json'  \
      https://doi.org/10.1051/0004-6361/202037850
    """
    return {
  "indexed": {
    "date-parts": [
      [
        2021,
        12,
        9
      ]
    ],
    "date-time": "2021-12-09T19:25:39Z",
    "timestamp": 1639077939575
  },
  "reference-count": 0,
  "publisher": "EDP Sciences",
  "license": [
    {
      "start": {
        "date-parts": [
          [
            2021,
            4,
            27
          ]
        ],
        "date-time": "2021-04-27T00:00:00Z",
        "timestamp": 1619481600000
      },
      "content-version": "vor",
      "delay-in-days": 0,
      "URL": "https://www.edpsciences.org/en/authors/copyright-and-licensing"
    }
  ],
  "content-domain": {
    "domain": [],
    "crossmark-restriction": False
  },
  "accepted": {
    "date-parts": [
      [
        2021,
        3,
        8
      ]
    ]
  },
  "DOI": "10.1051/0004-6361/202037850",
  "type": "journal-article",
  "created": {
    "date-parts": [
      [
        2021,
        4,
        27
      ]
    ],
    "date-time": "2021-04-27T08:30:49Z",
    "timestamp": 1619512249000
  },
  "source": "Crossref",
  "is-referenced-by-count": 0,
  "title": "Online data analysis system of the INTEGRAL telescope",
  "prefix": "10.1051",
  "author": [
    {
      "given": "A.",
      "family": "Neronov",
      "sequence": "first",
      "affiliation": []
    },
    {
      "given": "V.",
      "family": "Savchenko",
      "sequence": "additional",
      "affiliation": []
    },
    {
      "given": "A.",
      "family": "Tramacere",
      "sequence": "additional",
      "affiliation": []
    },
    {
      "given": "M.",
      "family": "Meharga",
      "sequence": "additional",
      "affiliation": []
    },
    {
      "given": "C.",
      "family": "Ferrigno",
      "sequence": "additional",
      "affiliation": []
    },
    {
      "given": "S.",
      "family": "Paltani",
      "sequence": "additional",
      "affiliation": []
    }
  ],
  "member": "250",
  "published-online": {
    "date-parts": [
      [
        2021,
        4,
        27
      ]
    ]
  },
  "container-title": "Astronomy & Astrophysics",
  "original-title": [],
  "link": [
    {
      "URL": "https://www.aanda.org/10.1051/0004-6361/202037850/pdf",
      "content-type": "unspecified",
      "content-version": "vor",
      "intended-application": "similarity-checking"
    }
  ],
  "deposited": {
    "date-parts": [
      [
        2021,
        6,
        1
      ]
    ],
    "date-time": "2021-06-01T18:58:58Z",
    "timestamp": 1622573938000
  },
  "score": 1,
  "subtitle": [],
  "short-title": [],
  "issued": {
    "date-parts": [
      [
        2021,
        4,
        27
      ]
    ]
  },
  "references-count": 0,
  "alternative-id": [
    "aa37850-20"
  ],
  "URL": "http://dx.doi.org/10.1051/0004-6361/202037850",
  "relation": {},
  "ISSN": [
    "0004-6361",
    "1432-0746"
  ],
  "subject": [
    "Space and Planetary Science",
    "Astronomy and Astrophysics"
  ],
  "container-title-short": "A&A",
  "published": {
    "date-parts": [
      [
        2021,
        4,
        27
      ]
    ]
  }
}



@pytest.fixture
def cff_1995729():
  return '''# YAML 1.2
# Metadata for citation of this software according to the CFF format (https://citation-file-format.github.io/)
cff-version: 1.2.0
message: If you use this software, please cite it using these metadata.
# FIXME title as repository name might not be the best name, please make human readable
title: Albert Einstein to Max Born                   1
doi: 10.1063/1.1995729
# FIXME splitting of full names is error prone, please check if given/family name are correct
authors:
- given-names: Albert
  family-names: Einstein
date-released: 2005-05-01
license: x
references:
-  # FIXME generic is too generic, see https://citation-file-format.github.io/1.2.0/specifications/#/reference-types for more specific types
  key: c1
  unstructured: 'M. Born , The Born–Einstein Letters 1916–1955: Freindship, Politics
    and Physics in Uncertain Times, Macmillan, New York (2005), p. 88. Original letter
    © The Hebrew University of Jerusalem, Israel.'
- # FIXME generic is too generic, see https://citation-file-format.github.io/1.2.0/specifications/#/reference-types for more specific types
  key: c2
  volume-title: 'The End of the Uncertain World: The Life and Science of Max Born'
  author: Greenspan N. T.
  year: '2005'
'''


@pytest.fixture
def cslfor_1995729():
    """Content was generated with:

    curl -L -H 'Accept: application/vnd.citationstyles.csl+json'  \
      https://doi.org/10.1063/1.1995729
    """
    return {
  "indexed": {
    "date-parts": [
      [
        2021,
        12,
        16
      ]
    ],
    "date-time": "2021-12-16T18:54:42Z",
    "timestamp": 1639680882985
  },
  "reference-count": 2,
  "publisher": "AIP Publishing",
  "issue": "5",
  "content-domain": {
    "domain": [],
    "crossmark-restriction": True
  },
  "published-print": {
    "date-parts": [
      [
        2005,
        5
      ]
    ]
  },
  "DOI": "10.1063/1.1995729",
  "type": "journal-article",
  "created": {
    "date-parts": [
      [
        2007,
        3,
        13
      ]
    ],
    "date-time": "2007-03-13T19:20:15Z",
    "timestamp": 1173813615000
  },
  "page": "16-16",
  "source": "Crossref",
  "is-referenced-by-count": 0,
  "title": "Albert Einstein to Max Born                   1",
  "prefix": "10.1063",
  "volume": "58",
  "author": [
    {
      "given": "Albert",
      "family": "Einstein",
      "sequence": "first",
      "affiliation": []
    }
  ],
  "member": "317",
  "reference": [
    {
      "key": "c1",
      "unstructured": "M. Born , The Born–Einstein Letters 1916–1955: Freindship, Politics and Physics in Uncertain Times, Macmillan, New York (2005), p. 88. Original letter © The Hebrew University of Jerusalem, Israel."
    },
    {
      "key": "c2",
      "volume-title": "The End of the Uncertain World: The Life and Science of Max Born",
      "author": "Greenspan N. T.",
      "year": "2005"
    }
  ],
  "container-title": "Physics Today",
  "original-title": [],
  "language": "en",
  "link": [
    {
      "URL": "http://physicstoday.scitation.org/doi/pdf/10.1063/1.1995729",
      "content-type": "unspecified",
      "content-version": "vor",
      "intended-application": "similarity-checking"
    }
  ],
  "deposited": {
    "date-parts": [
      [
        2016,
        12,
        28
      ]
    ],
    "date-time": "2016-12-28T18:02:11Z",
    "timestamp": 1482948131000
  },
  "score": 1,
  "subtitle": [],
  "short-title": [],
  "issued": {
    "date-parts": [
      [
        2005,
        5
      ]
    ]
  },
  "references-count": 2,
  "journal-issue": {
    "issue": "5",
    "published-print": {
      "date-parts": [
        [
          2005,
          5
        ]
      ]
    }
  },
  "alternative-id": [
    "10.1063/1.1995729"
  ],
  "URL": "http://dx.doi.org/10.1063/1.1995729",
  "relation": {},
  "ISSN": [
    "0031-9228",
    "1945-0699"
  ],
  "subject": [
    "General Physics and Astronomy"
  ],
  "container-title-short": "Physics Today",
  "published": {
    "date-parts": [
      [
        2005,
        5
      ]
    ]
  }
}
