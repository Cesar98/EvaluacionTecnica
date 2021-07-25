from django.contrib import admin
from EmployeesManagement.models import Empresas, Departamentos, Empleados 

class EmpleadosAdmin(admin.ModelAdmin):
    list_display=('nombre', 'fecha_nacimiento', 'email', 'genero', 'telefono', 'celular', 'fecha_ingreso', 'departamento')
    list_filter=('nombre', 'fecha_ingreso', 'departamento')
    date_hierarchy=('fecha_ingreso')

class DepartamentosAdmin(admin.ModelAdmin):
    list_display=('departamento', 'empresa')
    list_filter=('empresa',)
    
admin.site.register(Departamentos, DepartamentosAdmin)
admin.site.register(Empleados, EmpleadosAdmin)
admin.site.register(Empresas)