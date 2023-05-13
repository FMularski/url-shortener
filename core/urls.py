from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from .views import RedirectToShortenedView

description = """
Project created as a recruitment task. API for shortening URLs.

Created by mularskif@gmail.com
"""

schema_view = get_schema_view(
    openapi.Info(
        title="Shorten URLs API",
        default_version="v1",
        description=description,
        contact=openapi.Contact(email="mularskif@gmail.com"),
    ),
    public=True,
)

urlpatterns = [
    path("", schema_view.with_ui("swagger"), name="schema-swagger-ui"),
    path("api/", include("core.api.urls")),
    path("<short>/", RedirectToShortenedView.as_view(), name="redirect-to-shortened"),
]
