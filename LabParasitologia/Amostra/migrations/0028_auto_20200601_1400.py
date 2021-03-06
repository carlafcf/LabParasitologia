# Generated by Django 3.0.3 on 2020-06-01 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Amostra', '0027_auto_20200601_1347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amostra',
            options={'ordering': ['-data_coleta', 'origem', 'localidade', 'setor', 'especie_animal', 'identificacao', 'tipo_amostra']},
        ),
        migrations.RenameField(
            model_name='amostra',
            old_name='local_coleta',
            new_name='setor',
        ),
    ]
