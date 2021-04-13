from django.contrib import admin

from .models import Exame, ResultadoExame

admin.site.register(Exame)
admin.site.register(ResultadoExame)

