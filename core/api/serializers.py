import random
import socket
import string

from django.conf import settings
from rest_framework import serializers

from core.models import Link


class LinkShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ("short_url",)


class ShortenLinkSerializer(serializers.Serializer):
    long_url = serializers.URLField()
    length = serializers.IntegerField(required=False)

    def validate(self, attrs):
        if attrs.get("length", settings.SHORT_URL_DEFAULT_LENGTH) < 3:
            raise serializers.ValidationError("Lenght must be at least 3.")
        return super().validate(attrs)

    def create(self, validated_data):
        long_url = validated_data.get("long_url")
        length = validated_data.get("length", settings.SHORT_URL_DEFAULT_LENGTH)
        short_url = settings.SHORT_URL_BASE_URL + "".join(
            random.choices(string.ascii_lowercase + string.digits, k=length)
        )

        print(socket.gethostname())

        return Link.objects.create(long_url=long_url, short_url=short_url)

    def to_representation(self, instance):
        target_serializer = LinkShortUrlSerializer(instance)
        return target_serializer.data
