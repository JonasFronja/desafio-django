from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Empresa(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Departamento(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,related_name="departamentos")
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empresa = models.ManyToManyField(Empresa,related_name="funcionarios")
    departamento = models.ManyToManyField(Departamento,related_name="departamentos")

    def __str__(self):  
        return "%s" % self.user 

def create_funcionario(sender, instance, created, **kwargs):  
    if created:  
       profile, created = Funcionario.objects.get_or_create(user=instance)  

post_save.connect(create_funcionario, sender=User) 
