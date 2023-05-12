from django.urls import path

from .views import ShortenLinkAPIView

urlpatterns = [
    path("shorten/", ShortenLinkAPIView.as_view(), name="shorten"),
]
