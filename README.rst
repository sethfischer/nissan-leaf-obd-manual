===========================
*Nissan Leaf* OBD-II manual
===========================

|docs-status| |test-status| |linkcheck-status|


Getting started
---------------

.. code:: console

    $ make install-ide-config
    $ make install-vale-styles
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

|cc-by-4.0|


.. |cc-by-4.0| image:: https://img.shields.io/github/license/sethfischer/nissan-leaf-obd-manual
    :target: http://creativecommons.org/licenses/by/4.0/
    :alt: Attribution 4.0 International (CC BY 4.0)
.. |docs-status| image:: https://readthedocs.org/projects/leaf-obd/badge/?version=latest
    :target: https://leaf-obd.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. |test-status| image:: https://github.com/sethfischer/nissan-leaf-obd-manual/workflows/test/badge.svg
    :target: https://github.com/sethfischer/nissan-leaf-obd-manual/actions?query=workflow%3Atest
    :alt: Test Status
.. |linkcheck-status| image:: https://github.com/sethfischer/nissan-leaf-obd-manual/workflows/link%20check/badge.svg
    :target: https://github.com/sethfischer/nissan-leaf-obd-manual/actions?query=workflow%3A%22link+check%22
    :alt: Link Check Status
