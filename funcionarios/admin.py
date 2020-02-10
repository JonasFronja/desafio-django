from django.contrib import admin


from .models import Empresa,Departamento,Funcionario

admin.site.register(Empresa)
admin.site.register(Departamento)
admin.site.register(Funcionario)
