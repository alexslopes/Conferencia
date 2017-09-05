# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apresentadores',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
                ('filiacao', models.CharField(max_length=20)),
                ('resume', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('abstract', models.TextField()),
                ('data_hora_inicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_hora_fim', models.DateTimeField(default=django.utils.timezone.now)),
                ('apresentadores', models.ForeignKey(to='palestra.Apresentadores')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
                ('local', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('acronimos', models.CharField(max_length=5)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('acronimos', models.CharField(max_length=5)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='atividade',
            name='sala',
            field=models.ForeignKey(to='palestra.Sala'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='tags',
            field=models.ForeignKey(to='palestra.Tags'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='tipo',
            field=models.ForeignKey(to='palestra.Type'),
        ),
    ]
