from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, response, status

from core.models import Link

from .serializers import (
    LinkLongUrlSerializer,
    LinkSerializer,
    LinkShortUrlSerializer,
    ShortenLinkSerializer,
)


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

    description = """Shorten an URL. Body example:
    * long_url: https://google.com
    * length: 4 (default = 5, minimum = 3)
    """

    @swagger_auto_schema(
        operation_description=description,
        responses={status.HTTP_201_CREATED: LinkShortUrlSerializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ExtendLinkAPIView(generics.GenericAPIView):
    description = "Extend an URL from a shortened representation (shortening reversion)."

    @swagger_auto_schema(
        operation_description=description,
        responses={status.HTTP_200_OK: LinkLongUrlSerializer},
        request_body=LinkShortUrlSerializer,
    )
    def post(self, request):
        serializer = LinkShortUrlSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        link = get_object_or_404(Link, short_url=serializer.validated_data["short_url"])
        serializer = LinkLongUrlSerializer(link)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
