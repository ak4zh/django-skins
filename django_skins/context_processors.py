from django.conf import settings


def template(request):
    """
        Get all settings related to the Django Skins module and return them as context variables
    """
    context = {
        skin_name = getattr(settings, 'DJANGO_SKIN_NAME', default='volt'),

        # view names
        login_view = getattr(settings, 'DJANGO_SKINS_LOGIN_VIEW_NAME', 'login')
        logout_view = getattr(settings, 'DJANGO_SKINS_LOGOUT_VIEW_NAME', 'logout')
        signup_view = getattr(settings, 'DJANGO_SKINS_SIGNUP_VIEW_NAME', 'signup')

        # meta data
        site_meta = getattr(settings, 'DJANGO_SKINS_SITE_META')
        facebook_meta = getattr(settings, 'DJANGO_SKINS_FACEBOOK_META')
        twitter_meta = getattr(settings, 'DJANGO_SKINS_TWITTER_META')

    }
    return context
