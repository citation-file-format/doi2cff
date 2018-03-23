=====
Usage
=====

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
