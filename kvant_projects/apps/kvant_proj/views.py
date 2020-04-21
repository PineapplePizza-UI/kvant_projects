from django.shortcuts import render
from django.http import HttpResponse
from kvant_projects.apps.kvant_proj.models import Key_words, Kvantum, Kvantorianec, Master, kvant_projects


# Create your views here.

def index(request):
    kvantorianec_list = Kvantorianec.objects.all()
    context = {
        "kv_list": kvantorianec_list
    }
    return render(request, 'index.html', context)

def kvantums(request):
    Kvantum_list = Kvantum.objects.all()
    context = {
        "kvant_list": Kvantum_list
    }
    return render(request, 'kvantum_list.html', context)
