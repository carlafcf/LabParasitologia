from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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

class DetalheAmostra(LoginRequiredMixin, generic.DetailView):
    model = Amostra
