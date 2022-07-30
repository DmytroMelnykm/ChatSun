from django.urls import path, include
from .views import InfoHumanApi, AddInfoHumanApi

urlpatterns = [
    path('api/v1/write', AddInfoHumanApi.as_view()),
]
#path('to/data/', WorkData.as_view(), name='write_data'),