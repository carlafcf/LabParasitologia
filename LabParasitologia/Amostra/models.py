from django.db import models
from datetime import date

class Amostra(models.Model):
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


    #ESPECIES_ANIMAIS = [
    #    ('AV', 'Aves'),
    #    ('BO', 'Bovino'),
    #    ('CA', 'Camarão'),
    #    ('CN', 'Canino'),
    #    ('CP', 'Caprino'),
    #    ('EQ', 'Equino'),
    #    ('FE', 'Felino'),
    #    ('PE', 'Peixe'),
    #    ('OV', 'Ovino'),
    #    ('SU', 'Suíno'),
    #    ('OU', 'Outro'),
    #]

    #SEXO = [
    #    ('F', 'Feminino'),
    #    ('M', 'Masculino'),
    #    ('I', 'Indeterminado'),
    #]

	identificacao = models.CharField(max_length=10)
	origem = models.CharField(max_length=200)
	#responsavel = models.ForeignKey()
	#codigo_local nao entendi!
	local_coleta = models.CharField(max_length=200)
	data_coleta = models.DateField(default=date.today)
	tipo_amostra = models.CharField(max_length=2, choices=TIPOS_AMOSTRA,default='OU')
	#especie_animal = models.CharField(max_length=2, choices=ESPECIES_ANIMAIS,default='OU')
	#sexo_animal = models.CharField(max_length=1, choices=SEXO,default='I')
	#teste = models.MultipleChoiceField

	def __str__(self):
		return self.identificacao

	class Meta:
		ordering = ['-data_coleta']


