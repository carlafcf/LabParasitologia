from django.db import models
from datetime import date
from Usuario.models import User
from Exame.models import Exame
from Local.models import Local
from datetime import datetime, date

TIPOS_AMOSTRA = [
        ('SA', 'Sangue'),
        ('FE', 'Fezes'),
        ('FA', 'Resultado do FAMACHA'),
        ('CA', 'Carrapato'),
        ('MO', 'Mosca'),
        ('PU', 'Pulga'),
        ('PI', 'Piolho'),
        ('OU', 'Outro'),
    ]

SEXO = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('I', 'Indeterminado'),
    ]

ESPECIES_ANIMAIS = [
        ('AV', 'Aves'),
        ('BO', 'Bovino'),
        ('CA', 'Camarão'),
        ('CN', 'Canino'),
        ('CP', 'Caprino'),
        ('EQ', 'Equino'),
        ('FE', 'Felino'),
        ('PE', 'Peixe'),
        ('OV', 'Ovino'),
        ('SU', 'Suíno'),
        ('OU', 'Outro'),
    ]

class Amostra(models.Model):
    identificacao = models.CharField(max_length=10)
    origem = models.CharField(max_length=200)
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE, null = True, related_name='amostras')
    localidade = models.ForeignKey(Local, on_delete=models.CASCADE, null = True, related_name='local')
    setor = models.CharField(max_length=200)
    data_coleta = models.DateField(default=date.today)
    tipo_amostra = models.CharField(max_length=2, choices=TIPOS_AMOSTRA, default='OU')
    especie_animal = models.CharField(max_length=2, choices=ESPECIES_ANIMAIS,default='OU')
    sexo_animal = models.CharField(max_length=1, choices=SEXO, default='I')
    status = models.BooleanField(default=True)
    exame = models.ManyToManyField(Exame)
    created_at = models.DateField(default=date.today, null=True, blank=True)

    def __str__(self):
        return self.identificacao

    class Meta:
        ordering = ['-data_coleta','origem','localidade','setor','especie_animal','identificacao','tipo_amostra']



