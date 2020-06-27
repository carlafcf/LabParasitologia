from django import forms
from django.core import validators
from .models import Amostra
from datetime import date

class AmostraForm(forms.ModelForm):
    class Meta():
        model = Amostra
        fields=('identificacao', 'origem', 'setor', 'data_coleta', 'tipo_amostra')

class amostraForm(forms.ModelForm):
    def clean_data_coleta(self):
        data_coleta = self.cleaned_data['data_coleta']
        if data_coleta > date.today():
            raise forms.ValidationError("essa data ainda nao passou!")
        return data_coleta
    class Meta():
        model = Amostra
        fields=('data_coleta', 'origem', 'localidade','setor','especie_animal', 'identificacao', 'tipo_amostra','sexo_animal')