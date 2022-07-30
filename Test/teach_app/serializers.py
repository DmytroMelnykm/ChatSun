import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import InfoHuman
from dataclasses import dataclass

"""Name = serializers.CharField(max_length=100)
    Surname = serializers.CharField(max_length=100)
    Born = serializers.DateTimeField()
    Age = serializers.ImageField()"""


@dataclass
class InfoHumanModel:
    Name: str
    Surname: str
    Born: str
    Age: int


class HumanSerilaze(serializers.Serializer):
    Name = serializers.CharField(max_length=100)
    Surname = serializers.CharField(max_length=100)
    Born = serializers.DateTimeField()
    Age = serializers.IntegerField()

    def create(self, validated_data):
        return InfoHuman.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Surname = validated_data.get('Surname', instance.Surname)
        instance.Born = validated_data.get('Born', instance.Born)
        instance.Age = validated_data.get('Age', instance.Age)
        instance.save()
        return instance
