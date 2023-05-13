from django.urls import path

from .views import ExtendLinkAPIView, LinkListView, ShortenLinkAPIView

urlpatterns = [
    path("links/", LinkListView.as_view(), name="links"),
    path("shorten/", ShortenLinkAPIView.as_view(), name="shorten"),
    path("extend/", ExtendLinkAPIView.as_view(), name="extend"),
]
