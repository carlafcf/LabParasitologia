from django.views.generic import CreateView
from django.views import generic
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from . import forms
from .models import User

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('usuario:listar')
    template_name = 'Usuario/cadastrar.html'


class EditarUsuario(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = forms.EditarUsuarioForm
    template_name = 'Usuario/editarUsuario.html'
    success_url = reverse_lazy('usuario:listar')

@login_required
def listarUsuarios(request):
    user = User.objects.filter(is_active=True)
    context = {'lista_user':user}
    return render(request, 'Usuario/listarUser.html', context)

class DetalheUser(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "Usuario/user_detail.html"

class DeletarUser(LoginRequiredMixin, generic.DeleteView):
    model = User
    template_name = 'Usuario/listarUser.html'
    success_url = reverse_lazy('usuario:listar')

def mudar_coordenacao_status(request, coord_status, usuario):
    user = User.objects.get(pk=usuario)
    if (coord_status==1):
        user.is_superuser = True
    else:
        user.is_superuser = False
    user.save()
    return redirect('usuario:listar')

def mudar_ativo_status(request, ativo_status, usuario):
    user = User.objects.get(pk=usuario)
    if (ativo_status==1):
        user.is_active = True
    else:
        user.is_active = False
    user.save()
    return redirect('usuario:listar')

@login_required
def usuariosInativos(request):
    user = User.objects.filter(is_active=False)
    context = {'lista_user':user}
    return render(request, 'Usuario/usuarios_inativos.html', context)
