from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
app_name = 'usuario'

urlpatterns = [
    url('login/', auth_views.LoginView.as_view(template_name='Usuario/login.html'), name='login'),
    url('logout/', auth_views.LogoutView.as_view(), name='logout'),
    url('cadastrar/', views.Cadastrar.as_view(), name='cadastrar'),
    path('editar/<int:pk>', views.Editar.as_view(), name = 'editar'),
    url('listar/', views.listar, name='listar'),
    url('listar-inativos/', views.listar_inativos, name='listar_inativos'),
    path('deletar/<int:pk>', views.Deletar.as_view(), name='deletar'),
    path('detalhes/<int:pk>', views.Detalhes.as_view(), name='detalhes'),
    path('mudar-status-coordenacao/<int:coord_status>/<int:usuario>', views.mudar_coordenacao_status, name='mudar_coordenacao_status'),
    path('mudar-status-ativo/<int:ativo_status>/<int:usuario>', views.mudar_ativo_status, name='mudar_ativo_status'),
]
