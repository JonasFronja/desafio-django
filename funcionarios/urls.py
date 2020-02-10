from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:empresa_id>", views.empresa, name="empresa"),
    path("departamento/<int:departamento_id>", views.departamento, name="departamento"),
]