from django.urls import path, include
from .views import InfoHumanApi

urlpatterns = [
    path('api/v1/list', InfoHumanApi.as_view()),
    path('api/v1/write', InfoHumanApi.as_view()),
    path('api/v1/put/<int:pk>', InfoHumanApi.as_view()),
    path('api/v1/delete/<int:pk>', InfoHumanApi.as_view())
]