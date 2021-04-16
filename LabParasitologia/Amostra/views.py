from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from Usuario.models import User
from .models import Amostra, RealizacaoExame
from .forms import AmostraForm
from Exame.models import Exame
from datetime import date, timedelta,datetime
from .forms import amostraForm
import json
from dateutil.relativedelta import *

@login_required
def home(request):

    tdy = date.today()

    #quantidade de amostras(mes)
    amostras_mes = Amostra.objects.filter(data_coleta__month = tdy.month)
    qtdA = amostras_mes.count()

    #quantidade de exames(mes)
    exames_mes = RealizacaoExame.objects.filter(data__month = tdy.month)
    qtdE = exames_mes.count()

    #minhas amostras abertas
    user = User.objects.filter(username=request.user.username)[0]
    minhas_amostras_abertas = Amostra.objects.filter(responsavel=user, status=True)
    MAB = minhas_amostras_abertas.count()

    #quantidade de amostras abertas
    amostras_abertas = Amostra.objects.filter(status=True).order_by('data_coleta')
    amostras_fechadas = Amostra.objects.filter(status=False)

    if (amostras_abertas.len() > 0):
        data_ultima_amostra_aberta = amostras_abertas[0].data_coleta
    else:
        data_ultima_amostra_aberta = date.today()
    data_30_dias = date.today() - timedelta(days=30)
    if(data_ultima_amostra_aberta < data_30_dias):
        amostras_fechadas = amostras_fechadas.filter(data_coleta__gte=data_30_dias)
    else:
        amostras_fechadas = amostras_fechadas.filter(data_coleta__gte=data_ultima_amostra_aberta)

    ultimo_seis_meses = tdy+relativedelta(months=-6)

    pctAB = (amostras_abertas.count() * 100)/(amostras_abertas.count() + amostras_fechadas.count())

    #amostras e exames cadastrados (últimos 12 meses)
    ultimo_12 = []
    mesE = []
    mesA = []
    LE = []
    LEV = []
    mes_atual = tdy.month
    ano_atual = tdy.year-1

    for i in range(1, 13):
        mes_atual += 1
        if (mes_atual == 13):
            mes_atual = 1
        if (mes_atual == 1):
            ano_atual += 1
        amostras_passadas = Amostra.objects.filter(data_coleta__month = mes_atual, data_coleta__year = ano_atual)
        exames_passados = RealizacaoExame.objects.filter(data__month = mes_atual, data__year = ano_atual)
        mesA.insert(i, amostras_passadas.count())
        mesE.insert(i, exames_passados.count())
        ultimo_12.insert(i, str(mes_atual)+"/"+str(ano_atual))
    
    #exames realizados (últimos 6 meses)
    exame = Exame.objects.filter(status=True)
    ultimo_seis_meses = tdy+relativedelta(months=-6)
    resultados_exame = RealizacaoExame.objects.filter(data__gte = ultimo_seis_meses)

    count = 0
    for e in exame:
        LE.insert(count, e.nome)
        LEV.insert(count, resultados_exame.filter(exame = e).count())
        count += 1

    #definição dos json
    json_coluna = json.dumps(ultimo_12)
    json_mesA = json.dumps(mesA)
    json_mesE = json.dumps(mesE)
    json_LE = json.dumps(LE)
    json_LEV = json.dumps(LEV)

    context = {'qtdE':qtdE,'qtdA':qtdA,'tdy':tdy,'MAB':MAB,
                'pctAB':round(pctAB, 2),'mesA':json_mesA,'mesE':json_mesE,
                'LE':json_LE,'LEV':json_LEV,'coluna':json_coluna, 'lista_exames': exame}
    return render(request, 'home.html', context)

@login_required
def listar_amostras(request):
    amostras = Amostra.objects.filter(status = True)
    quinze = date.today() - timedelta(days=15)
    dez = date.today() - timedelta(days=10)
    context = {'lista_amostras': amostras, 'titulo': "Amostras", 'amostrasUsuario': False,
               'finalizadas': False, 'paginaRetorno': 'Amostra:listar','quinze':quinze,'dez':dez}
    return render(request, 'Amostra/listar.html', context)

@login_required
def listar_amostras_finalizadas(request):
    amostras = Amostra.objects.filter(status = False)
    context = {'lista_amostras': amostras, 'titulo': "Amostras finalizadas", 'amostrasUsuario': False,
               'finalizadas': True, 'paginaRetorno': 'Amostra:listarFinalizada'}
    return render(request, 'Amostra/listar.html', context)

@login_required
def listar_amostras_usuario(request, pk):
    amostras = Amostra.objects.filter(responsavel_id=pk,  status = True)
    quinze = date.today() - timedelta(days=15)
    dez = date.today() - timedelta(days=10)
    context = {'lista_amostras': amostras, 'titulo': "Minhas amostras", 'amostrasUsuario': True,
               'finalizadas': False, 'paginaRetorno': 'Amostra:listarAmostraUser','quinze':quinze,'dez':dez}
    return render(request, 'Amostra/listar.html', context)

@login_required
def listar_amostras_finalizadas_usuario(request, pk):
    amostras = Amostra.objects.filter(responsavel_id=pk,  status = False)
    context = {'lista_amostras': amostras, 'titulo': "Minhas amostras finalizadas", 'amostrasUsuario': True,
               'finalizadas': True, 'paginaRetorno': 'Amostra:listarAmostraUserFinalizada'}
    return render(request, 'Amostra/listar.html', context)

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

    #def get_initial(self):
    #    if 'addmais' in self.request.POST:
    #        initial = super(CriarAmostra, self).get_initial()
    #        obj = Amostra.objects.filter(responsavel_id=self.request.user.pk).order_by('-id')[0]
    #        initial['data_coleta'] = obj.data_coleta
    #        initial[ 'origem'] = obj.origem
    #        initial['localidade'] = obj.localidade
    #        initial['setor'] = obj.setor
    #        initial['especie_animal'] = obj.especie_animal
    #    else:
    #        initial = super(CriarAmostra, self).get_initial()
    #    return initial

    def form_valid(self, form):
        user = User.objects.filter(username=self.request.user.username)[0]
        form.instance.responsavel = user
        return super(CriarAmostra, self).form_valid(form)

    def get_success_url(self):
        if 'addmais' in self.request.POST:
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
def listar_alertas(request):
    quinze = date.today() - timedelta(days=15)
    dez = date.today() - timedelta(days=10)
    amostras_alerta = Amostra.objects.filter(
        responsavel=request.user,
        status=True,
        data_coleta__lte=date.today() - timedelta(days=10)).order_by('data_coleta')
    context = {'lista_amostras': amostras_alerta, 'titulo': "Amostras com alerta", 'amostrasUsuario': True,
               'finalizadas': False, 'paginaRetorno': 'Amostra:listarAlertas','quinze':quinze,'dez':dez}
    return render(request, 'Amostra/listar.html', context)

