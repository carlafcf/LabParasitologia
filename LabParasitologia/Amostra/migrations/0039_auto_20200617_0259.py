# Generated by Django 3.0.3 on 2020-06-17 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amostra', '0038_amostra_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amostra',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
