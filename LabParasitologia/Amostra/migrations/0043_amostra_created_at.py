# Generated by Django 3.0.3 on 2020-06-17 06:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amostra', '0042_remove_amostra_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='amostra',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
