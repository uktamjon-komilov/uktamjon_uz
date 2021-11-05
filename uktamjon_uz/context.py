from django.conf import settings


def site_data(request):
    return {
        "default_title": settings.SITE_DEFAULT_TITLE
    }