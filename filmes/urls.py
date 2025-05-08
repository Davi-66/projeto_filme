from django.urls import path
from filmes import views

urlpatterns = [
    path('cadastrarfilme/', views.cadastrarFilme, name='cadastrarFilme'),
    path('listarfilmes/', views.listarFilmes, name = 'listarfilmes'),

]