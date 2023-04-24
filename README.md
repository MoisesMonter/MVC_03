
# Título do Projeto

Uma breve descrição sobre o que esse projeto faz e para quem ele é


## Referência

 - [Video Aula](https://www.youtube.com/watch?v=c708Nf0cHrs&t=2553s)
 - [Django_Restframework](https://www.django-rest-framework.org)



## Redes Sociais

- [@Github](https://github.com/MoisesMonter)
- [@Instagram](https://instagram.com/moises.mtro/)

## Deploy

Para fazer o deploy desse projeto rode


```bash
   install -r req.txt
```
## Teste 
Para fazer o deploy desse projeto rode
```bash
  python manage.py runserver
```

## Funcionalidades

- CRIAR ELEIÇÃO API
- CRIAR CANDIDATOS API
- MANIPULAR VOTOS API
- Visualizar pelo Djangoadmin


## Documentação da API

#### Criar Eleição
essa parte gerará a eleição particular para ser manipulado
```http
  GET localhost:8000/api/Lista_Eleicao/
  POST 
    {
      "eleicao_nome": "exemplo321",
      "eleicao_data_fim": "2023-05-19"
    }
```

#### Criar Candidato
essa parte pegará a eleição criada e gerará um candidato referente ao número da eleição
```http
  GET localhost:8000/api/Dado_Eleicao/
  POST 
    {
        "eleicao_n": 1,
        "candidato_nome": "candidatoExemplo321"
    }

```
#### Manipular Votos
essa parte pegará o dado do candidato e incrementará 1[UM] VOTO.
```http
  GET localhost:8000/api/Votar_Eleicao/
  POST 
    {
        "eleicao_n": 1,
        "candidato_nome": "candidatoExemplo321"
    }

```

#### Visualizar pelo Djangoadmin
Ver os dados Manipulados por API, Usando django Admin

```bash
  python manage.py createsuperuser
  CONTA DE TESTE
  (id:admin
   password:A123B456)
```
```http

  Admin: localhost:8000/admin/

```
