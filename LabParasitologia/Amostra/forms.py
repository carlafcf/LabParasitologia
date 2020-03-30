from django import forms
from django.core import validators
from .models import Amostra

class AmostraForm(forms.ModelForm):
    class Meta():
        model=Amostra
        fields=('identificacao', 'origem', 'local_coleta', 'data_coleta', 'tipo_amostra')