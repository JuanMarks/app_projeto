from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Presentes(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='foto_presentes/%d/%m/%Y', blank=True)
    nome = models.CharField(max_length=100)
    preco = models.IntegerField(blank=True)

class Eventos(models.Model):
    nome_evento = models.CharField(max_length=100)
    data_inicio = models.DateTimeField(default=datetime.now(), blank=True)
    data_termino = models.DateTimeField(default=datetime.now(), blank=True)
    presentes = models.ForeignKey(Presentes, on_delete=models.CASCADE, blank=True)