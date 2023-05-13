from django.urls import include, path

from .views import RedirectToShortenedView

urlpatterns = [
    path("api/", include("core.api.urls")),
    path("<short>/", RedirectToShortenedView.as_view(), name="redirect-to-shortened"),
]
