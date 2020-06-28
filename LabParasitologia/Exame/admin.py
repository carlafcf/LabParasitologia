from django.contrib import admin

from .models import Exame, RealizacaoExame, ResultadoExame

admin.site.register(Exame)
admin.site.register(RealizacaoExame)
admin.site.register(ResultadoExame)

