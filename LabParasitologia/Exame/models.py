from django.db import models
from datetime import datetime, date
from django.utils import timezone

TIPOS_RESULTADO = [
    ('NUM', 'Numérico'),
    ('TEX', 'Valores exatos')
]

class Exame(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    status = models.BooleanField(default=True)
    tipo_resultado = models.CharField(max_length=3, choices=TIPOS_RESULTADO, default='NUM', null=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)



class ResultadoExame(models.Model):
    resultado_textual = models.CharField(max_length=200, blank=True, null=True)
    resultado_numerico = models.IntegerField(blank=True, null=True)
    ordem = models.PositiveIntegerField(blank=True, null=True)
    exame = models.ForeignKey(Exame, on_delete=models.CASCADE, related_name='resultados')

    def __str__(self):
        return "{}".format(self.exame.nome)

    class Meta:
        ordering = ['exame']
