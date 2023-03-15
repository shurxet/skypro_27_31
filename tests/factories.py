import factory

from authentication.models import User
from ads.models import Ad


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = "password"
    email = factory.Faker("email")


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "test_name_test"
    author = factory.SubFactory(UserFactory)
    price = 100
    is_published = False
