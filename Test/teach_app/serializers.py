from rest_framework import serializers, viewsets, generics
from .models import InfoHuman

"""Name = serializers.CharField(max_length=100)
    Surname = serializers.CharField(max_length=100)
    Born = serializers.DateTimeField()
    Age = serializers.ImageField()"""


class DataHuman(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InfoHuman
        fields = ['Name', 'Surname', 'Born', 'Age']


class DataLook(viewsets.ModelViewSet):
    queryset = InfoHuman.objects.all()
    serializer_class = DataHuman


class WriteData(viewsets.ModelViewSet):
    queryset = InfoHuman.objects.all()
    serializer_class = DataHuman

    def update(self, request, *args, **kwargs):
        self.queryset = InfoHuman(Name=request.data.get('Name'),
                                  Surname=request.data.get('Surname'),
                                  Born=request.data.get('Born'),
                                  Age=request.data.get('Age')).save()




