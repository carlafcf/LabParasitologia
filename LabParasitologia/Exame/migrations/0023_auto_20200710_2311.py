# Generated by Django 3.0.3 on 2020-07-11 02:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exame', '0022_auto_20200710_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realizacaoexame',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.today, null=True),
        ),
    ]
