# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 13:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doenca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=30)),
                ('rua', models.CharField(max_length=100)),
                ('numero', models.IntegerField(default=0)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=10)),
                ('estado', models.CharField(default='MS', max_length=2)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faixa_etaria', models.CharField(max_length=15)),
                ('sexo', models.CharField(max_length=1)),
                ('data', models.DateTimeField(verbose_name='data da ocorrência')),
                ('doenca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webservices.Doenca')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webservices.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='ocorrencia',
            name='raca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webservices.Raca'),
        ),
    ]
