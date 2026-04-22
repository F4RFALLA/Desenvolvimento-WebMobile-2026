from django.db import models
from veiculo.consts import MARCA_CHOICES, COR_CHOICES, COMBUSTIVEL_CHOICES


class Veiculo(models.Model):
    marca = models.SmallIntegerField(choices=MARCA_CHOICES)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.SmallIntegerField(choices=COR_CHOICES)
    combustivel = models.SmallIntegerField(choices=COMBUSTIVEL_CHOICES)
    foto = models.ImageField(upload_to='veiculo/fotos', null=True, blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return f'{self.get_marca_display()} {self.modelo} ({self.ano})'

    @property
    def nome_exibicao(self):
        return f'{self.get_marca_display()} {self.modelo}'