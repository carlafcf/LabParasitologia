# Generated by Django 3.0.3 on 2020-05-12 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amostra', '0002_auto_20200511_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='amostra',
            name='sexo_animal',
            field=models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('I', 'Indeterminado')], default='I', max_length=1),
        ),
    ]
