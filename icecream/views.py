from django.http import HttpResponse
from .models import icecream_db


def icecream_list(request):
    icecreams = []
    for icecream in icecream_db:
        icecreams.append(icecream['name'])

    response = '::'.join(icecreams)
    return HttpResponse(f'Cписок сортов мороженого: {response}')
