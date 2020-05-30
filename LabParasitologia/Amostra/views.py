from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from Usuario.models import User
from .models import Amostra
from .forms import AmostraForm

def home(request):
	return render(request, 'Amostra/index.html')

@login_required
def listar(request):
	amostras = Amostra.objects.filter(status = True)
	context = {'lista_amostras': amostras, 'titulo': "Amostras", 'amostrasUsuario': False,
               'finalizadas': False, 'paginaRetorno': 'Amostra:listar'}
	return render(request, 'Amostra/listar.html', context)

@login_required
def listarFinalizada(request):
	amostras = Amostra.objects.filter(status = False)
	context = {'lista_amostras': amostras, 'titulo': "Amostras finalizadas", 'amostrasUsuario': False,
               'finalizadas': True, 'paginaRetorno': 'Amostra:listarFinalizada'}
	return render(request, 'Amostra/listar.html', context)

@login_required
def listarAmostraUser(request, pk):
	amostras = Amostra.objects.filter(responsavel_id=pk,  status = True)
	context = {'lista_amostras': amostras, 'titulo': "Minhas amostras", 'amostrasUsuario': True,
               'finalizadas': False, 'paginaRetorno': 'Amostra:listarAmostraUser'}
	return render(request, 'Amostra/listar.html', context)

@login_required
def listarAmostraFinalizada(request, pk):
	amostras = Amostra.objects.filter(responsavel_id=pk,  status = False)
	context = {'lista_amostras': amostras, 'titulo': "Minhas amostras finalizadas", 'amostrasUsuario': True,
               'finalizadas': True, 'paginaRetorno': 'Amostra:listarAmostraUserFinalizada'}
	return render(request, 'Amostra/listar.html', context)

@login_required
def adicionar(request):
    if request.method=="POST":
        amostra_form = AmostraForm(request.POST)

        if amostra_form.is_valid():
            amostra = amostra_form.save()
            amostra.save()
            return listar(request)

        else:
            print(amostra_form.errors)
    else:
        amostra_form = AmostraForm()

    return render(request, 'Amostra/adicionar.html',
                        {'amostra_form':amostra_form})

def mudar_status(request, status, amostra):
    amostra = Amostra.objects.get(pk=amostra)
    if (status==1):
        amostra.status = True
    else:
        amostra.status = False
    amostra.save()
    return redirect(request.POST.get('next', '/'))

class CriarAmostra(LoginRequiredMixin, generic.CreateView):
    fields = ('data_coleta', 'origem', 'local_coleta','especie_animal', 'identificacao', 'tipo_amostra','sexo_animal')
    model = Amostra
    template_name = 'Amostra/adicionar.html'

    def form_valid(self, form):
        user = User.objects.filter(username=self.request.user.username)[0]
        form.instance.responsavel = user
        return super(CriarAmostra, self).form_valid(form)

    def get_success_url(self):

        if 'add' in self.request.POST:
            url = reverse_lazy('amostra:adicionar')
        else:
            url = reverse_lazy('amostra:listar')

        return url


class DetalheAmostra(LoginRequiredMixin, generic.DetailView):
    model = Amostra
    template_name = "Amostra/amostra_detail.html"

class EditarAmostra(LoginRequiredMixin, generic.UpdateView):
    model = Amostra
    fields = ['data_coleta', 'origem', 'local_coleta','especie_animal', 'identificacao', 'tipo_amostra','sexo_animal']
    template_name = 'Amostra/amostra_update_form.html'

    def get_success_url(self):
        return(self.request.POST.get('next', '/'))

class DeletarAmostra(LoginRequiredMixin, generic.DeleteView):
    model = Amostra
    template_name = 'Amostra/listar.html'

    def get_success_url(self):
        return(self.request.POST.get('next', '/'))

