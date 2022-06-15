from django.db import models
from Local.models import Local

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

class Animal(models.Model):
    identificacao = models.CharField(max_length=10)
    origem = models.CharField(max_length=200)
    localidade = models.ForeignKey(Local, on_delete=models.CASCADE, null = True, related_name='local')
    setor = models.CharField(max_length=200)
    especie_animal = models.CharField(max_length=2, choices=ESPECIES_ANIMAIS,default='OU')
    sexo_animal = models.CharField(max_length=1, choices=SEXO, default='I')
    situação = models.BooleanField(default=True)

    def __str__(self):
        return str(self.localidade) + "-" + self.identificacao

    class Meta:
        ordering = ('situacao', 'localidade', 'especie_animal', 'identificacao')