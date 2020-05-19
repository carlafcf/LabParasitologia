from django.views.generic import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('usuario:login')
    template_name = 'Usuario/cadastrar.html'

@login_required
def Update(request):
	return render(request, 'Usuario/editarUsuario.html')
