# Generated by Django 5.1.6 on 2025-03-02 19:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrdenReparacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Reparado', 'Reparado')], max_length=20)),
                ('item', models.CharField(max_length=255)),
                ('problema', models.TextField()),
                ('accesorios', models.TextField()),
                ('fotos', models.ImageField(blank=True, null=True, upload_to='ordenes_fotos/')),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reparaciones.cliente')),
            ],
        ),
    ]
