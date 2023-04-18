#from django.shortcuts import render
import json
from django.http import JsonResponse
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