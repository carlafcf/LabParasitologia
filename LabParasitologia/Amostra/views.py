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

def home(request):
    tdy = datetime.today()
    exame = Exame.objects.all()
    Rexame = RealizacaoExame.objects.all()
    amostra = Amostra.objects.all()
    AB = Amostra.objects.filter(status=True)
    user = User.objects.filter(username=request.user.username)[0]
    MAB = 0
    qtdE = 0
    qtdA = 0
    qtdAB = 0
    pctAB = 0
    jan = 0
    fev = 0
    mar = 0
    abr = 0
    mai = 0
    jun = 0
    jul = 0
    ago = 0
    set = 0
    out = 0
    nov = 0
    dez = 0
    jan1 = 0
    fev1 = 0
    mar1 = 0
    abr1 = 0
    mai1 = 0
    jun1 = 0
    jul1 = 0
    ago1 = 0
    set1 = 0
    out1 = 0
    nov1 = 0
    dez1 = 0
    famacha = 0
    exame2 = 0
    exame3 = 0
    for item in AB:
        qtdAB = qtdAB + 1
        if item.responsavel == user:
            MAB = MAB + 1
    for item in amostra:
        if item.created_at.month == tdy.month:
            qtdA = qtdA + 1
        if item.created_at.month == 1:   jan = jan + 1
        if item.created_at.month == 2:   fev = fev + 1
        if item.created_at.month == 3:   mar = mar + 1
        if item.created_at.month == 4:   abr = abr + 1
        if item.created_at.month == 5:   mai = mai + 1
        if item.created_at.month == 6:   jun = jun + 1
        if item.created_at.month == 7:   jul = jul + 1
        if item.created_at.month == 8:   ago = ago + 1
        if item.created_at.month == 9:   set = set + 1
        if item.created_at.month == 10:  out = out + 1
        if item.created_at.month == 11:  nov = nov + 1
        if item.created_at.month == 12:  dez = dez + 1
    for item in Rexame:
        if item.created_at.month == tdy.month:
            qtdE = qtdE + 1
        if item.created_at.month == 1:   jan1 = jan1 + 1
        if item.created_at.month == 2:   fev1 = fev1 + 1
        if item.created_at.month == 3:   mar1 = mar1 + 1
        if item.created_at.month == 4:   abr1 = abr1 + 1
        if item.created_at.month == 5:   mai1 = mai1 + 1
        if item.created_at.month == 6:   jun1 = jun1 + 1
        if item.created_at.month == 7:   jul1 = jul1 + 1
        if item.created_at.month == 8:   ago1 = ago1 + 1
        if item.created_at.month == 9:   set1 = set1 + 1
        if item.created_at.month == 10:  out1 = out1 + 1
        if item.created_at.month == 11:  nov1 = nov1 + 1
        if item.created_at.month == 12:  dez1 = dez1 + 1
        if item.exame.nome == 'Famacha': famacha = famacha + 1
        if item.exame.nome == 'exame2': exame2 = exame2 + 1
        if item.exame.nome == 'exame3': exame3 = exame3 + 1
    LE = [famacha, exame2, exame3]
    mesE = [jan1, fev1, mar1, abr1, mai1, jun1, jul1, ago1, set1, out1, nov1, dez1]
    mesA = [jan, fev, mar, abr, mai, jun, jul, ago, set, out, nov, dez]
    json_mesA = json.dumps(mesA)
    json_mesE = json.dumps(mesE)
    json_LE = json.dumps(LE)
    pctAB = (qtdAB*100)/qtdA
    context = {'qtdE':qtdE,'qtdA':qtdA,'tdy':tdy,'MAB':MAB,'exame':exame,'pctAB':round(pctAB, 2),'mesA':json_mesA,'mesE':json_mesE,'LE':json_LE}
    return render(request, 'Amostra/index.html', context)

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
    amostras_alerta = Amostra.objects.filter(
        responsavel=request.user,
        status=True,
        data_coleta__lte=date.today() - timedelta(days=10)).order_by('data_coleta')
    context = {'lista_amostras': amostras_alerta, 'titulo': "Amostras com alerta", 'amostrasUsuario': True,
               'finalizadas': False, 'paginaRetorno': 'Amostra:listarAlertas'}
    return render(request, 'Amostra/listar.html', context)

