from django.shortcuts import render
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
	amostras = Amostra.objects.all()
	context = {'lista_amostras': amostras}
	return render(request, 'Amostra/listar.html', context)

@login_required
def listarAmostraUser(request, pk):
	amostras = Amostra.objects.filter(responsavel_id=pk)
	context = {'lista_amostrasUser': amostras}
	return render(request, 'Amostra/listarAmostraUser.html', context)

def listarAmostraFinalizada(request, pk):
	amostras = Amostra.objects.filter(responsavel_id=pk, is_active = True)
	context = {'lista_amostrasUserFinalizada': amostras}
	return render(request, 'Amostra/listarAmostraUserFinalizada.html', context)


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
        amostra.is_active = True
    else:
        amostra.is_active = False
    amostra.save()
    return redirect('amostra:listar')

class CriarAmostra(LoginRequiredMixin, generic.CreateView):
    fields = ('identificacao', 'origem', 'local_coleta', 'data_coleta', 'tipo_amostra','sexo_animal','especie_animal')
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
    fields = ['identificacao', 'origem', 'local_coleta', 'data_coleta', 'tipo_amostra','sexo_animal','especie_animal']
    template_name = 'Amostra/amostra_update_form.html'
    success_url = reverse_lazy('amostra:listar')

class DeletarAmostra(LoginRequiredMixin, generic.DeleteView):
    model = Amostra
    template_name = 'Amostra/listar.html'
    success_url = reverse_lazy('amostra:listar')

