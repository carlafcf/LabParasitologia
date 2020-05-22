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
    url('listarUsuarios/', views.menuUsuarios, name='menu'),
    path('deletarUsuario/<int:pk>', views.DeletarUser.as_view(), name='deletarUser'),
    path('detalhesUsuario/<int:pk>', views.DetalheUser.as_view(), name='detalhesUser'),
]
