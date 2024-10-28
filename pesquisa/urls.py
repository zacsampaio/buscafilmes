from django.urls import path

from . import views

urlpatterns = [
    path('', views.buscar_filmes, name='buscar_filmes')
]
