from rest_framework import serializers

from authentication.models import Location, User


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


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
        slug_field="name"
    )

    class Meta:
        model = User
        fields = "__all__"

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop("location", [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for location in self._locations:
            location_obj, _ = Location.objects.get_or_create(name=location)
            user.location.add(location_obj)
        user.set_password(user.password)
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
            self._locations = self.initial_data.pop("location", [])
        else:
            self._locations = []
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        for location in self._locations:
            location_obj, _ = Location.objects.get_or_create(name=location)
            user.location.add(location_obj)
        user.set_password(user.password)
        user.save()
        return user


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]