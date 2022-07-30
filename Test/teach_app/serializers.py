from rest_framework import serializers, viewsets, generics
from .models import InfoHuman
from .ClassStructure.HumanTuple import InfoHumanTuple
from rest_framework.permissions import IsAuthenticated

"""Name = serializers.CharField(max_length=100)
    Surname = serializers.CharField(max_length=100)
    Born = serializers.DateTimeField()
    Age = serializers.ImageField()"""


class DataHuman(serializers.ModelSerializer):
    class Meta:
        model = InfoHuman
        fields = ('Name', 'Surname', 'Born', 'Age')

"""
class DataLook(viewsets.ModelViewSet):
    queryset = InfoHuman.objects.all()
    serializer_class = DataHuman


DATA_HUMAN = InfoHumanTuple(Name='Vova', Surname='Melnyk', Born='2021-05-25', Age=15)



"""

