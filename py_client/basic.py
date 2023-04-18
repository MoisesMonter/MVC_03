import requests
from datetime import date
'''endpoint = "https://httpbin.org/status/200/"'''
endpoint = "http://127.0.0.1:8000/api/"

#get_response = requests.get(endpoint) #http obtem solicitação da API  tipo get get

#print(get_response.text)  #vai imprimir o codigo fonte que será imprimido

#HTTP Request -> HTML

#REST API HTTP Request -> JSON

#Javascript Object Notion ~ python Dict
#print(get_response.text)
#print(get_response.status_code)
eleicao_nome = "Api de testes"
date_select = str(date(2023,4,19))
get_response = requests.get(endpoint, params={"abc":123}, data={"eleicao_nome":eleicao_nome,"date_select":date_select},)
#print( get_response.json()) 