# Generated by Django 3.0.3 on 2020-06-10 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exame', '0006_auto_20200610_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='realizacaoexame',
            name='created_at',
            field=models.DateTimeField(default=' '),
        ),
    ]
