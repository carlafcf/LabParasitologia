from django.db import models
#from Amostra.models import Amostra


class Exame(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class RealizacaoExame(models.Model):
    exame = models.ForeignKey(Exame, on_delete=models.CASCADE)
    amostra = models.ForeignKey(to='Amostra.amostra', on_delete=models.CASCADE, null=True)
    resultado = models.CharField(max_length=200)

    def __str__(self):
        return self.exame