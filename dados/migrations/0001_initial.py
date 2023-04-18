# Generated by Django 4.2 on 2023-04-18 00:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eleicao',
            fields=[
                ('eleicao_n', models.IntegerField(primary_key=True, serialize=False)),
                ('eleicao_nome', models.CharField(max_length=150)),
                ('eleicao_data_inicio', models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 17, 21, 16, 17, 576173))),
                ('eleicao_data_fim', models.DateTimeField()),
                ('eleicao_ativo', models.BooleanField(blank=True, default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dado_Eleicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidato_nome', models.CharField(max_length=150)),
                ('candidato_voto', models.IntegerField(blank=True, default=0)),
                ('eleicao_n', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dados.eleicao')),
            ],
        ),
    ]