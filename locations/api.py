
from rest_framework import viewsets, permissions
from locations.models import Location
from .serializers import LocationSerializer

# Bookrides Viewset
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LocationSerializer