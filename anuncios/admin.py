from django.contrib import admin
from anuncios.models import Anuncio


class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'valor', 'data_criacao', 'veiculo', 'usuario')
    search_fields = ('titulo', 'descricao', 'veiculo__modelo')
    list_filter = ('data_criacao', 'valor', 'veiculo__marca')

admin.site.register(Anuncio, AnuncioAdmin)
