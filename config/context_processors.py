from django.conf import settings

def cache_ttl(request):
    return {
        'CACHE_TTL': settings.CACHE_TTL,
    }

def debug(request):
    return {'DEBUG': settings.DEBUG}