from django.shortcuts import render, redirect
from .forms import RealizacaoExameForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
import json

from .forms import especieForm
from .models import RealizacaoExame, Exame
from Amostra.models import Amostra

def exameListar(request):
    exame_list = Exame.objects.all()
    paginator = Paginator(exame_list, 5)

    page = request.GET.get('page')
    exame = paginator.get_page(page)
    context = {'listar_exame':exame}
    return render(request, 'Exame/ListarExame.html', context)

def exame_amostraDetalhes(request, pk):
    amostra = Amostra.objects.filter(pk=pk)
    exame = RealizacaoExame.objects.filter(amostra_id=pk)
    context = {'a':amostra, 'lista_exame':exame}
    return render(request, 'Amostra/amostra_detail.html', context)


#class AdicionarExame(LoginRequiredMixin, generic.CreateView):
#    fields = ('exame','resultado')
#    model = RealizacaoExame
#    template_name = 'Exame/AdicionarExame.html'

#    def form_valid(self, form):
#        amostra = Amostra.objects.filter(pk=pk)
#        form.instance.amostra = amostra
#        return super(AdicionarExame, self).form_valid(form)
#
#    def get_success_url(self):
#
#        if 'add' in self.request.POST:
#            url = reverse_lazy('exame:AdicionarExame')
#        else:
#            url = reverse_lazy('amostra:listar')

#        return url

def addExame(request, pk):
    amostra = Amostra.objects.get(pk=pk)
    if request.method == "POST":
        exame_form = RealizacaoExameForm(request.POST)
    else:
        exame_form = RealizacaoExameForm()

    if exame_form.is_valid():
        exame_form.instance.amostra = amostra
        RealizacaoExame = exame_form.save()
        RealizacaoExame.save()
        if 'add' in request.POST:
            return redirect('exame:AdicionarExame', pk)
        else:
            return redirect('amostra:detalhes', pk)
    else:
        print(exame_form.errors)
    return render(request, 'Exame/AdicionarExame.html',
                  {'exame_form': exame_form, 'amostra':amostra})



class CadastrarExame(LoginRequiredMixin, generic.CreateView):
    fields = ('nome',)
    model = Exame
    template_name = 'Exame/CadastrarExame.html'

    def get_success_url(self):

        if 'add' in self.request.POST:
            url = reverse_lazy('exame:CadastrarExame')
        else:
            url = reverse_lazy('exame:ListarExame')
        return url

class DetalheExame(LoginRequiredMixin, generic.DetailView):
    model = Exame
    template_name = "Exame/exame_detail.html"

def DetalheExame(request, pk):
    nome = Exame.objects.filter(pk=pk)
    exames = RealizacaoExame.objects.filter(exame_id=pk)
    resultado = []
    resultadoE = []
    tipo_exame = []
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
    um = 0
    dois = 0
    tres = 0
    quatro = 0
    cinco = 0
    um1 = 0
    dois2 = 0
    tres3 = 0
    quatro4 = 0
    cinco5 = 0
    saudavel = 0
    normal = 0
    doente = 0
    saudavel1 = 0
    normal2 = 0
    doente3 = 0
    especie = None
    teste = None
    for exame in exames:
        if exame.data.month == 1:   jan = jan + 1
        if exame.data.month == 2:   fev = fev + 1
        if exame.data.month == 3:   mar = mar + 1
        if exame.data.month == 4:   abr = abr + 1
        if exame.data.month == 5:   mai = mai + 1
        if exame.data.month == 6:   jun = jun + 1
        if exame.data.month == 7:   jul = jul + 1
        if exame.data.month == 8:   ago = ago + 1
        if exame.data.month == 9:   set = set + 1
        if exame.data.month == 10:  out = out + 1
        if exame.data.month == 11:  nov = nov + 1
        if exame.data.month == 12:  dez = dez + 1
    if request.method == 'POST':
        form = especieForm(request.POST)
        if form.is_valid():
            especie = request.POST['especie_animal']
            for item in nome:
                if item.nome == 'Famacha':
                    tipo_exame = ['1', '2', '3', '4', '5']
                    for exame in exames:
                        if exame.amostra.especie_animal == especie:
                            if exame.resultado == 1:   um = um + 1
                            if exame.resultado == 2:   dois = dois + 1
                            if exame.resultado == 3:   tres = tres + 1
                            if exame.resultado == 4:   quatro = quatro + 1
                            if exame.resultado == 5:   cinco = cinco + 1
                            resultadoE = [um, dois, tres, quatro, cinco]
                    for exame in exames:
                        if exame.resultado == 1:   um1 = um1 + 1
                        if exame.resultado == 2:   dois2 = dois2 + 1
                        if exame.resultado == 3:   tres3 = tres3 + 1
                        if exame.resultado == 4:   quatro4 = quatro4 + 1
                        if exame.resultado == 5:   cinco5 = cinco5 + 1
                        resultado = [um1, dois2, tres3, quatro4, cinco5]
                else:
                    tipo_exame = ['0-50', '51-100', '101-200']
                    for exame in exames:
                        if exame.amostra.especie_animal == especie:
                            if exame.resultado >= 0 and exame.resultado <= 50:   saudavel = saudavel + 1
                            if exame.resultado >= 51 and exame.resultado <= 100:   normal = normal + 1
                            if exame.resultado >= 101 and exame.resultado <= 200:   doente = doente + 1
                            resultadoE = [saudavel, normal, doente]
                    for exame in exames:
                        if exame.resultado >= 0 and exame.resultado <= 50:   saudavel1 = saudavel1 + 1
                        if exame.resultado >= 51 and exame.resultado <= 100:   normal2 = normal2 + 1
                        if exame.resultado >= 101 and exame.resultado <= 200:   doente3 = doente3 + 1
                        resultado = [saudavel1, normal2, doente3]
    else:
        form = especieForm()
    mes = [jan, fev ,mar ,abr, mai, jun, jul, ago, set, out, nov, dez]
    json_resultado = json.dumps(resultado)
    json_resultadoE = json.dumps(resultadoE)
    json_tipo_exame = json.dumps(tipo_exame)
    json_mes = json.dumps(mes)
    context = {'nomes':nome, 'meses':json_mes, 'tipo_exames':json_tipo_exame, 'resultadosE':json_resultadoE,'resultados':json_resultado,'form': form, 'especie':especie}
    return render(request, 'Exame/exame_detail.html', context)


class EditarExame(LoginRequiredMixin, generic.UpdateView):
    model = Exame
    fields = ['nome']
    template_name = 'Exame/exame_update.html'

    def get_success_url(self):
        return(self.request.POST.get('next', '/'))

class DeletarExame(LoginRequiredMixin, generic.DeleteView):
    model = Exame
    template_name = 'Exame/ListarExame.html'

    def get_success_url(self):
        return(self.request.POST.get('next', '/'))

def mudar_status_exame(request, status, exame):
    exame = Exame.objects.get(pk=exame)
    if (status==1):
        exame.status = True
    else:
        exame.status = False
    exame.save()
    return redirect('exame:ListarExame')

@login_required
def examesInativos(request):
    exame_list = Exame.objects.filter(status=False)
    paginator = Paginator(exame_list, 5)

    page = request.GET.get('page')
    exame = paginator.get_page(page)
    context = {'listar_exame':exame}
    return render(request, 'Exame/exames_inativos.html', context)



