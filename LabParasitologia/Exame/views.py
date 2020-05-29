from django.shortcuts import render
from . import forms
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import RealizacaoExame


class AdicionarExame(LoginRequiredMixin, generic.CreateView):
    fields = ('exame','amostra', 'resultado')
    model = RealizacaoExame
    template_name = 'Exame/AdicionarExame.html'

    def get_success_url(self):

        if 'add' in self.request.POST:
            url = reverse_lazy('exame:AdicionarExame')
        else:
            url = reverse_lazy('amostra:listar')

        return url
