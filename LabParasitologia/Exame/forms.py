from django import forms
from django.core import validators
from .models import RealizacaoExame
from Amostra.models import Amostra

class RealizacaoExameForm(forms.ModelForm):
    class Meta():
        model = RealizacaoExame
        fields=('exame','resultado','data')

class especieForm(forms.ModelForm):
    class Meta():
        model = Amostra
        fields=('especie_animal',)