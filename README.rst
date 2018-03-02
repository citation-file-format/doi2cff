=============
Release 2 cff
=============


.. image:: https://img.shields.io/travis/3D-e-Chem/release2cff.svg
        :target: https://travis-ci.org/3D-e-Chem/release2cff

.. image:: https://readthedocs.org/projects/release2cff/badge/?version=latest
        :target: https://release2cff.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Create citation file formatted file (https://citation-file-format.github.io/) from a Github/Zenodo release


* Free software: Apache Software License 2.0
* Documentation: https://release2cff.readthedocs.io.


Installation
------------

.. code-block:: bash

    pip install git+https://github.com/3D-e-Chem/release2cff

Usage
-----

To create a CITATION.cff file of a release, you must supply the doi that is associated with the release.

.. code-block:: bash

   release2cff init <doi>

   # For example for boatswain (https://github.com/NLeSC/boatswain)
   release2cff init https://doi.org/10.5281/zenodo.1149011

The generated file must be checked for correctness and you are encouraged to enrich it further.

Whenever a new release is made of the software the CITATION.cff must be updated with new doi/version/release date.
This process can be automated by running

.. code-block:: bash

    release2cff update <doi>

CITATION.cff file can be validated with

.. code-block:: bash

    release2cff validate

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
