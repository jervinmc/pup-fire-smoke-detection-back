from rest_framework import serializers
from .models import Recepient

class RecepientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recepient
        fields="__all__"
