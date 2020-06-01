from django.shortcuts import render, redirect
from .forms import RealizacaoExameForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import RealizacaoExame, Exame
from Amostra.models import Amostra

def exameListar(request):
    exame = Exame.objects.all()
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



