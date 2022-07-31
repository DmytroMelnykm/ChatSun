from django.db import models
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import InfoHuman
from .serializers import HumanSerilaze


class InfoHumanApi(APIView):
    @staticmethod
    def __valid_method(request, instance: models = None) -> serializers:
        serilizer = HumanSerilaze(data=request.data, instance=instance)
        serilizer.is_valid(raise_exception=True)
        serilizer.save()
        return serilizer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'users': HumanSerilaze(InfoHuman.objects.all(), many=True).data, 
                             'count': InfoHuman.objects.all().count()})

        try:
            instance = InfoHuman.objects.get(pk=pk)
            data_by_id = HumanSerilaze(InfoHuman.objects.get(pk=pk)).data
        except:
            return Response({'error': 'Object not found'})

        return Response({'user': data_by_id})

    def post(self, request) -> Response:
        serilizer = self.__valid_method(request)
        return Response({'user': serilizer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Put not allowed'})

        try:
            instance = InfoHuman.objects.get(pk=pk)
        except:
            return Response({'error': 'Object not found'})

        serilizer = self.__valid_method(request=request, instance=instance)
        return Response({'user': serilizer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'delete not allowed'})

        try:
            instance = InfoHuman.objects.get(pk=pk)
            data_for_delete = HumanSerilaze(InfoHuman.objects.get(pk=pk)).data
            instance.delete()
        except:
            return Response({'error': 'Object not found'})

        return Response({'user': data_for_delete})
