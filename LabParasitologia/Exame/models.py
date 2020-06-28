from django.db import models
#from Amostra.models import Amostra
from datetime import datetime, date


class Exame(models.Model):
    nome = models.CharField(max_length=200)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)

class RealizacaoExame(models.Model):
    exame = models.ForeignKey(Exame, on_delete=models.CASCADE)
    amostra = models.ForeignKey(to='Amostra.amostra', on_delete=models.CASCADE, null=True)
    resultado = models.BigIntegerField(null=True)
    created_at = models.DateField(default=date.today, null=True, blank=True)
    data = models.DateField(default=date.today)

