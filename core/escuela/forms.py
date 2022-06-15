from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import Persona,Genero,Turno,Curso,Alumno
from core.user.models import TipoUsuario,User

# ESTABLECEMOS LOS WIDGETS DE LOS FORMULARIOS
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
    

	class Meta:
		model = User
		fields = ['username','password1','password2','tipo']
		widgets = { 'tipo': forms.Select(attrs={'class': 'form-control input', 'text-transform':'capitalize'}),
                    }
		help_texts = {k:"" for k in fields }

class TipoUsuarioForm(ModelForm):
    class Meta:
        model = TipoUsuario
        fields = '__all__'
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control input', 'text-transform':'capitalize'})
                    }

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = '__all__' # ('nombre')
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control input', 'text-transform':'capitalize'})
                    }

class DateInput(forms.DateInput):
    input_type='date'

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = { 'nombre': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize'}),
                    'apellido': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize'}),
                    'num_doc': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'id':'dni', 'placeholder':'12.345.678'}),
                    'num_cuit': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'id':'cuit', 'placeholder':'12-34.567.890-1'}),
                    'fecha_nac': DateInput(format='%Y-%m-%d', attrs={'class':'form-control input-sm','min':"2002-01-01", 'max':"2009-01-01"}),
                    'telefono': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'id':'phone', 'placeholder':'(264) 512-3456'}),
                    'email': forms.EmailInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'placeholder':'nombreUsuario@domino.com'}),
                    'direccion': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'placeholder':'Las Heras 430 Este'}),
                    'genero': forms.Select(attrs={'class':'form-control input'}),
                    'usuario': forms.Select(attrs={'class':'form-control input', 'text-transform':'capitalize'}),
                    }

class TurnoForm(ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'
        widgets = { 'nombre': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize'}),
                    }

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        widgets = { 'año': forms.Select(attrs={'type':'number', 'class':'form-control input'}),
                    'division': forms.Select(attrs={'type':'number', 'class':'form-control input', 'text-transform':'capitalize'}),
                    'turno': forms.Select(attrs={'class':'form-control input', 'text-transform':'capitalize'}),
                    'cant_alumnos': forms.TextInput(attrs={'type':'number','class':'form-control input', 'text-transform':'capitalize', 'min':'1'}),
                    #'materia': forms.Select(attrs={'class':'form-control input', 'text-transform':'capitalize'}),
                    }

class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
        widgets = { 'persona': forms.Select(attrs={'class':'form-control input', 'text-transform':'capitalize'}),
                    'num_reg': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'name':'registro', 'id':'registro'}),
                    'curso': forms.Select(attrs={'class':'form-control input', 'text-transform':'capitalize', 'id':"exampleFormControlSelect2"}),
                    }