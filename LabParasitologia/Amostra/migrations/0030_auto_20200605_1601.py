# Generated by Django 3.0.3 on 2020-06-05 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amostra', '0029_auto_20200605_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amostra',
            name='localidade',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]