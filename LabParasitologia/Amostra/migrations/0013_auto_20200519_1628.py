# Generated by Django 3.0.3 on 2020-05-19 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amostra', '0012_amostra_responsavel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amostra',
            name='responsavel',
            field=models.CharField(default='aaaaaaaaa', max_length=200),
        ),
    ]
