# Generated by Django 3.0.3 on 2020-06-05 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Local', '0001_initial'),
        ('Amostra', '0030_auto_20200605_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amostra',
            name='localidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='local', to='Local.Local'),
        ),
    ]
