from rest_framework import routers
from .views import ImageGet, ImageSet


router = routers.DefaultRouter()
router.register(r'^get', ImageGet.as_view(), base_name='image-get')
router.register(r'^set', ImageSet.as_view(), base_name='image-set')
