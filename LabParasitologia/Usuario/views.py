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
    success_url = reverse_lazy('usuario:login')
    template_name = 'Usuario/cadastrar.html'


class EditarUsuario(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = forms.EditarUsuarioForm
    template_name = 'Usuario/editarUsuario.html'
    success_url = reverse_lazy('amostra:listar')

@login_required
def menuUsuarios(request):
    user = User.objects.all()
    context = {'lista_user':user}
    return render(request, 'Usuario/listarAmostraUser.html', context)

class DetalheUser(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "Usuario/user_detail.html"

class DeletarUser(LoginRequiredMixin, generic.DeleteView):
    model = User
    template_name = 'Usuario/deletar_user.html'
    success_url = reverse_lazy('usuario:menu')