from django.urls import path
from .views import InfoHumanApi

urlpatterns = [
    path('api/v1/data', InfoHumanApi.as_view()),
    path('api/v1/data/<int:pk>', InfoHumanApi.as_view()),
]