=========
DOI 2 cff
=========


.. image:: https://travis-ci.org/citation-file-format/doi2cff.svg?branch=master
    :target: https://travis-ci.org/citation-file-format/doi2cff
    
.. image:: https://readthedocs.org/projects/doi2cff/badge/?version=latest
        :target: https://doi2cff.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://sonarcloud.io/api/project_badges/measure?project=doi2cff&metric=alert_status
       :target: https://sonarcloud.io/dashboard?id=doi2cff
       :alt: SonarCloud quality gate

.. image:: https://sonarcloud.io/api/project_badges/measure?project=doi2cff&metric=coverage
       :target: https://sonarcloud.io/api/project_badges/measure?project=doi2cff&metric=coverage
       :alt: SonarCloud coverage

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.1206048.svg
   :target: https://doi.org/10.5281/zenodo.1206048

Script to create citation file formatted file (https://citation-file-format.github.io/) from a DOI.

Current supported DOI types:

* Zenodo software from a GitHub release

Free software: Apache Software License 2.0

Documentation: https://doi2cff.readthedocs.io.

Installation
------------

Requires Python 3.5 or higher.

.. code-block:: bash

    pip install git+https://github.com/citation-file-format/doi2cff

Usage
-----

To create a CITATION.cff file of a release, you must supply the doi that is associated with the release.

.. code-block:: bash

   doi2cff init <doi>

   # For example for boatswain (https://github.com/NLeSC/boatswain)
   doi2cff init https://doi.org/10.5281/zenodo.1149011

The generated file must be checked for correctness and you are encouraged to enrich it further.

Whenever a new release is made of the software the CITATION.cff must be updated with new doi/version/release date.
This process can be automated by running

.. code-block:: bash

    doi2cff update <doi>

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
