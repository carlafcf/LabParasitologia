from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
app_name = 'exame'

urlpatterns = [
    #path('AdicionarExame/<int:pk>', views.listarRealizacaoExame, name='AdicionarExame'),
    url('AdicionarExame/', views.AdicionarExame.as_view(), name='AdicionarExame'),
    url('CadastrarExame/', views.CadastrarExame.as_view(), name='CadastrarExame'),
]
