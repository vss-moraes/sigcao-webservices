# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-29 01:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doenca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FaixaEtaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(default=django.utils.timezone.now)),
                ('endereco_completo', models.CharField(default='', max_length=200)),
                ('bairro', models.CharField(default='', max_length=50)),
                ('cidade', models.CharField(default='', max_length=10)),
                ('estado', models.CharField(default='MS', max_length=2)),
                ('latitude', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('doenca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webservices.Doenca')),
                ('faixa_etaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webservices.FaixaEtaria')),
            ],
        ),
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Veterinario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=100)),
                ('estado', models.CharField(default='MS', max_length=2)),
                ('tipo_inscricao', models.CharField(default='Primária', max_length=10)),
                ('situacao', models.CharField(default='Atuante', max_length=10)),
                ('crmv', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='ocorrencia',
            name='raca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webservices.Raca'),
        ),
        migrations.AddField(
            model_name='ocorrencia',
            name='sexo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webservices.Sexo'),
        ),
        migrations.AddField(
            model_name='ocorrencia',
            name='veterinario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webservices.Veterinario'),
        ),
    ]
