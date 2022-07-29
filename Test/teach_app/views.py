import datetime

from django.http import HttpResponse
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
