from rest_framework import routers
from .api import ArtisanViewSet

router = routers.DefaultRouter()
router.register('api/artisan', ArtisanViewSet, 'artisan')

urlpatterns = router.urls 