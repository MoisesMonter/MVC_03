#from django.shortcuts import render
from datetime import datetime
#Usuarios
from django.contrib.auth.models import User
from django.shortcuts import render
from dados.forms import FormularioCadastro
#importar models & Serializers
from dados.models import Eleicao,Dado_Eleicao
from dados.serializers import EleicaoSerializerGET, EleicaoSerializerPOST,DadoEleicaoSerializerGET,DadoEleicaoSerializerPOST,Votar_SerializerGET,Votar_SerializerPOST

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
        serializer = EleicaoSerializerGET(eleicao,many=True)
        print(eleicao)
        return Response(serializer.data)        
    if request.method == 'POST':
        serializer = EleicaoSerializerPOST(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.db.models import Max

@api_view(['GET','POST'])
def Eleicao_Dado(request):
    if request.method =='GET':
        dados = Dado_Eleicao.objects.all()
        serializer = DadoEleicaoSerializerGET(dados,many=True)
        return Response(serializer.data)        
    if request.method == 'POST':
        serializer =DadoEleicaoSerializerPOST(data=request.data)
        if serializer.is_valid():
            serializer.save()
            validar_ativo = Eleicao.objects.get(eleicao_n= serializer.data['eleicao_n'])
            print(validar_ativo.eleicao_ativo)
            data2 = Dado_Eleicao.objects.filter(eleicao_n = validar_ativo.eleicao_n)
            print(len(data2))
            if len(data2) >1:
                validar_ativo.eleicao_ativo = True
                print(validar_ativo.eleicao_ativo)
                validar_ativo.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])  
def Votar_Eleicao(request):
    if request.method == 'GET':
        dados = Dado_Eleicao.objects.all()
        serializer = Votar_SerializerGET(dados,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer =  Votar_SerializerGET(data=request.data)
        if serializer.is_valid():
            print(serializer.data['eleicao_n'])
            validar_data = Eleicao.objects.get(eleicao_n= serializer.data['eleicao_n'])
            print(validar_data.eleicao_data_fim)
            data_final =datetime.fromisoformat(str(validar_data.eleicao_data_fim)[:10])
            if datetime.now() > data_final:
                if serializer.data['eleicao_ativo'] == True:
                    print('is true')
                    obj = Dado_Eleicao.objects.get(eleicao_n=serializer.data['eleicao_n'],candidato_nome =serializer.data['candidato_nome'])
                    obj.candidato_voto+=1
                    obj.save()
                else:
                    print("eielição nao está ativo")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''def Eleicao_Site(request):
    if request.method == 'GET':
         return render(request,'index.html')


def CriarEleicao(request):
    if request.method == 'GET':
        form = FormularioCadastro()
        print(form)
        return render(request,'criar.html',context={"form":form})
    else:
        form = FormularioCadastro(request.POST)
        if form.is_valid():
            print(form)'''