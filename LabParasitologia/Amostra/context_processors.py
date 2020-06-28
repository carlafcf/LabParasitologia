from Amostra.models import Amostra
from datetime import date, timedelta

def amostras_pendentes(request):
    if (request.user.is_authenticated):
        amostras = Amostra.objects.filter(
            responsavel=request.user, status=True,
            data_coleta__lte = date.today()- timedelta(days=10))
    else:
        amostras = Amostra.objects.filter(
            status=True,
            data_coleta__lte = date.today()- timedelta(days=10))
    return {
        'amostras_pendentes_count': amostras.count(),
        'amostras_pendentes': amostras.order_by('data_coleta')
    }