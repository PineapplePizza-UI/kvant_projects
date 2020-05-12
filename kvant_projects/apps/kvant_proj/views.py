from django.shortcuts import render
from django.http import HttpResponse
from kvant_projects.apps.kvant_proj.models import Key_words, Kvantum, Kvantorianec, Master, Kvant_projects


# Create your views here.

def index(request):
    kvantorianec_list = Kvantorianec.objects.all()
    project_list = Kvant_projects.objects.all()
    context = {
        "kv_list": kvantorianec_list,
        "proj_list": project_list,
    }
    return render(request, 'index.html', context)

def kvantums(request):
    Kvantum_list = Kvantum.objects.all()
    context = {
        "kvant_list": Kvantum_list
    }
    return render(request, 'kvantum_list.html', context)


def kvantum(request, kvantum_id):
    kvant = Kvantum.objects.get(id=kvantum_id)
    context = {
        "kvant": kvant
    }
    return render(request, 'kvantum.html', context)


def kvant_project(request, project_id):
    project = Kvant_projects.objects.get(id=project_id)
    context = {
        "project": project,
        "kvantirianec": project.kvantorianec.all(),
        "kvantums": project.kvantum.all(),
    }
    return render(request, 'project.html', context)
