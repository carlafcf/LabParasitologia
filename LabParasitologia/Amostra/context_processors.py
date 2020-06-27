from Amostra.models import Amostra
from datetime import date, timedelta

def amostras_pendentes(request):
<<<<<<< HEAD
    if (request.user.is_authenticated):
        amostras = Amostra.objects.filter(
            responsavel=request.user, status=True,
            data_coleta__lte = date.today()- timedelta(days=10))
    else:
        amostras = Amostra.objects.filter(
=======
    return {
        'amostras_pendentes_count': Amostra.objects.filter(
             status=True,
            data_coleta__lte = date.today()- timedelta(days=10)).count(),
        'amostras_pendentes': Amostra.objects.filter(

>>>>>>> 85ff3c66ba56c5a9aabd4f22e82111e909bb0418
            status=True,
            data_coleta__lte = date.today()- timedelta(days=10))
    return {
        'amostras_pendentes_count': amostras.count(),
        'amostras_pendentes': amostras.order_by('data_coleta')
    }