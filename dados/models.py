from django.db import models
from datetime import datetime
# Create your models here.
class Eleicao(models.Model):
    eleicao_n = models.IntegerField(primary_key=True)
    eleicao_nome = models.CharField(max_length=150,blank=False)
    eleicao_data_inicio = models.DateTimeField(default=datetime.now(),blank=True)
    eleicao_data_fim = models.DateTimeField(blank=False)
    eleicao_ativo = models.BooleanField(default=True,blank=True)

class Dado_Eleicao(models.Model):
    eleicao_n = models.ForeignKey("Eleicao", on_delete=models.CASCADE)
    candidato_nome=models.CharField(max_length=150,blank=False)
    candidato_voto= models.IntegerField(default=0,blank=True)