from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Empresa,Funcionario,Departamento

@login_required
def index(request):
    user = request.user

    context = {
        "empresas": Empresa.objects.all()
    }

    return render(request, "pages/listar.html",context)

def empresa(request, empresa_id):
    try:
        empresa = Empresa.objects.get(pk=empresa_id)
    except Empresa.DoesNotExist:
        raise Http404("Empresa não existe")
    context = {
        "empresa": empresa,
        "funcionario": empresa.funcionarios.all(),
        "departamentos": empresa.departamentos.all(),
    }

    return render(request, "pages/departamento.html", context)

def departamento(request, departamento_id):
    try:
        departamento = Departamento.objects.get(pk=departamento_id)
    except Departamento.DoesNotExist:
        raise Http404("Departamento não existe")
    context = {
        "departamento": departamento,
        "funcionarios": departamento.departamentos.all(),
        "no_funcionarios": Funcionario.objects.exclude(departamento = departamento).all()
    }

    return render(request, "pages/funcionarios.html", context)

