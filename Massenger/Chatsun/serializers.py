from rest_framework import serializers
from .models import Chatsun


class ChatsunSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chatsun
        fields = ('pk', 'name', 'email', 'document', 'phone', 'registrationDate')