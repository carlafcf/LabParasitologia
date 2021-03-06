# Generated by Django 3.0.3 on 2020-06-13 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amostra', '0036_auto_20200613_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amostra',
            name='especie_animal',
            field=models.CharField(choices=[('AV', 'Aves'), ('BO', 'Bovino'), ('CA', 'Camarão'), ('CN', 'Canino'), ('CP', 'Caprino'), ('EQ', 'Equino'), ('FE', 'Felino'), ('PE', 'Peixe'), ('OV', 'Ovino'), ('SU', 'Suíno'), ('OU', 'Outro')], default='OU', max_length=2),
        ),
    ]
