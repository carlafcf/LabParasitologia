from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

app_name = 'exame'

urlpatterns = [
    path('adicionar/<int:pk>', views.adicionar, name='adicionar'),
    path('adicionar/<int:pk>/<int:exame>', views.adicionar_exame_amostra, name='adicionar_exame_amostra'),
    # path('DefinirResultados/<int:pk>', views.definir_resultados, name='definir_resultados'),
    path('listar/', views.listar, name='listar'),
    path('listar-inativos/', views.listar_inativos, name='listar_inativos'),
    # path('CadastrarExame/', views.CadastrarExame.as_view(), name='CadastrarExame'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('cadastrar/resultados/<str:nome>/<str:tipo_resultado>', views.definir_saidas, name='resultados'),
    path('detalhes/<int:pk>', views.detalhes, name='detalhes'),
    path('detalhes/<int:pk>', views.NovoDetalheExame, name='DetalheExame'),
    path('editar/<int:pk>', views.Editar.as_view(), name='editar'),
    path('deletar/<int:pk>', views.Deletar.as_view(), name='deletar'),
    path('mudar-status/<int:status>/<int:exame>', views.mudar_status_exame, name='mudar_status_exame'),

    path('cadastrar-multiplos-resultados/<int:fase>/<int:pk>', views.cadastrar_multiplos_resultados, name='cadastrar_multiplos_resultados'),

	path('download/', views.download_exames, name='download')
]
