#from django.shortcuts import render
#Usuarios
from django.contrib.auth.models import User

#importar models & Serializers
from dados.models import Eleicao,Dado_Eleicao
from dados.serializers import EleicaoSerializer,DadoEleicaoSerializer

#importar converção Json
import json
from django.http import JsonResponse

# importar bibliotecas rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import authentication, permissions

#viewser para class
from rest_framework import viewsets
# Create your views here.

def api_home(request, *args,**kwargs):
    #body = request.body #JSON Data
    body = request
    data = {}
    try:
        data =json.load(body) #dados json transformado em dicionário python
    except:
        pass#data =json.loads(body)
    print(data)
    print(body)
    return JsonResponse({"mensagem":"Hi there, this is Django API response}"})



'''class ListYsers(APIView):
    authentication_classes =[authentication.tokenAuthentication]
    permission_classes =[permissions.IsAdminUser]
    def get(self,request,format=None):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)'''

#
@api_view(['GET','POST'])
def Eleicao_Lista(request):
    if request.method =='GET':
        eleicao = Eleicao.objects.all()
        serializer = EleicaoSerializer(eleicao,many=True)
        print(eleicao)
        return Response(serializer.data)        

    if request.method == 'POST':
        gerar_eleicao = EleicaoSerializer(data=request.data)
        print(gerar_eleicao)
        if gerar_eleicao.isvalid():
            ge = gerar_eleicao.save()
            return Response(gerar_eleicao.data,status=status.HTTP_201_CREATED)       
        Response(gerar_eleicao.errors)
    

@api_view(['GET','POST'])
def Eleicao_Dado(request):
    if request.method =='GET':
        dados = Dado_Eleicao.objects.all()
        serializer = DadoEleicaoSerializer(dados,many=True)
        return Response(serializer.data)        
    if request.method == 'POST':
        dado_eleicao =DadoEleicaoSerializer(data=request.data)
        lista_buscar_pk = Eleicao.objects.get(eleicao_nome= dado_eleicao.eleicao_nome)
        print(lista_buscar_pk)
        dado_eleicao.eleicao_n_id = lista_buscar_pk.eleicao_n
        print(dado_eleicao)
        if dado_eleicao.isvalid():
            dado_eleicao.save()
            return Response(dado_eleicao.data,status=status.HTTP_201_CREATED)       
        return Response(dado_eleicao.errors, status=status.HTTP_400_BAD_REQUEST)