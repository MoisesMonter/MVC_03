# Generated by Django 4.2 on 2023-04-19 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0003_dado_eleicao_eleicao_nome_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dado_eleicao',
            name='eleicao_nome',
        ),
        migrations.AlterField(
            model_name='eleicao',
            name='eleicao_data_inicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 19, 14, 12, 17, 385760)),
        ),
    ]