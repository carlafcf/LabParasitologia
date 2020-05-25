from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
app_name = 'usuario'

urlpatterns = [
    url('login/', auth_views.LoginView.as_view(template_name='Usuario/login.html'), name='login'),
    url('logout/', auth_views.LogoutView.as_view(), name='logout'),
    url('cadastrar/', views.SignUp.as_view(), name='cadastrar'),
    path('editarUsuario/<int:pk>', views.EditarUsuario.as_view(), name = 'editar'),
    url('listarUsuarios/', views.listarUsuarios, name='listar'),
    url('usuariosInativos/', views.usuariosInativos, name='inativos'),
    path('deletarUsuario/<int:pk>', views.DeletarUser.as_view(), name='deletarUser'),
    path('detalhesUsuario/<int:pk>', views.DetalheUser.as_view(), name='detalhesUser'),
    path('mudar_coordenacao_status/<int:coord_status>/<int:usuario>', views.mudar_coordenacao_status, name='mudar_coordenacao_status'),
    path('mudar_ativo_status/<int:ativo_status>/<int:usuario>', views.mudar_ativo_status, name='mudar_ativo_status'),
]
