from datetime import date

import pytest


@pytest.mark.django_db
def test_retrieve_ad(client, ad, token):
    expected_response = {
        "id": ad.pk,
        "name": "test_name_test",
        "author": ad.author.username,
        "price": ad.price,
        "description": None,
        "is_published": ad.is_published,
        "image": None,
        "category": None
    }

    response = client.get(
        f"/ad/{ad.pk}/",
        HTTP_AUTHORIZATION="Token " + token
    )

    assert response.status_code == 200
    assert response.data == expected_response
