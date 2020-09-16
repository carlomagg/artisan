from rest_framework import serializers
from artisan.models import Artisan

# Passenger Serializer
class ArtisanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artisan
        fields = '__all__'