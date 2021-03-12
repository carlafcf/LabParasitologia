from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
app_name = 'exame'

urlpatterns = [
    #path('AdicionarExame/<int:pk>', views.AdicionarExame.as_view(), name='AdicionarExame'),
    path('AdicionarExame/<int:pk>', views.addExame, name='AdicionarExame'),
    path('NovoAdicionarExame/<int:pk>/<int:exame>', views.novoAddExame, name='NovoAdicionarExame'),
    # path('DefinirResultados/<int:pk>', views.definir_resultados, name='definir_resultados'),
    path('ListarExame/', views.exameListar, name='ListarExame'),
    path('examesInativos/', views.examesInativos, name='examesInativos'),
    # path('CadastrarExame/', views.CadastrarExame.as_view(), name='CadastrarExame'),
    path('cadastrar/', views.cadastrar_exame, name='cadastrar'),
    path('cadastrar/resultados/<str:nome>/<str:tipo_resultado>', views.definir_saidas, name='resultados'),
    path('DestalhesExame/<int:pk>', views.NovoDetalheExame, name='DetalheExame'),
    path('EditarExame/<int:pk>', views.EditarExame.as_view(), name='EditarExame'),
    path('DeletarExame/<int:pk>', views.DeletarExame.as_view(), name='DeletarExame'),
    path('mudar_status_exame/<int:status>/<int:exame>', views.mudar_status_exame, name='mudar_status_exame'),

]
