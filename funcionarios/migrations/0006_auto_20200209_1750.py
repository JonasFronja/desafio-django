# Generated by Django 3.0.3 on 2020-02-09 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0005_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='departamento',
            field=models.ManyToManyField(related_name='funcionarios', to='funcionarios.Departamento'),
        ),
    ]
