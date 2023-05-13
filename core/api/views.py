from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status

from core.models import Link

from .serializers import LinkSerializer, LinkShortUrlSerializer, ShortenLinkSerializer


class LinkListView(generics.ListAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()

    @swagger_auto_schema(
        operation_description="Returns the list of all shortened urls.",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ShortenLinkAPIView(generics.CreateAPIView):
    serializer_class = ShortenLinkSerializer
    queryset = Link.objects.all()

    description = """Shorten an URL.

    Input example:
    * long_url: https://google.com
    * length: 4 (default = 5, minimum = 3)
    """

    @swagger_auto_schema(
        operation_description=description,
        responses={status.HTTP_201_CREATED: LinkShortUrlSerializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
