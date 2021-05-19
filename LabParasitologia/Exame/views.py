from django.shortcuts import render, redirect

from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime, date, timedelta

from django.contrib import messages

import json

from .forms import especieForm
from .forms import ExameForm, RealizacaoExameForm, ResultadoFormNumerico, ResultadoFormTextual
from .forms import ResultadoTextualFormset, ResultadoNumericoFormset

from .models import Exame, ResultadoExame
from Amostra.models import Amostra, RealizacaoExame

def exameListar(request):
    exame_list = Exame.objects.filter(status=True)
    paginator = Paginator(exame_list, 5)

    page = request.GET.get('page')
    exame = paginator.get_page(page)
    context = {'listar_exame':exame}
    return render(request, 'Exame/ListarExame.html', context)

def exame_amostraDetalhes(request, pk):
    amostra = Amostra.objects.filter(pk=pk)[0]
    resultados_exames = RealizacaoExame.objects.filter(amostra_id=pk)
    exames_cadastrados = Exame.objects.all()

    quinze = date.today() - timedelta(days=15)
    dez = date.today() - timedelta(days=10)

    if amostra.data_coleta <= quinze:
        alerta = "#e74a3b"
    elif amostra.data_coleta <= dez:
        alerta = "#f6c23e"
    else:
        alerta = None

    context = {
        'amostra':amostra,
        'lista_exames': resultados_exames,
        'exames_cadastrados': exames_cadastrados,
        'alerta': alerta
    }
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
        exame_form = RealizacaoExameForm(tipo="NUM")

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

def novoAddExame(request, pk, exame):
    amostra = Amostra.objects.get(pk=pk)
    exame_cadastrar = Exame.objects.get(pk=exame)
    tipo = exame_cadastrar.tipo_resultado
    possiveis_resultados = ResultadoExame.objects.filter(exame=exame)

    if request.method == "POST":
        exame_form = RealizacaoExameForm(request.POST, tipo=tipo, exame=exame)
    else:
        exame_form = RealizacaoExameForm(tipo=tipo, exame=exame)

    if exame_form.is_valid():
        exame_form.instance.amostra = amostra
        exame_form.instance.exame = exame_cadastrar
        RealizacaoExame = exame_form.save()
        RealizacaoExame.save()
        if 'add' in request.POST:
            return redirect('exame:AdicionarExame', pk)
        else:
            return redirect('amostra:detalhes', pk)
    return render(request, 'Exame/AdicionarExame.html',
                  {'form': exame_form, 'amostra':amostra, 'tipo': tipo, 'exame': exame_cadastrar})


class CadastrarExame(LoginRequiredMixin, generic.CreateView):
    fields = ('nome','tipo_resultado')
    model = Exame
    template_name = 'Exame/CadastrarExame.html'

    def get_success_url(self):
        if 'add' in self.request.POST:
            url = reverse_lazy('exame:CadastrarExame')
        else:
            url = reverse_lazy('exame:definir_resultados', kwargs={'pk': self.object.id})
        return url

def cadastrar_exame(request):
    if request.method == "POST":
        exame_form = ExameForm(request.POST)
        if exame_form.is_valid():
            nome = exame_form.cleaned_data['nome']
            tipo_resultado = exame_form.cleaned_data['tipo_resultado']
            return redirect('exame:resultados', nome, tipo_resultado)
        else:
            print(exame_form.errors)
    else:
        exame_form = ExameForm()
    
    
    return render(request, 'Exame/CadastrarExame.html',
                  {'form': exame_form})

def definir_saidas(request, nome, tipo_resultado):
    template_name = 'Exame/DefinirResultados.html'
    i=0
    if tipo_resultado == "NUM":
        if request.method == 'GET':
            formset = ResultadoNumericoFormset(request.GET or None)
        elif request.method == 'POST':
            formset = ResultadoNumericoFormset(request.POST)
            if formset.is_valid():
                exame = Exame(nome=nome, tipo_resultado=tipo_resultado)
                exame.save()
                for count, form in enumerate(formset, start=1):
                    valor = form.cleaned_data.get('valor')
                    if valor:
                        ResultadoExame(resultado_numerico=valor, exame=exame, ordem=i).save()
                        i=i+1
                return redirect('exame:ListarExame')
        return render(request, template_name, {
            'formset': formset, 'tipo': 'NUM',
        })
    else:
        if request.method == 'GET':
            formset = ResultadoTextualFormset(request.GET or None)
        elif request.method == 'POST':
            formset = ResultadoTextualFormset(request.POST)
            if formset.is_valid():
                # is_empty = False
                # for form in formset:
                #     if not form.cleaned_data.get('valor'):
                #         is_empty = True
                #         messages.error(request, 'Document deleted.')
                # if not is_empty:
                    exame = Exame(nome=nome, tipo_resultado=tipo_resultado)
                    exame.save()
                    for count, form in enumerate(formset, start=1):
                        valor = form.cleaned_data.get('valor')
                        if valor:
                            ResultadoExame(resultado_textual=valor, exame=exame, ordem=count).save()
                    return redirect('exame:ListarExame')    
        return render(request, template_name, {'formset': formset, 'tipo': 'TEX',})    

