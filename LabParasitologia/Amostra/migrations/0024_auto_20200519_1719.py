# Generated by Django 3.0.3 on 2020-05-19 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0001_initial'),
        ('Amostra', '0023_auto_20200519_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amostra',
            name='responsavel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='amostras', to='Usuario.User'),
        ),
    ]
