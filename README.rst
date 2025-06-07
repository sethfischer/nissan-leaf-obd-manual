===========================
*Nissan Leaf* OBD-II manual
===========================

|docs-status| |test-status| |linkcheck-status|


Getting started
---------------

.. code:: console

    $ make install-ide-config
    $ make install-git-hooks

.. code-block:: console

    $ virtualenv .venv
    $ . .venv/bin/activate
    $ pip install -U pip
    $ pip install -r requirements.txt
    $ pip install -r requirements-dev.txt
    $ make html


License
-------

|license-cc-by-4.0| |license-mit|

Prose is licensed under the
`Creative Commons Attribution 4.0 International License`_ (CC BY 4.0).

Code listings are licensed under the `MIT License`_.


.. _`Creative Commons Attribution 4.0 International License`: LICENSE
.. _`MIT License`: source/code/LICENSE


.. |docs-status| image:: https://readthedocs.org/projects/leaf-obd/badge/?version=latest
    :target: https://leaf-obd.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. |test-status| image:: https://github.com/sethfischer/nissan-leaf-obd-manual/workflows/test/badge.svg
    :target: https://github.com/sethfischer/nissan-leaf-obd-manual/actions?query=workflow%3Atest
    :alt: Test Status
.. |linkcheck-status| image:: https://github.com/sethfischer/nissan-leaf-obd-manual/workflows/link%20check/badge.svg
    :target: https://github.com/sethfischer/nissan-leaf-obd-manual/actions?query=workflow%3A%22link+check%22
    :alt: Link Check Status
.. |license-cc-by-4.0| image:: https://img.shields.io/github/license/sethfischer/nissan-leaf-obd-manual
    :target: http://creativecommons.org/licenses/by/4.0/
    :alt: Attribution 4.0 International (CC BY 4.0)
.. |license-mit| image:: https://img.shields.io/badge/license-MIT-green
    :target: https://opensource.org/licenses/MIT
    :alt: MIT License
