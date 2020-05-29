from django import forms
from django.core import validators
from .models import RealizacaoExame

class AmostraForm(forms.ModelForm):
    class Meta():
        model = RealizacaoExame
        fields=('exame','amostra', 'resultado')