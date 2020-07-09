from django import forms
from django.core import validators
from django.forms import formset_factory
from .models import RealizacaoExame, ResultadoExame
from Amostra.models import Amostra
from datetime import date

class RealizacaoExameForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.tipo = kwargs.pop('tipo')
        self.exame = kwargs.pop('exame')
        super().__init__(*args, **kwargs)
        if self.tipo == 'NUM':
            del self.fields['resultado_textual']
        else:
            del self.fields['resultado_numerico']
            self.fields['resultado_textual'] = forms.ChoiceField(
                choices=[(str(o.resultado_textual), str(o.resultado_textual)) for o in ResultadoExame.objects.filter(exame=self.exame)]
            )

    def clean_data(self):
        data = self.cleaned_data['data']
        if data > date.today():
            raise forms.ValidationError("Não é possível cadastrar exames para datas futuras.")
        return data

    class Meta():
        model = RealizacaoExame
        fields = ('resultado_numerico', 'resultado_textual', 'data')


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