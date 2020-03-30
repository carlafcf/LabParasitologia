from django.shortcuts import render
from .models import Amostra
from .forms import AmostraForm

def home(request):
	return render(request, 'Amostra/index.html')

def listar(request):
	amostras = Amostra.objects.all()
	context = {'lista_amostras': amostras}
	return render(request, 'Amostra/listar.html', context)

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
