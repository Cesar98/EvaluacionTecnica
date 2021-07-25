from EmployeesManagement.models import Empleados
from django.http import HttpResponse;
from django.template import Template, Context, loader;
from django.shortcuts import render;
from EmployeesManagement.models import Empleados, Departamentos, Empresas

def home(request):
    return render(request, 'home.html')

def list_employees(request):
    empleados = Empleados.objects.all()
    return render(request, 'listEmployees.html', {'empleados':empleados})
    
def form_employees(request):
    departamentos = Departamentos.objects.all()
    return render(request, 'form_employees.html', {'departamentos':departamentos})

def buscar(request):
    if request.GET['searchEMp'] != '':
        if request.GET['tipo'] == '1':

            mensaje = 'El empleado %s se esta buscando por nombre...' % request.GET['searchEMp']
            busqueda = request.GET['searchEMp']
            empleados = Empleados.objects.filter(nombre__contains='%s' % busqueda)

        elif request.GET['tipo'] == '2':

            mensaje = 'El empleado %s se esta buscando por departamento...' % request.GET['searchEMp']
            busqueda = request.GET['searchEMp']
            dep = Departamentos.objects.get(departamento='%s' % busqueda)
            empleados = Empleados.objects.filter(departamento='%s' % dep.id)

        elif request.GET['tipo'] == '3':

            mensaje = 'El empleado %s se esta buscando por empresa...' % request.GET['searchEMp']
            busqueda = request.GET['searchEMp']

            empresa = Empresas.objects.get(empresa='%s' % busqueda)
            dep = Departamentos.objects.filter(empresa='%s' % empresa.id)

            empleados = Empleados.objects.filter(departamento_id__in= dep)
            
    else:
        mensaje = 'No se ingreso nada en el formulario'
        empleados = Empleados.objects.all()
        
    return render(request, 'listEmployees.html', {'mensaje': mensaje, 'empleados': empleados})

def crear(request):
    dep = Departamentos.objects.get(departamento='%s' % request.GET['departamento'] )
    newEmp = Empleados(nombre='%s' % request.GET['nombre'],
                        fecha_nacimiento='%s' % request.GET['fecha_nacimiento'],
                        email='%s' % request.GET['email'],
                        genero='%s' % request.GET['genero'],
                        telefono='%s' % request.GET['telefono'],
                        celular='%s' % request.GET['celular'],
                        fecha_ingreso='%s' % request.GET['fecha_ingreso'],
                        departamento=dep)
    if newEmp.save():
        mensaje = 'No se pudo realizar la operacion'
    else:
        mensaje = 'El empleado se creo correctamente'
        
    empleados = Empleados.objects.all()
    return render(request, 'listEmployees.html', {'mensaje':mensaje, 'empleados': empleados})

def editar(request, id):
    emp = Empleados.objects.get(id='%s' %id)
    departamentos = Departamentos.objects.all()
    return render(request, 'form_employees.html', {'departamentos':departamentos, 'emp': emp})
    
def editarF(request):
    dep = Departamentos.objects.get(departamento='%s' % request.GET['departamento'])
    emp = Empleados.objects.get(id='%s' % request.GET['id'])
    emp.nombre='%s' % request.GET['nombre']
    emp.fecha_nacimiento='%s' % request.GET['fecha_nacimiento']
    emp.email='%s' % request.GET['email']
    emp.genero='%s' % request.GET['genero']
    emp.telefono='%s' % request.GET['telefono']
    emp.celular='%s' % request.GET['celular']
    emp.fecha_ingreso='%s' % request.GET['fecha_ingreso']
    emp.departamento=dep

    if emp.save():
        mensaje = 'No se pudo realizar la operacion'
    else:
        mensaje = 'El empleado se edito correctamente'
    empleados = Empleados.objects.all()
    return render(request, 'listEmployees.html', {'mensaje':mensaje, 'empleados': empleados})

def eliminar(request, id):
    emp = Empleados.objects.get(id='%s' %id)
    if emp.delete():
        mensaje = 'Se pudo realizar la operacion'
    else:
        mensaje = 'El empleado se elimino correctamente'
    empleados = Empleados.objects.all()
    return render(request, 'listEmployees.html', {'mensaje':mensaje, 'empleados': empleados})
