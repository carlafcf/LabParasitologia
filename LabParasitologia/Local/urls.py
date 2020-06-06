from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
app_name = 'local'

urlpatterns = [
    url('CadastrarLocal/', views.CadastrarLocal.as_view(), name='cadastrarLocal'),
    url('ListarLocal/', views.localListar, name='listarLocal'),
    path('DetalhesLocal/<int:pk>', views.local_amostraDetalhes, name='detalhesLocal'),
    path('EditarLocal/<int:pk>', views.EditarLocal.as_view(), name='EditarLocal'),
    path('DeletarLocal/<int:pk>', views.DeletarLocal.as_view(), name='DeletarLocal'),
]
