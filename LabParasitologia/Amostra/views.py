from django.shortcuts import render
from .models import Amostra

def home(request):
	return render(request, 'Amostra/index.html')

def listar(request):
	amostras = Amostra.objects.all()
	context = {'lista_amostras': amostras}
	return render(request, 'Amostra/listar.html', context)
