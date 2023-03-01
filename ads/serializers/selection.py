from rest_framework import serializers
from ads.models import Ad, Selection
from ads.serializers.ad import AdListSerializer


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
        fields = ["id"]
