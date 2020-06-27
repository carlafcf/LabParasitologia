from Amostra.models import Amostra
from datetime import date, timedelta

def amostras_pendentes(request):
    return {
        'amostras_pendentes_count': Amostra.objects.filter(
             status=True,
            data_coleta__lte = date.today()- timedelta(days=10)).count(),
        'amostras_pendentes': Amostra.objects.filter(

            status=True,
            data_coleta__lte = date.today()- timedelta(days=10)).
            order_by('data_coleta')
    }