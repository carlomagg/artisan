from rest_framework import serializers
from locations.models import Location

# Passenger Serializer
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'