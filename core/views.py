from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView

from .models import Link


class RedirectToShortenedView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        short_url = self.request.build_absolute_uri()[:-1]  # remove the trailing "/"
        link = get_object_or_404(Link, short_url=short_url)

        return link.long_url
