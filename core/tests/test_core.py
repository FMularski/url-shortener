import pytest
from django.shortcuts import reverse
from rest_framework import status

from core.models import Link


@pytest.mark.django_db
@pytest.mark.parametrize(
    "test_url, response_status",
    (
        ["http://test-url.com", status.HTTP_201_CREATED],
        ["https://test-url.com", status.HTTP_201_CREATED],
        ["htps://invalid-url.com", status.HTTP_400_BAD_REQUEST],
        ["invalid-url.com", status.HTTP_400_BAD_REQUEST],
        ["", status.HTTP_400_BAD_REQUEST],
    ),
)
def test_create_link(api_client, test_url, response_status):
    post_url = reverse("shorten")
    response = api_client.post(post_url, data={"long_url": test_url})

    assert response.status_code == response_status


@pytest.mark.django_db
def test_redirect(api_client):
    test_url = "http://test-url.com"
    post_url = reverse("shorten")
    response = api_client.post(post_url, data={"long_url": test_url}).json()
    short_url = response["short_url"]
    response = api_client.get(short_url)

    assert response.status_code == status.HTTP_301_MOVED_PERMANENTLY


@pytest.mark.django_db
def test_extend(api_client):
    test_url = "http://test-url.com"
    shorten_url = reverse("shorten")
    response = api_client.post(shorten_url, data={"long_url": test_url}).json()

    # manually replace testserver with localhost as it is not treated as a valid url
    short_url = response["short_url"].replace("testserver", "localhost")
    link = Link.objects.first()
    link.short_url = link.short_url.replace("testserver", "localhost")
    link.save()

    extend_url = reverse("extend")
    response = api_client.post(extend_url, data={"short_url": short_url}).json()
    long_url = response["long_url"]

    assert long_url == test_url


@pytest.mark.django_db
def test_links_list(api_client):
    get_url = reverse("links")
    response = api_client.get(get_url)

    assert response.status_code == status.HTTP_200_OK
