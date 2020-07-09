from django.db import models
# from Amostra.models import Amostra
from datetime import datetime, date

TIPOS_RESULTADO = [
    ('NUM', 'Números'),
    ('TEX', 'Valores exatos')
]

class Exame(models.Model):
    nome = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    tipo_resultado = models.CharField(max_length=3, choices=TIPOS_RESULTADO, default='NUM')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)

class RealizacaoExame(models.Model):

    exame = models.ForeignKey(Exame, on_delete=models.CASCADE)
    amostra = models.ForeignKey(to='Amostra.amostra', on_delete=models.CASCADE, null=True)
    resultado_numerico = models.IntegerField(null=True)
    resultado_textual = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.today, null=True, blank=True)
    data = models.DateField(default=date.today)

    def __str__(self):
        return self.exame.nome

class ResultadoExame(models.Model):
    resultado_textual = models.CharField(max_length=200, blank=True, null=True)
    resultado_numerico = models.IntegerField(blank=True, null=True)
    ordem = models.PositiveIntegerField(blank=True, null=True)
    exame = models.ForeignKey(Exame, on_delete=models.CASCADE, related_name='resultados')

    def __str__(self):
        return "{}".format(self.exame.nome)

    class Meta:
        ordering = ['exame']
