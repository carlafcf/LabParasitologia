from django import forms
from django.core import validators
from .models import RealizacaoExame
from Amostra.models import Amostra
from datetime import date

class RealizacaoExameForm(forms.ModelForm):
    def clean_data(self):
        data = self.cleaned_data['data']
        if data > date.today():
            raise forms.ValidationError("essa data ainda nao passou!")
        return data
    class Meta():
        model = RealizacaoExame
        fields=('exame','resultado','data')


class especieForm(forms.ModelForm):
    class Meta():
        model = Amostra
        fields=('especie_animal',)