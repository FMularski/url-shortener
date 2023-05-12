from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status

from core.models import Link

from .serializers import LinkShortUrlSerializer, ShortenLinkSerializer


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
