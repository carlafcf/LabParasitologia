from django import forms
from django.core import validators
from .models import RealizacaoExame

class RealizacaoExameForm(forms.ModelForm):
    class Meta():
        model = RealizacaoExame
        fields=('exame','amostra','resultado')