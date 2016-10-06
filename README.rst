========
Overview
========

.. start-badges

|travis|
|codecov|
|landscape|
|version|
|downloads|
|wheel|
|gitter|

.. |travis| image:: https://travis-ci.org/Pawamoy/django-cs-models.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/Pawamoy/django-cs-models/

.. |codecov| image:: https://codecov.io/github/Pawamoy/django-cs-models/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/Pawamoy/django-cs-models/

.. |landscape| image:: https://landscape.io/github/Pawamoy/django-cs-models/master/landscape.svg?style=flat
    :target: https://landscape.io/github/Pawamoy/django-cs-models/
    :alt: Code Quality Status

.. |version| image:: https://img.shields.io/pypi/v/django-cs-models.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/django-cs-models/

.. |downloads| image:: https://img.shields.io/pypi/dm/django-cs-models.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/django-cs-models/

.. |wheel| image:: https://img.shields.io/pypi/wheel/django-cs-models.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/django-cs-models/

.. |gitter| image:: https://badges.gitter.im/Pawamoy/django-cs-models.svg
    :alt: Join the chat at https://gitter.im/Pawamoy/django-cs-models
    :target: https://gitter.im/Pawamoy/django-cs-models?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge


.. end-badges

A Django app that helps you creating models within a Complex System.

License
=======

Software licensed under `MPL 2.0`_ license.

.. _BSD-2 : https://opensource.org/licenses/BSD-2-Clause
.. _MPL 2.0 : https://www.mozilla.org/en-US/MPL/2.0/

Installation
============

::

    pip install django-cs-models


Usage
=====

Two parameters have to be set in your settings. Here is an example:

.. code:: python

    COMPLEX_APP_NAME = 'ecosystem'

    COMPLEX_STRUCTURE = {
        'roots': [
            ['Organization', 'Committee', 'Board', 'Cohort'],
        ],
        'nodes': [
            ['ProjectTeam'],
            ['Resource'],
            ['Member'],
        ]
    }

Roots are entities that contain nodes (a root cannot contain another root).
Nodes are entities contained by and containing other nodes.

You can define roots and nodes at different levels, i.e. their position
in the hierarchy. These levels will tell if such entity can be
contained by such other entity.

Now in `ecosystem` app:

.. code:: python

    from csmodels.models import abstract_model

    class Cohort(abstract_model('Cohort')):
        your_model_fields_here = models.SomeField()

        class Meta:
            verbose_name = _('Cohort')
            verbose_name_plural = _('Cohorts')


The cohort model will inherit many to many relationships to
project teams, resources and members from the abstract model.

Of course, a change in the complex structure will change the models,
therefore migrations will be needed!

First diagram shows the example above.

.. image:: http://i.imgur.com/a2dGa9V.png
    :alt: Example diagram


Second diagram shows how links are created between entity depending on their
type (root or node) and their level. Letters (their names) are not important,
but numbers (their levels) are.

.. image:: http://i.imgur.com/apJNGpe.png
    :alt: Abstract diagram


Documentation
=============

https://github.com/Pawamoy/django-cs-models.wiki

Development
===========

To run all the tests: ``tox``