def definir_resultados(request,pk):
    template_name = 'Exame/DefinirResultados.html'
    exame = Exame.objects.get(pk=pk)
    i=0
    if exame.tipo_resultado == "NUM":
        if request.method == 'GET':
            formset = ResultadoNumericoFormset(request.GET or None)
        elif request.method == 'POST':
            print("post")
            formset = ResultadoNumericoFormset(request.POST)
            if formset.is_valid():
                print("valid")
                for count, form in enumerate(formset, start=1):
                    valor = form.cleaned_data.get('valor')
                    if valor:
                        ResultadoExame(resultado_numerico=valor, exame=exame, ordem=i).save()
                        i=i+1
                return redirect('exame:ListarExame')
        print("not valid")
        return render(request, template_name, {
            'formset': formset, 'tipo': 'NUM',
        })
    else:
        if request.method == 'GET':
            formset = ResultadoTextualFormset(request.GET or None)
        elif request.method == 'POST':
            formset = ResultadoTextualFormset(request.POST)
            if formset.is_valid():
                for count, form in enumerate(formset, start=1):
                    valor = form.cleaned_data.get('valor')
                    if valor:
                        ResultadoExame(resultado_textual=valor, exame=exame, ordem=count).save()
                return redirect('exame:ListarExame')
        return render(request, template_name, {
            'formset': formset, 'tipo': 'TEX',
        })

class DetalheExame(LoginRequiredMixin, generic.DetailView):
    model = Exame
    template_name = "Exame/exame_detail.html"

def monthdelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m: m = 12
    d = min(date.day, [31,
        29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
    return date.replace(day=d,month=m, year=y)

def encontrarCategoria(resultado, categorias, tipo):
    if tipo == 'NUM':
        for i in range(len(categorias)):
            if i == 0 and resultado <= categorias[i]:
                return i
            elif i == (len(categorias)-1) and resultado > categorias[i]:
                return i+1
            elif i != (len(categorias)-1) and resultado > categorias[i] and resultado <= categorias[i+1]:
                return i+1
    else:
        try:
            return categorias.index(resultado)
        except ValueError:
            return -1

def NovoDetalheExame(request, pk):
    nome = Exame.objects.filter(pk=pk)
    tipo = nome[0].tipo_resultado
    categorias = []
    for cat in nome[0].resultados.all():
        if tipo == 'NUM':
            categorias.append(cat.resultado_numerico)
        else:
            categorias.append(cat.resultado_textual)
    valores = [0,0,0,0,0]
    exames = RealizacaoExame.objects.filter(exame_id=pk)

    print("Categorias")
    print(categorias)

    # Total de exames por mes nos últimos 12 meses
    months = []
    total = []
    for m in range(-11, 1):
        months.append(str(monthdelta(datetime.now(), m).month)+"/"+str(monthdelta(datetime.now(), m).year))
        total.append(0)
    for exame in exames:
        data = str(exame.data.month)+"/"+str(exame.data.year)
        try:
            index = months.index(data)
        except ValueError:
            index = -1
        if index>=0:
            total[index]=total[index]+1

    # Resultado dos exames em range por especie nos ultimos 12 meses
    resultado = []
    resultado_total = []
    categorias_exibir = []
    # Definir como exibir os ranges de resultados
    if tipo=='NUM':
        exames = exames.order_by('resultado_numerico')
        categorias_exibir.append("resultado <= " + str(categorias[0]))
        for i in range(len(categorias)):
            if i!=(len(categorias)-1):
                categorias_exibir.append(str(categorias[i]) + " < resultado <= " + str(categorias[i+1]))
            resultado.append(0)
            resultado_total.append(0)
        categorias_exibir.append("resultado > " + str(categorias[len(categorias)-1]))
        resultado.append(0)
        resultado_total.append(0)
    else:
        exames = exames.order_by('resultado_textual')
        categorias_exibir = categorias
        for i in range(len(categorias)):
            resultado.append(0)
            resultado_total.append(0)

    # O que exibir: POST (por especie) ou então todos
    if request.method == 'POST':
        form = especieForm(request.POST)
        if form.is_valid():
            especie = request.POST['especie_animal']
            for exame in exames:
                data = str(exame.data.month) + "/" + str(exame.data.year)
                try:
                    index_mes = months.index(data)
                    if tipo == 'NUM':
                        index_tipo = encontrarCategoria(exame.resultado_numerico, categorias, tipo)
                    else:
                        index_tipo = encontrarCategoria(exame.resultado_textual, categorias, tipo)
                    # try:
                    #     index_tipo = categorias.index(exame.resultado)
                    # except ValueError:
                    #     index_tipo = -1
                except ValueError:
                    index_mes = -1
                if index_mes >= 0:
                    resultado_total[index_tipo] = resultado_total[index_tipo] + 1
                    if exame.amostra.especie_animal == especie:
                        resultado[index_tipo] = resultado[index_tipo] + 1
    else:
        form = especieForm()
        for exame in exames:
            data = str(exame.data.month) + "/" + str(exame.data.year)
            try:
                index_mes = months.index(data)
                if tipo=='NUM':
                    index_tipo = encontrarCategoria(exame.resultado_numerico, categorias, tipo)
                else:
                    index_tipo = encontrarCategoria(exame.resultado_textual, categorias, tipo)
                # try:
                #     index_tipo = categorias.index(exame.resultado)
                # except ValueError:
                #     index_tipo = -1
            except ValueError:
                index_mes = -1
            if index_mes >= 0:
                resultado_total[index_tipo] = resultado_total[index_tipo] + 1


    json_resultado_especie = json.dumps(resultado)
    json_resultado_total = json.dumps(resultado_total)
    json_tipo_exame = json.dumps(categorias_exibir)
    json_mes = json.dumps(total)
    json_labels = json.dumps(months)
    context = {'nomes': nome, 'meses': json_mes, 'form':form, 'labels': json_labels, 'resultado': json_resultado_especie,
               'categorias': json_tipo_exame, 'resultado_total': json_resultado_total}
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

@login_required
def cadastrar_multiplos_resultados(request, fase, pk):
    exame = Exame.objects.filter(pk=pk)[0]
    if request.method == 'POST':
        if fase==0:
            id_amostras_selecionadas = request.POST.getlist('amostras')
            amostras_selecionadas = []
            for amostra_id in id_amostras_selecionadas:
                amostras_selecionadas.append(Amostra.objects.filter(id=int(amostra_id))[0])
            resultados_exame = ResultadoExame.objects.filter(exame=exame)
            return render(request, 'Exame/cadastrar_multiplos_resultados.html', 
                {'amostras_selecionadas': amostras_selecionadas, 'exame': exame, 
                'resultados_exame': resultados_exame, 'data_atual': date.today()})
        else:
            resultados_numericos = request.POST.getlist('resultados_num')
            resultados_textuais = request.POST.getlist('resultados_tex')
            id_amostras = request.POST.getlist('id_amostra')
            for index, id_amostra in enumerate(id_amostras):
                amostra = Amostra.objects.filter(id=id_amostra)[0]
                if (exame.tipo_resultado=="NUM"):
                    realizacao_exame = RealizacaoExame(exame=exame, amostra=amostra,
                                                        resultado_numerico=int(resultados_numericos[index]),
                                                        data=request.POST.get('date'))
                    realizacao_exame.save()
                else:
                    realizacao_exame = RealizacaoExame(exame=exame, amostra=amostra,
                                                        resultado_textual=resultados_textuais[index],
                                                        data=request.POST.get('date'))
                    realizacao_exame.save()
            return redirect('amostra:listar')
    else:
        if fase==0:
            quinze = date.today() - timedelta(days=15)
            dez = date.today() - timedelta(days=10)
            lista_amostras = Amostra.objects.filter(status=True).order_by('data_coleta')
            return render(request, 'Exame/selecionar_amostras.html', 
                        {'lista_amostras': lista_amostras, 'exame': exame,
                        'quinze':quinze,'dez':dez})
        else:
            pass






