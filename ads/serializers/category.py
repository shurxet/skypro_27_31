from rest_framework import serializers
from ads.models import Category


class CategoryCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Category
        fields = "__all__"