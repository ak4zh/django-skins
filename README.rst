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
        'django_skins.apps.DjangoSkinsConfig',
        ...
    )

Add Django Skins's URL patterns:

.. code-block:: python

    from django_skins import urls as django_skins_urls


    urlpatterns = [
        ...
        url(r'^', include(django_skins_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
