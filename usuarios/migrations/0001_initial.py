# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-11 21:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=50)),
                ('identificacion', models.BigIntegerField(primary_key=True, serialize=False)),
                ('telefono', models.BigIntegerField()),
                ('estado', models.BooleanField(default=True)),
                ('correo', models.EmailField(max_length=254)),
                ('area_oficina', models.CharField(max_length=40)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]