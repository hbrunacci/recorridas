# Generated by Django 2.2.4 on 2020-03-17 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entradas', '0003_auto_20200317_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='monto_total',
            field=models.FloatField(default=0, verbose_name='Monto Total'),
        ),
    ]
