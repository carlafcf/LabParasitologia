# Generated by Django 3.0.3 on 2020-07-11 02:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exame', '0023_auto_20200710_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realizacaoexame',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
