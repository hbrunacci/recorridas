# Generated by Django 2.2.4 on 2019-12-05 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('export_date', models.DateTimeField(blank=True, editable=False, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Eventos',
                'verbose_name': 'Evento',
            },
        ),
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('export_date', models.DateTimeField(blank=True, editable=False, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('valor', models.IntegerField()),
                ('evento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='tarifas', to='entradas.Evento')),
            ],
            options={
                'verbose_name_plural': 'Tarifas',
                'verbose_name': 'Tarifa',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('export_date', models.DateTimeField(blank=True, editable=False, null=True)),
                ('evento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='entradas.Evento')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Pedidos',
                'verbose_name': 'Pedido',
            },
        ),
        migrations.CreateModel(
            name='LimiteReserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('export_date', models.DateTimeField(blank=True, editable=False, null=True)),
                ('cantidad', models.IntegerField()),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='limites', to='entradas.Evento')),
                ('tarifa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='limites', to='entradas.Tarifa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='limites', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Limites de Reservas',
                'ordering': ['pk'],
                'verbose_name': 'Limite de Reserva',
            },
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('export_date', models.DateTimeField(blank=True, editable=False, null=True)),
                ('nombre_destinatario', models.CharField(max_length=40)),
                ('dni_destinatario', models.CharField(max_length=10)),
                ('nro_socio_destinatario', models.CharField(blank=True, max_length=8, null=True)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entradas', to='entradas.Evento')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entradas', to='entradas.Pedido')),
                ('tarifa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entradas', to='entradas.Tarifa')),
            ],
            options={
                'verbose_name_plural': 'Entradas',
                'ordering': ['pk'],
                'verbose_name': 'Entrada',
            },
        ),
    ]
