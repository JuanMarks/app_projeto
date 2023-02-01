from django.shortcuts import render
from rest_framework import viewsets
from aplicacao.models import Presentes, Eventos
from .serializer import PresenteSerializer, UsersSerializer, EventoSerializer
from django.contrib.auth.models import User


class PresentesViewSet(viewsets.ModelViewSet):
    queryset = Presentes.objects.all()
    serializer_class = PresenteSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Eventos.objects.all()
    serializer_class = EventoSerializer