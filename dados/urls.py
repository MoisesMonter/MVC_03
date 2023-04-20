from django.urls import path,include

from . import views
from dados.views import *



urlpatterns = [
    path('',api_home),
    path('Lista_Eleicao/',Eleicao_Lista),
    path('Dado_Eleicao/',Eleicao_Dado),
    path('Votar_Eleicao',Votar_Eleicao),
]

#urlpatterns+=router.urls