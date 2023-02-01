from rest_framework import serializers
from aplicacao.models import Presentes, Eventos
from django.contrib.auth.models import User

class PresenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentes
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = '__all__'
