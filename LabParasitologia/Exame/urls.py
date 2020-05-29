from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
app_name = 'exame'

urlpatterns = [
    url('AdicionarExame/', views.AdicionarExame.as_view(), name='AdicionarExame'),
]
