from rest_framework import serializers


def is_published_validator(value: bool):
    if value:
        raise serializers.ValidationError(
            "When creating an ad, the is_published field will not help to be True"
        )


