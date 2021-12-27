=====
Usage
=====

To create a CITATION.cff file of a release, you must supply the doi that is associated with the release.

.. code-block:: bash

   doi2cff init <doi>

   # For example for boatswain (https://github.com/NLeSC/boatswain)
   doi2cff init https://doi.org/10.5281/zenodo.1149011

The generated file must be checked for correctness and you are encouraged to enrich it further.

The command above works well for Zenodo doi's, which contain especially rich metadata.
It is also possible to produce a CITATION.cff file from any available information. This feature is experimental:

.. code-block:: bash

   doi2cff init --experimental <doi>

   # For example
   doi2cff init 10.1051/0004-6361/202037850 --experimental


Whenever a new release is made of the software the CITATION.cff must be updated with new doi/version/release date.
This process can be automated by running (only for Zenodo dois)

.. code-block:: bash

    doi2cff update <doi>


