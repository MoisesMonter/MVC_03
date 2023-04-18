from django.urls import path

from . import views

# from view import api_home


urlpatterns = [
    path('',views.api_home),
]