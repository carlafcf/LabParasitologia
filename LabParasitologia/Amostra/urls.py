"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'amostra'

urlpatterns = [
	path('home/', views.home, name='home'),

	path('', views.home, name='home'),
	path('listar/', views.listar, name='listar'),
	path('listar/finalizadas', views.listar_finalizadas, name='listar_finalizadas'),
	path('listar/usuario/<int:pk>', views.listar_amostras_usuario, name='listar_amostras_usuario'),
	path('listar/finalizadas/usuario/<int:pk>', views.listar_amostras_finalizadas_usuario, name='listar_amostras_finalizadas_usuario'),

	path('cadastrar/', views.cadastrar, name='cadastrar'),
	path('detalhes/<int:pk>', views.detalhes, name='detalhes'),
	path('editar/<int:pk>', views.Editar.as_view(), name='editar'),
	path('deletar/<int:pk>', views.Deletar.as_view(), name='deletar'),
	
	path('mudar-status/<int:status>/<int:amostra>', views.mudar_status, name='mudar_status'),
	path('alertas/', views.listar_alertas, name='listar_alertas'),

	path('download/', views.download_amostras, name='download')

]
