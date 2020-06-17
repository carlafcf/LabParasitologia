from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from Usuario.models import User
from .models import Amostra
from .forms import AmostraForm
from Exame.models import Exame
from datetime import date, timedelta
from .forms import amostraForm

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
        form = amostraForm(request.POST)

        if form.is_valid():
            user = User.objects.filter(username=request.user.username)[0]
            form.instance.responsavel = user
            amostra = form.save()
            amostra.save()
            return listar(request)

        else:
            print(form.errors)
    else:
        form = amostraForm()

    return render(request, 'Amostra/adicionar.html',
                        {'form':form})

def mudar_status(request, status, amostra):
    amostra = Amostra.objects.get(pk=amostra)
    if (status==1):
        amostra.status = True
    else:
        amostra.status = False
    amostra.save()
    return redirect(request.POST.get('next', '/'))

class CriarAmostra(LoginRequiredMixin, generic.CreateView):
    form_class = amostraForm
    model = Amostra
    template_name = 'Amostra/adicionar.html'


    def get_initial(self):
        if 'add' in self.request.POST:
            initial = super(CriarAmostra, self).get_initial()
            obj = Amostra.objects.filter(responsavel_id=self.request.user.pk).order_by('-id')[0]
            initial['data_coleta'] = obj.data_coleta
            initial[ 'origem'] = obj.origem
            initial['localidade'] = obj.localidade
            initial['setor'] = obj.setor
            initial['especie_animal'] = obj.especie_animal
        else:
            initial = super(CriarAmostra, self).get_initial()
        return initial

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


#class DetalheAmostra(LoginRequiredMixin, generic.DetailView):
#    model = Amostra
#    template_name = "Amostra/amostra_detail.html"


class EditarAmostra(LoginRequiredMixin, generic.UpdateView):
    model = Amostra
    form_class = amostraForm
    template_name = 'Amostra/amostra_update_form.html'

    def get_success_url(self):
        return(self.request.POST.get('next', '/'))

class DeletarAmostra(LoginRequiredMixin, generic.DeleteView):
    model = Amostra
    template_name = 'Amostra/listar.html'

    def get_success_url(self):
        return(self.request.POST.get('next', '/'))

@login_required
def listarAlertas(request):
    amostras_alerta = Amostra.objects.filter(
        responsavel=request.user,
        status=True,
        data_coleta__lte=date.today() - timedelta(days=10)).order_by('data_coleta')
    context = {'lista_amostras': amostras_alerta, 'titulo': "Amostras com alerta", 'amostrasUsuario': True,
               'finalizadas': False, 'paginaRetorno': 'Amostra:listarAlertas'}
    return render(request, 'Amostra/listar.html', context)

