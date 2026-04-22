from django.urls import path

from veiculo.views import (
    CriarVeiculos,
    EditarVeiculos,
    ExcluirVeiculo,
    FotoVeiculo,
    ListarVeiculos,
)

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='listar-veiculos'),
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='foto-veiculo'),
    path('novo/', CriarVeiculos.as_view(), name='criar-veiculos'),
    path('editar/<int:pk>/', EditarVeiculos.as_view(), name='editar-veiculos'),
    path('excluir/<int:pk>/', ExcluirVeiculo.as_view(), name='excluir-veiculo'),
]