from django.urls import path, include
from .views import WorkData
from .router import router

urlpatterns = [
    path('', include(router.urls)),
    path('api', include('rest_framework.urls', namespace='rest_framework')),
    path('to/data/', WorkData.as_view(), name='write_data'),
]
