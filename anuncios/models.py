from django.db import models
from veiculo.models import Veiculo
from django.contrib.auth.models import User


class Anuncio(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
