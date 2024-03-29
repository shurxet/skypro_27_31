from rest_framework.viewsets import ModelViewSet
from authentication.models import Location
from authentication.serializers.location import LocationSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
