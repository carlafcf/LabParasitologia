# Generated by Django 3.0.3 on 2020-06-07 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amostra', '0033_auto_20200605_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amostra',
            name='localidade',
            field=models.CharField(max_length=200),
        ),
    ]
