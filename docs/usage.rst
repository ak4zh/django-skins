=====
Usage
=====

To use Django Skins in a project, add it to your `INSTALLED_APPS`:

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
