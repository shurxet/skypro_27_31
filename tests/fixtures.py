import pytest


@pytest.fixture
@pytest.mark.django_db
def token(client, django_user_model):
    username = "name"
    password = "password"

    django_user_model.objects.create_user(
        username=username,
        password=password,
        role="hr"
    )

    response = client.post(
        "/user/login/",
        {"username": username, "password": password},
        format='json'
    )

    return response.data["token"]
