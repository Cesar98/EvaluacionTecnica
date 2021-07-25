# Generated by Django 3.2.5 on 2021-07-25 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeesManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamentos',
            name='departamento',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='celular',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='genero',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='telefono',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='empresa',
            field=models.CharField(max_length=20),
        ),
    ]
