from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'autenticacao.html', {})

    def post(self, request):
        nome_usuario = request.POST.get('username')
        senha = request.POST.get('password')

        usuario = authenticate(request, username=nome_usuario, password=senha)

        if usuario is not None:
            if usuario.is_active:
                login(request, usuario)
                return redirect('home')  
            else:
                return render(request, 'autenticacao.html', {'erro': 'Usuário inativo.'})
        else:
            return render(request, 'autenticacao.html', {'erro': 'Usuário ou senha inválidos.'})


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('index')
