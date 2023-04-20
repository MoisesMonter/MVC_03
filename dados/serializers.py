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


class DadoEleicaoSerializerGET(serializers.ModelSerializer):
    class Meta:
        model = Dado_Eleicao
        fields = ['eleicao_n','candidato_nome','candidato_voto']#
        
        def create(self, validated_data):
            return Dado_Eleicao.objects.create(**validated_data)

class DadoEleicaoSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Dado_Eleicao
        fields = ['eleicao_n','candidato_nome']#'eleicao_n',,'candidato_voto'
        
        def create(self, validated_data):
            return Dado_Eleicao.objects.create(**validated_data)
        

class Votar_SerializerGET(serializers.ModelSerializer):
    class Meta:
        model = Dado_Eleicao
        fields =['eleicao_n','candidato_nome']    

        def create(self, validated_data):
            return Dado_Eleicao.objects.create(**validated_data)

class Votar_SerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Dado_Eleicao
        fields =['eleicao_n','candidato_nome','candidato_votar']    

        def create(self, validated_data):
            return Dado_Eleicao.objects.create(**validated_data)