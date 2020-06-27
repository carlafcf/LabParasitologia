from django import forms
from django.core import validators
from django.forms import formset_factory
from .models import RealizacaoExame, ResultadoExame
from Amostra.models import Amostra

class RealizacaoExameForm(forms.ModelForm):
    class Meta():
        model = RealizacaoExame
        fields=('exame','resultado','data')

class especieForm(forms.ModelForm):
    class Meta():
        model = Amostra
        fields=('especie_animal',)

# class ResultadoFormTextual(forms.ModelForm):
#     class Meta():
#         model = ResultadoExame
#         fields=('resultado_textual',)

class ResultadoFormTextual(forms.Form):
    valor = forms.CharField(
        label='Valor do resultado',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Possível resultado'
        })
    )

class ResultadoFormNumerico(forms.Form):
    valor = forms.IntegerField(
        label='Valor do resultado',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Possível resultado'
        })
    )

ResultadoTextualFormset = formset_factory(ResultadoFormTextual, extra=1)
ResultadoNumericoFormset = formset_factory(ResultadoFormNumerico, extra=1)

# class ResultadoFormNumerico(forms.ModelForm):
#     class Meta():
#         model = ResultadoExame
#         fields=('resultado_numerico',)