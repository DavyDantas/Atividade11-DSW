from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', listAlunos, name="ListAluno"),
    path('<int:pk>', detalheAluno, name="detalheAluno"),
    path('form-Aluno', alunoForm, name="alunoForm"),
]
