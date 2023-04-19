from .models import *
from rest_framework import serializers


class EleicaoSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Eleicao
        fields = ['eleicao_nome','eleicao_data_fim']#,'eleicao_ativo','eleicao_data_inicio'
    def create(self, validated_data):
                return Eleicao.objects.create(**validated_data)

class EleicaoSerializerGET(serializers.ModelSerializer):
    class Meta:
        model = Eleicao
        fields = ['eleicao_n','eleicao_nome','eleicao_data_inicio','eleicao_data_fim','eleicao_ativo',]
    def create(self, validated_data):
                return Eleicao.objects.create(**validated_data)


class DadoEleicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dado_Eleicao
        fields = ['eleicao_nome','candidato_nome']#'eleicao_n',,'candidato_voto'