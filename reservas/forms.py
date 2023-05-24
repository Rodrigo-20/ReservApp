from django import forms
from django.forms import ModelForm
from .models import Employee, Coordinator


class EmployeeForm(ModelForm):
       class Meta:
        model = Employee
        fields = ['name', 'lastname', 'file_number' ]
        labels = {
            'name': 'Nombre',
            'lastname': 'Apellido',
            'file_number': 'Numero de Legajo',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'lastname': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'file_number': forms.TextInput(attrs={
                'class': 'form-control',
                "type" : "number"
            }),

        }


class CoordinatorFormRegister(ModelForm):
    class Meta:
        model = Coordinator
        fields = ['name', 'lastname', 'dni_number']
        labels = {
            'name': 'Nombre',
            'lastname': 'Apellido',
            'dni_number': 'Numero de Dni',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 50%;',
                'type': 'text'

            }),
            'lastname': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 50%;',
                'type': 'text'
            }),
            'dni_number': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 50%;',
                'type': 'number',
                'min': '1000000',
                'max': '46000000'
            }),
        }


 class CoordinatorFormUpdate(ModelForm):
    class Meta:
        model = Coordinator
        fields = ['name', 'lastname', 'dni_number', 'created_at', 'is_active']
        labels = {
            'name': "Nombre",
            'lastname': "Apellido",
            'dni_number': "Nro. DNI",
            'is_active': "Activo"
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'lastname': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'dni_number': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number'
            })
        }