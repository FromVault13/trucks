from django.shortcuts import render
from .models import Samosval
from django.db.models import F
from django.db.models.functions import Greatest

def main(request):
    """main page with table"""
    if request.method == 'POST' and request.POST.get('mark', default='Все') != 'Все':
        data = Samosval.objects.annotate(overload=Greatest((F('current_cargo')-F('max_cargo'))*100/F('max_cargo'), 0))\
            .filter(mark=request.POST.get('mark'))
    else:
        data = Samosval.objects.annotate(overload=Greatest((F('current_cargo')-F('max_cargo'))*100/F('max_cargo'), 0))
    models = ['Все'] + list(i['mark'] for i in Samosval.objects.values('mark').distinct())
    context = {'models': models,
               'trucks': [
                   [i.board_num, i.mark, i.max_cargo, i.current_cargo, i.overload] for i in data]}
    return render(request, 'main/main.html', context=context)
