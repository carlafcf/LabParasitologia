# Generated by Django 3.0.3 on 2020-06-17 05:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amostra', '0037_auto_20200613_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='amostra',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.today, null=True),
        ),
    ]
