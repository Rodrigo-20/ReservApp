from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm, CoordinatorForm
from .models import Employee, Coordinator


# Create your views here.
def index(request):
    return HttpResponse("<h1> Hola Mundo </h1>")


def employee_register(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('list')
    form = EmployeeForm()
    
    return render(request, 'employee_register.html', {
        'form': form,
        "submit": "Registrar Empleado"
    })


def employees_view(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})


def employee_activate(request, id):
    employee = Employee.objects.get(id=id)
    employee.is_active = True
    employee.save()
    
    return redirect("list")


def employee_update(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            
            return redirect("list")
    form = EmployeeForm(instance=employee)
    
    return render(request, 'employee_update.html', {
        'form': form,
        'submit': 'Actualizar'
    })


def employee_deactivate(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.is_active = False
    employee.save()
    
    return redirect("list")


def employee_delete(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()

    return redirect("list")

  
def coordinators_view(request):
    coordinators = Coordinator.objects.all()
    
    return render(request, 'coordinators.html', {
        'coordinators': coordinators
    })
  
  
def coordinator_update(request, coordinator_id):
    coordinator = Coordinator.objects.get(id=coordinator_id)
    if request.method == 'POST':
        form = CoordinatorForm(request.POST, instance=coordinator)
        if form.is_valid():
            form.save()
            
            return redirect("list")
          
    form = CoordinatorForm(instance=coordinator)
    
    return render(request, 'coordinator_update.html', {
        'form': form,
        'submit': 'Actualizar'
    })
