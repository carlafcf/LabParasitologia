from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from .models import Local
from Amostra.models import Amostra

class Cadastrar(LoginRequiredMixin, generic.CreateView):
    fields = ('nome',)
    model = Local
    template_name = 'Local/cadastrarLocal.html'

    def get_success_url(self):

        if 'add' in self.request.POST:
            url = reverse_lazy('local:cadastrar')
        else:
            url = reverse_lazy('local:listarLocal')
        return url

def localListar(request):
    local = Local.objects.all()
    context = {'listar_local':local}
    return render(request, 'Local/ListarLocal.html', context)

def listar_amostras_local(request, pk):
    local = Local.objects.filter(pk=pk)
    amostra = Amostra.objects.filter(localidade_id=pk)
    context = {'loc':local, 'lista_amostra':amostra}
    return render(request, 'Local/local_detail.html', context)

class Detalhes(LoginRequiredMixin, generic.DetailView):
    model = Local
    template_name = "Local/local_detail.html"

class Editar(LoginRequiredMixin, generic.UpdateView):
    model = Local
    fields = ['nome']
    template_name = 'Local/local_update.html'

    def get_success_url(self):
        return(self.request.POST.get('next', '/'))

class Deletar(LoginRequiredMixin, generic.DeleteView):
    model = Local
    template_name = 'Local/ListarLocal.html'

    def get_success_url(self):
        return(self.request.POST.get('next', '/'))

