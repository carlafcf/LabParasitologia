# Generated by Django 3.0.3 on 2020-05-28 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exame', '0001_initial'),
        ('Amostra', '0025_amostra_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='amostra',
            name='exame',
            field=models.ManyToManyField(to='Exame.Exame'),
        ),
    ]
