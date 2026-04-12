from django.urls import path
from . import views

urlpatterns = [
    path('lista_produtos', views.lista, name='lista_produtos'),
]