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

from Amostra import views

app_name = 'amostra'

urlpatterns = [
	path('home/', views.home, name='home'),
	path('', views.listar, name='listar'),
	path('listar', views.listar, name='listar'),
	#path('nova', views.adicionar, name='adicionar'),
	path('nova', views.CriarAmostra.as_view(), name='adicionar'),
	path('detalhes/<int:pk>', views.DetalheAmostra.as_view(), name='detalhes'),
	path('editar/<int:pk>', views.EditarAmostra.as_view(), name='editar'),
	path('deletar/<int:pk>', views.DeletarAmostra.as_view(), name='deletar'),
	path('listarAmostraUser/<int:pk>', views.listarAmostraUser, name='listarAmostraUser'),
	path('listarAmostraUserFinalizada/<int:pk>', views.listarAmostraFinalizada, name='listarAmostraUserFinalizada'),
	path('mudar_status/<int:status>/<int:amostra>', views.mudar_status, name='mudar_status'),

]
