import random
import string

from django.conf import settings
from rest_framework import serializers

from core.models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        exclude = ("id",)


class LinkLongUrlSerializer(serializers.Serializer):
    long_url = serializers.URLField()


class LinkShortUrlSerializer(serializers.Serializer):
    short_url = serializers.URLField()


class ShortenLinkSerializer(serializers.Serializer):
    long_url = serializers.URLField()
    length = serializers.IntegerField(required=False)

    def validate(self, attrs):
        if attrs.get("length", settings.SHORT_URL_DEFAULT_LENGTH) < 3:
            raise serializers.ValidationError("Lenght must be at least 3.")
        return super().validate(attrs)

    def create(self, validated_data):
        hostname = self.context["request"].build_absolute_uri("/")
        long_url = validated_data.get("long_url")
        length = validated_data.get("length", settings.SHORT_URL_DEFAULT_LENGTH)

        short_url = hostname + "".join(
            random.choices(string.ascii_lowercase + string.digits, k=length)
        )

        return Link.objects.create(long_url=long_url, short_url=short_url)

    def to_representation(self, instance):
        target_serializer = LinkShortUrlSerializer(instance)
        return target_serializer.data
