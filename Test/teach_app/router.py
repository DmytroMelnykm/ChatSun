from rest_framework import routers
from .serializers import DataLook, WriteData


router = routers.DefaultRouter()
router.register('get/data/', DataLook)
router.register('write/data/', WriteData)
