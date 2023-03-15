import pytest


@pytest.mark.django_db
def test_create_ad(client, token):
    expected_response = {
        "id": 1,
        "name": "test_name_test",
        "author": 1,
        "price": 100,
        "description": None,
        "is_published": False,
        "image": None,
        "category": None
    }

    data = {
        "name": "test_name_test",
        "author": 1,
        "price": 100,
        "is_published": False
    }

    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Token " + token
    )

    assert response.status_code == 201
    assert response.data == expected_response
