from django.shortcuts import render
from .forms import RealizacaoExameForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import RealizacaoExame, Exame
from Amostra.models import Amostra


def exameListar(request, pk):
    amostra = Amostra.objects.filter(pk=pk)
    exame = RealizacaoExame.objects.filter(amostra_id=pk)
    context = {'a':amostra, 'lista_exame':exame}
    return render(request, 'Amostra/amostra_detail.html', context)


class AdicionarExame(LoginRequiredMixin, generic.CreateView):
    fields = ('exame','amostra','resultado')
    model = RealizacaoExame
    template_name = 'Exame/AdicionarExame.html'

    #def form_valid(self, form):
    #    amostra = Amostra.objects.filter(pk=pk)
    #    form.instance.amostra = amostra
    #    return super(AdicionarExame, self).form_valid(form)

    def get_success_url(self):

        if 'add' in self.request.POST:
            url = reverse_lazy('exame:AdicionarExame')
        else:
            url = reverse_lazy('amostra:listar')

        return url

#def addExame(request, pk):
#    amostra = Amostra.objects.get(pk=pk)
#    url = reverse_lazy('amostra:listar')
#    if request.method == "POST":
#        exame_form = RealizacaoExameForm(request.POST)
#    else:
#        exame_form = RealizacaoExameForm()

#    if exame_form.is_valid():
#        amostra.exame = exame_form.save()
#        amostra.exame.save()
#        return url

#    else:
#        print(exame_form.errors)
#    return render(request, 'Exame/AdicionarExame.html',
#                  {'exame_form': exame_form})



class CadastrarExame(LoginRequiredMixin, generic.CreateView):
    fields = ('nome',)
    model = Exame
    template_name = 'Exame/CadastrarExame.html'

    def get_success_url(self):

        if 'add' in self.request.POST:
            url = reverse_lazy('exame:CadastrarExame')
        else:
            url = reverse_lazy('amostra:listar')
        return url