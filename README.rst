##################################
pelican-diminuendo - HTML minifier
##################################

This Pelican plugin uses `python-diminuendo <https://github.com/hrbonz/python-diminuendo>`_ to minify HTML.

.. image:: https://travis-ci.org/hrbonz/pelican-diminuendo.svg?branch=master
    :target: https://travis-ci.org/hrbonz/pelican-diminuendo
    :alt: Testing Status

.. image:: https://readthedocs.org/projects/pelican-diminuendo/badge/?version=latest
    :target: https://readthedocs.org/projects/pelican-diminuendo/?badge=latest
    :alt: Documentation Status

.. image:: http://img.shields.io/badge/license-BSD%203--Clause-blue.svg
    :target: http://opensource.org/licenses/BSD-3-Clause
    :alt: license BSD 3-Clause


Install
=======

.. code-block:: sh

    $ pip install pelican-diminuendo

Usage
=====

To use the plugin, add it to the PLUGINS list in your configuration file. Put it in pelicanconf.py by default:

.. code-block:: python

    PLUGINS = [
        # ...
        'pelican-diminuendo',
    ]

Development
===========

Test
----

Test the package:

.. code-block:: sh

    $ python -m unittest discover

Automatic testing in various environments:

.. code-block:: sh

    $ tox

Release
=======

Use `bumpr` to release the package:

.. code-block:: sh

    $ bumpr -b -m

Project
=======

* `Source code on github <https://github.com/hrbonz/pelican-diminuendo>`_
* `Documentation on readthedocs <http://pelican-diminuendo.readthedocs.org/>`_
* `Package on pypi <https://pypi.python.org/pypi/pelican-diminuendo>`_

License
=======

pelican-diminuendo is published under a BSD 3-clause license, see the LICENSE
file distributed with the project.
