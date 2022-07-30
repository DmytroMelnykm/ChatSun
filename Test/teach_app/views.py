"""from django.http import HttpResponse
from django.views import View
from .models import InfoHuman
from .ClassStructure.HumanTuple import InfoHumanTuple
import traceback

DATA_HUMAN = InfoHumanTuple(Name='Vova', Surname='Melnyk', Born='2021-05-25', Age=15)


class WorkData(View):
    Positive = 'done'
    Negative = 'failed'

    def get(self, request):
        try:
            InfoHuman(Name=DATA_HUMAN.Name, Surname=DATA_HUMAN.Surname, Born=DATA_HUMAN.Born, Age=DATA_HUMAN.Age).save()
            answer = self.Positive
        except:
            traceback.print_exc()
            answer = self.Negative

        return HttpResponse('{}'.format(answer))
"""


from rest_framework import generics
from rest_framework.response import Response

from .models import InfoHuman
from .serializers import DataHuman
from rest_framework.views import APIView


"""class InfoHumanApi(generics.ListAPIView):
    queryset = InfoHuman.objects.all()
    serializer_class = DataHuman
"""


class InfoHumanApi(APIView):
    @staticmethod
    def __get_all_list_human() -> list:
        return list(InfoHuman.objects.all().values())

    def get(self, request):
        return Response({'Data': self.__get_all_list_human})

    def post(self, request):
        return Response({'Data': self.__get_all_list_human})


class AddInfoHumanApi(APIView):
    @staticmethod
    def __get_all_list_human() -> list:
        return list(InfoHuman.objects.all().values())

    def get(self, request):
        return Response({'Data': self.__get_all_list_human})

    def post(self, request) -> Response:
        InfoHuman(Name=request.data['Name'],
                  Surname=request.data['Surname'],
                  Born=request.data['Born'],
                  Age=request.data['Age']).save()

        return Response({'Data': self.__get_all_list_human()})
