from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
app_name = 'local'

urlpatterns = [
    url('cadastrar/', views.Cadastrar.as_view(), name='cadastrar'),
    url('listar/', views.localListar, name='listarLocal'),
    path('detalhes/<int:pk>', views.listar_amostras_local, name='listar_amostras_local'),
    path('editar/<int:pk>', views.Editar.as_view(), name='editar'),
    path('deletar/<int:pk>', views.Deletar.as_view(), name='deletar'),
]
