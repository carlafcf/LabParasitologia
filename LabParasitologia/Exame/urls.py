from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
app_name = 'exame'

urlpatterns = [
    #path('AdicionarExame/<int:pk>', views.AdicionarExame.as_view(), name='AdicionarExame'),
    path('AdicionarExame/<int:pk>', views.addExame, name='AdicionarExame'),
    url('ListarExame/', views.exameListar, name='ListarExame'),
    url('examesInativos/', views.examesInativos, name='examesInativos'),
    url('CadastrarExame/', views.CadastrarExame.as_view(), name='CadastrarExame'),
    path('DestalhesExame/<int:pk>', views.DetalheExame.as_view(), name='DetalheExame'),
    path('EditarExame/<int:pk>', views.EditarExame.as_view(), name='EditarExame'),
    path('DeletarExame/<int:pk>', views.DeletarExame.as_view(), name='DeletarExame'),
    path('mudar_status_exame/<int:status>/<int:exame>', views.mudar_status_exame, name='mudar_status_exame'),

]
