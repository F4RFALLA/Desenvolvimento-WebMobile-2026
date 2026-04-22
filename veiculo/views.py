from pathlib import Path

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from veiculo.forms import FormularioVeiculo
from veiculo.models import Veiculo


class ListarVeiculos(LoginRequiredMixin, ListView):
    model = Veiculo
    template_name = 'veiculo/listar.html'
    context_object_name = 'veiculos'
    paginate_by = 6

    def get_queryset(self):
        queryset = Veiculo.objects.all()

        busca = (self.request.GET.get('busca') or '').strip()
        if busca:
            queryset = queryset.filter(modelo__icontains=busca)

        ordenar = self.request.GET.get('ordenar', 'recentes')
        ordenacoes = {
            'recentes': '-id',
            'antigos': 'id',
            'ano_desc': '-ano',
            'ano_asc': 'ano',
            'modelo': 'modelo',
        }
        queryset = queryset.order_by(ordenacoes.get(ordenar, '-id'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['busca_atual'] = (self.request.GET.get('busca') or '').strip()
        context['ordenacao_atual'] = self.request.GET.get('ordenar', 'recentes')
        return context


class CriarVeiculos(LoginRequiredMixin, CreateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/form.html'
    success_url = reverse_lazy('listar-veiculos')


class EditarVeiculos(LoginRequiredMixin, UpdateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy('listar-veiculos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['veiculo'] = self.object
        return context


class ExcluirVeiculo(LoginRequiredMixin, View):
    def post(self, request, pk):
        veiculo = get_object_or_404(Veiculo, pk=pk)

        if veiculo.foto:
            veiculo.foto.delete(save=False)

        veiculo.delete()
        return redirect('listar-veiculos')


class FotoVeiculo(View):
    def get(self, request, arquivo):
        caminho_arquivo = Path(settings.MEDIA_ROOT) / 'veiculo' / 'fotos' / arquivo
        if not caminho_arquivo.exists() or not caminho_arquivo.is_file():
            raise Http404('Foto não encontrada.')

        try:
            return FileResponse(caminho_arquivo.open('rb'))
        except ObjectDoesNotExist:
            raise Http404('Foto não encontrada.')