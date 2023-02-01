from django.contrib import admin
from .models import Presentes, Eventos

# Register your models here.

class ListandoPresentes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco')
    list_display_links = ('id', 'nome')
    list_per_page = 10

admin.site.register(Presentes, ListandoPresentes)

class ListandoEventos(admin.ModelAdmin):
    list_display = ('id', 'nome_evento')
    list_display_links = ('id', 'nome_evento')

admin.site.register(Eventos, ListandoEventos)
