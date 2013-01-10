import re
from django.core.cache import cache
from django.conf import settings

class NginxMemCacheMiddleWare:
    def process_response(self, request, response):
        url = request.get_full_path()

        cache_it = not settings.DEBUG \
            and request.method == 'GET' \
            and response.status_code == 200

        if cache_it:
            stoplist = [
                x for x
                in settings.CACHE_IGNORE_REGEXPS
                if re.match(x, url)
            ]
            if not stoplist:
                cache.set(url, response.content)

        return response

