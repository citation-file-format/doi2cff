#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `doi2cff` package."""
from io import StringIO

import pytest
import ruamel.yaml

from click.testing import CliRunner
import requests_mock

from doi2cff import cli
from doi2cff.cli import init, update_version

yaml = ruamel.yaml.YAML(typ='safe', pure=True)

@pytest.fixture
def runner():
    return CliRunner()


def test_command_line_interface(runner):
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'Console script to generate/update CITATION.cff' in result.output


def test_command_line_interface_help(runner):
    result = runner.invoke(cli.main, ['--help'])
    assert result.exit_code == 0
    assert 'Console script to generate/update CITATION.cff' in result.output


def test_init(runner, zenodo_1200251, cff_1200251):
    doi = 'https://doi.org/10.5281/zenodo.597993'
    zenodo_json = zenodo_1200251

    with runner.isolated_filesystem(), requests_mock.mock() as m:
        m.get('https://zenodo.org/api/records/597993', json=zenodo_json)

        runner.invoke(init, [doi])

        with open('CITATION.cff', 'r') as f:
            result = f.read()

    expected = cff_1200251
    assert yaml.load(result) == yaml.load(expected)


def test_update_version(cff_1194353, zenodo_1200251, cff_1194353_updated_1200251):
    doi = 'https://doi.org/10.5281/zenodo.1200251'
    cff_v1 = cff_1194353
    zenodo_json = zenodo_1200251

    with requests_mock.mock() as m:
        m.get('https://zenodo.org/api/records/1200251', json=zenodo_json)
        f = StringIO(cff_v1)

        update_version(doi, f)

        result = f.getvalue()

    expected = cff_1194353_updated_1200251
    assert yaml.load(result) == yaml.load(expected)


def test_init_withzenodoref(runner, zenodo_1197761, zenodo_1200251, cff_1197761):
    doi = 'https://doi.org/10.5281/zenodo.1197761'

    with runner.isolated_filesystem(), requests_mock.mock() as m:
        m.get('https://zenodo.org/api/records/1197761', json=zenodo_1197761)
        m.get('https://zenodo.org/api/records/597993', json=zenodo_1200251)

        runner.invoke(init, [doi])

        with open('CITATION.cff', 'r') as f:
            result = f.read()

    expected = cff_1197761
    assert yaml.load(result) == yaml.load(expected)


def test_init_withnonzenodoref(runner, zenodo_58369, cslfor_58369, cff_58369):
    doi = 'https://doi.org/10.5281/zenodo.58369'

    with runner.isolated_filesystem(), requests_mock.mock() as m:
        m.get('https://zenodo.org/api/records/58369', json=zenodo_58369)
        m.get('https://doi.org/10.1186/1471-2105-12-332', json=cslfor_58369)

        runner_result = runner.invoke(init, [doi])
        assert 'Trying experimental parsing of arbitrary DOI' not in runner_result.output

        with open('CITATION.cff', 'r') as f:
            result = f.read()

    expected = cff_58369
    assert yaml.load(result) == yaml.load(expected)



def test_init_csl_noref(runner, cff_202037850, cslfor_202037850):
    doi = '10.1051/0004-6361/202037850'

    with runner.isolated_filesystem(), requests_mock.mock() as m:    
        m.get('https://doi.org/10.1051/0004-6361/202037850', json=cslfor_202037850)

        runner_result = runner.invoke(init, [doi, '--experimental', '--cff_fn', 'CITATION.cff'], catch_exceptions=False)
        assert 'Trying experimental parsing of arbitrary DOI' in runner_result.output

        with open('CITATION.cff', 'r') as f:
            result = f.read()

    assert yaml.load(result) == yaml.load(cff_202037850)


def test_init_csl_nolicense(runner, cff_1995729, cslfor_1995729):
    # TODO: complete!    
    doi = '10.1063/1.1995729'

    with runner.isolated_filesystem(), requests_mock.mock() as m:    
        m.get('https://doi.org/10.1063/1.1995729', json=cslfor_1995729)
        runner.invoke(init, [doi, '--experimental', '--cff_fn', 'CITATION.cff'], catch_exceptions=False)

        with open('CITATION.cff', 'r') as f:
            result = f.read()

    assert yaml.load(result) == yaml.load(cff_1995729)

