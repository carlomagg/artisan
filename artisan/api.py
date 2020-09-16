
from rest_framework import viewsets, permissions
from artisan.models import Artisan
from .serializers import ArtisanSerializer

# Bookrides Viewset
class ArtisanViewSet(viewsets.ModelViewSet):
    queryset = Artisan.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ArtisanSerializer