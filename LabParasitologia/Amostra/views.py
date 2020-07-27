from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from Usuario.models import User
from .models import Amostra
from .forms import AmostraForm
from Exame.models import Exame, RealizacaoExame
from datetime import date, timedelta,datetime
from .forms import amostraForm
import json
from dateutil.relativedelta import *

def home(request):
    exame = Exame.objects.all()
    Rexame = RealizacaoExame.objects.all()
    amostra = Amostra.objects.all()
    AB = Amostra.objects.filter(status=True)
    user = User.objects.filter(username=request.user.username)[0]

    ultimo_12 = []
    mesE = []
    mesA = []
    LE = []
    LEV = []
    i = 0
    j = 0
    a1 = 1
    a2 = 1
    a = 1
    ex = 0

    tdy = date.today()
    ultimo_ano = tdy+relativedelta(years=-1)
    ultimo_seis_meses = tdy+relativedelta(months=-6)
    coluna = ultimo_ano

    MAB = 0
    qtdE = 0
    qtdA = 0
    qtdAT = 0
    qtdAB = 0

    while(ex <=12):
        coluna = coluna + relativedelta(months=1)
        if coluna.month <= tdy.month:
            ultimo_12.insert(a, str(coluna.month)+"/"+str(coluna.year))
            a = a + 1
        ex = ex + 1
    coluna = ultimo_ano
    while(a <=12):
        coluna = coluna + relativedelta(months=1)
        if coluna.month > tdy.month:
            ultimo_12.insert(a, str(coluna.month)+"/"+str(coluna.year))
        a = a + 1

    for item in AB:
        qtdAB = qtdAB + 1
        if item.responsavel == user:
            MAB = MAB + 1

    for item in amostra:
        if item.created_at.month == tdy.month:
            qtdA = qtdA + 1
        qtdAT = qtdAT+1

    while (a1 <= 12):
        for a in amostra:
            if (item.data_coleta >= ultimo_ano and item.data_coleta <= tdy):
                if a.data_coleta.month == a1: j = j + 1
        mesA.insert(a1, j)
        a1 = a1 + 1
        j = 0

    for item in Rexame:
        if item.data.month == tdy.month:
            qtdE = qtdE + 1

    while (a2 <= 12):
        for e in Rexame:
            if (item.data >= ultimo_ano and item.data <= tdy):
                if e.data.month == a2: j = j + 1
        mesE.insert(a2, j)
        a2 = a2 + 1
        j = 0

    for e in exame:
        LE.insert(i, e.nome)
        for item in Rexame:
            if (item.data >= ultimo_seis_meses and item.data <= tdy):
                if LE[i] == item.exame.nome: j = j + 1
        LEV.insert(i, j)
        i = i + 1
        j = 0
    json_coluna = json.dumps(ultimo_12)
    json_mesA = json.dumps(mesA)
    json_mesE = json.dumps(mesE)
    json_LE = json.dumps(LE)
    json_LEV = json.dumps(LEV)

    if qtdAT == 0:
        pctAB = (qtdAB * 100) / 1
    else:
        pctAB = (qtdAB*100)/qtdAT
    context = {'qtdE':qtdE,'qtdA':qtdA,'tdy':tdy,'MAB':MAB,'exame':exame,'pctAB':round(pctAB, 2),'mesA':json_mesA,'mesE':json_mesE,'LE':json_LE,'LEV':json_LEV,'coluna':json_coluna}
    return render(request, 'Amostra/index.html', context)

@login_required
def listar(request):
    amostras = Amostra.objects.filter(status = True)
    quinze = date.today() - timedelta(days=15)
    dez = date.today() - timedelta(days=10)
    context = {'lista_amostras': amostras, 'titulo': "Amostras", 'amostrasUsuario': False,
               'finalizadas': False, 'paginaRetorno': 'Amostra:listar','quinze':quinze,'dez':dez}
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
    quinze = date.today() - timedelta(days=15)
    dez = date.today() - timedelta(days=10)
    context = {'lista_amostras': amostras, 'titulo': "Minhas amostras", 'amostrasUsuario': True,
               'finalizadas': False, 'paginaRetorno': 'Amostra:listarAmostraUser','quinze':quinze,'dez':dez}
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
def listarAlertas(request):
    quinze = date.today() - timedelta(days=15)
    dez = date.today() - timedelta(days=10)
    amostras_alerta = Amostra.objects.filter(
        responsavel=request.user,
        status=True,
        data_coleta__lte=date.today() - timedelta(days=10)).order_by('data_coleta')
    context = {'lista_amostras': amostras_alerta, 'titulo': "Amostras com alerta", 'amostrasUsuario': True,
               'finalizadas': False, 'paginaRetorno': 'Amostra:listarAlertas','quinze':quinze,'dez':dez}
    return render(request, 'Amostra/listar.html', context)

