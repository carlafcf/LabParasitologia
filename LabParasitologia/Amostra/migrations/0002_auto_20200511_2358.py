# Generated by Django 3.0.3 on 2020-05-11 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Amostra', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amostra',
            options={'ordering': ['-data_coleta']},
        ),
    ]
