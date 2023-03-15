import pytest


@pytest.mark.django_db
def test_create_selection(client, user, ad, token):
    expected_response = {
        "id": 1,
        "name": "name",
        "owner": user.pk,
        "items": [ad.pk]
    }

    data = {
        "name": "name",
        "owner": user.pk,
        "items": [ad.pk]
    }

    response = client.post(
        "/selection/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Token " + token
    )

    assert response.status_code == 201
    assert response.data == expected_response
