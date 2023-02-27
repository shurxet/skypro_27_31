from rest_framework import serializers

<<<<<<< HEAD
from ads.models import Ad, Location, User, Category


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
=======
from ads.models import Ad, Category, Selection
from authentication.models import User
>>>>>>> b7ed7a2 (first commit)


class AdListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field="username"
    )

    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = Ad
        fields = "__all__"


<<<<<<< HEAD
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "role"]


class UserDetailSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        many=True,
        queryset=Location.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = User
        exclude = ["password"]


class UserCreateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
=======
class AdDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field="username"
    )

    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
>>>>>>> b7ed7a2 (first commit)
        slug_field="name"
    )

    class Meta:
<<<<<<< HEAD
        model = User
        fields = "__all__"

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop("location")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for location in self._locations:
            location_obj, _ = Location.objects.get_or_create(name=location)
            user.location.add(location_obj)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = User
        fields = "__all__"

    def is_valid(self, raise_exception=False):
        if "location" in self.initial_data:
            self._locations = self.initial_data.pop("location")
        else:
            self._locations = []
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        for location in self._locations:
            location_obj, _ = Location.objects.get_or_create(name=location)
            user.location.add(location_obj)
        user.save()
        return user


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
=======
        model = Ad
        fields = "__all__"


class AdCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Ad
        fields = "__all__"


class CategoryCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Category
        fields = "__all__"


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["id", "name"]


class SelectionDetailSerializer(serializers.ModelSerializer):
    items = AdListSerializer(many=True)

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionCreateUpdateSerializer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Ad.objects.all(),
        slug_field="id"
    )

    class Meta:
        model = Selection
        fields = "__all__"

    def is_valid(self, raise_exception=False):
        if "items" in self.initial_data:
            self._items = self.initial_data.pop("items", [])
        else:
            self._items = []
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        selection = super().save()

        for item in self._items:
            item_obj, _ = Ad.objects.get_or_create(pk=item)
            selection.items.add(item_obj)
        selection.save()
        return selection


class SelectionDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
>>>>>>> b7ed7a2 (first commit)
        fields = ["id"]
