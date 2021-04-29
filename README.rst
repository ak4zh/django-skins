=============================
Django Skins
=============================

.. image:: https://badge.fury.io/py/django-skins.svg
    :target: https://badge.fury.io/py/django-skins

.. image:: https://travis-ci.org/ak4zh/django-skins.svg?branch=master
    :target: https://travis-ci.org/ak4zh/django-skins

.. image:: https://codecov.io/gh/ak4zh/django-skins/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/ak4zh/django-skins

easily apply skins to your django web app

Documentation
-------------

The full documentation is at https://django-skins.readthedocs.io.

Quickstart
----------

Install Django Skins::

    pip install django-skins

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_skins',
        ...
    )

Add django_skins.context_processors.template to context_processors:

.. code-block:: python

    TEMPLATES = [
            ...
            'OPTIONS': {
                'context_processors': [
                    ...
                    'django_skins.context_processors.template',
                ],
            ...
    ]
