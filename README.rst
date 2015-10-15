/!\\ Warning /!\\
=================

This package is not registered not stored on PyPi.
All the following content is just **template** content.







django-cs-models
================


.. image:: https://pypip.in/version/django-cs-models/badge.svg
    :target: https://pypi.python.org/pypi/django-cs-models/
    :alt: Latest Version

.. image:: https://pypip.in/status/django-cs-models/badge.svg
    :target: https://pypi.python.org/pypi/django-cs-models/
    :alt: Development Status

.. image:: https://pypip.in/format/django-cs-models/badge.svg
    :target: https://pypi.python.org/pypi/django-cs-models/
    :alt: Download format

.. image:: https://travis-ci.org/Pawamoy/archan.svg?branch=master
    :target: https://travis-ci.org/Pawamoy/archan
    :alt: Build Status

.. image:: https://pypip.in/py_versions/django-cs-models/badge.svg
    :target: https://pypi.python.org/pypi/django-cs-models/
    :alt: Supported Python versions

.. image:: https://pypip.in/license/django-cs-models/badge.svg
    :target: https://pypi.python.org/pypi/django-cs-models/
    :alt: License


Installation
------------

Just run:

    pip install django-cs-models
    
Then add django-cs-models to the installed apps of your Django project:

.. code:: python

    # settings.py
    
    INSTALLED_APPS += ('cs_models')
    

Usage
-----

Two parameters have to be set in your settings. Here is an example:

.. code:: python

    COMPLEX_APP_NAME = 'ecosystem'
    
    COMPLEX_STRUCTURE = {
        'roots': [
            ['Organization', 'Committee', 'Board', 'Cohort'],
        ],
        'nodes': [
            [['ProjectTeam'], ],
            [['Resource'], ],
            [['Member'], ],
        ]
    }

Roots are entities that containes the others (a root cannot contain another root).
Nodes are entites contained by and containing other nodes.

You can define roots and nodes at different levels, i.e. their position in the hierarchy.
These levels will tell if such entity can be contained by such other entity.

First diagram shows the example above.
Second diagram shows how links are created between entity depending on their type (root or node) and their level. Letters (their names) are not important, but numbers (their levels) are.

.. image:: http://i.imgur.com/a2dGa9V.png
    :alt: Example diagram

.. image:: http://i.imgur.com/apJNGpe.png
    :alt: Abstract diagram
