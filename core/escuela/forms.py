from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import Preceptor,Aula,Alumno,Materia,Curso,Turno,Tiene,Rinde,Profesor,Dicta
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

'''class TipoUsuarioForm(ModelForm):
    class Meta:
        model = TipoUsuario
        fields = '__all__'
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control input', 'text-transform':'capitalize'})
                    }
        help_texts = {k:"" for k in fields }'''

'''class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = '__all__' # ('nombre')
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control input', 'text-transform':'capitalize'})
                    }
'''
class DateInput(forms.DateInput):
    input_type='date'

class PreceptorForm(ModelForm):
    class Meta:
        model = Preceptor
        fields = '__all__'
        widgets = { 'nombre': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize'}),
                    'apellido': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize'}),
                    'num_doc': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'id':'dni', 'placeholder':'12.345.678'}),
                    'num_cuil': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'id':'cuit', 'placeholder':'12-34.567.890-1'}),
                    'fecha_nac': DateInput(format='%Y-%m-%d', attrs={'class':'form-control input-sm','min':"2002-01-01", 'max':"2009-01-01"}),
                    'telefono': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'id':'phone', 'placeholder':'(264) 512-3456'}),
                    'direccion': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'placeholder':'Las Heras 430 Este'}),
                    }
        help_texts = {k:"" for k in fields }

class AulaForm(ModelForm):
    class Meta:
        model = Aula
        fields = '__all__'
        widgets = { 'año': forms.Select(attrs={'type':'number', 'class':'form-control input'}),
                    'division': forms.Select(attrs={'type':'number', 'class':'form-control input', 'text-transform':'capitalize'}),
                    'preceptor': forms.Select(attrs={'class':'form-control input', 'text-transform':'capitalize'}),
                    #'cant_alumnos': forms.TextInput(attrs={'type':'number','class':'form-control input', 'text-transform':'capitalize', 'min':'1'}),
                    #'materia': forms.Select(attrs={'class':'form-control input', 'text-transform':'capitalize'}),
                    }
        help_texts = {k:"" for k in fields }

class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
        widgets = { 'num_reg': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'name':'registro', 'id':'registro'}),
                    'nombre': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize'}),
                    'apellido': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize'}),
                    'num_doc': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'id':'dni', 'placeholder':'12.345.678'}),
                    'fecha_nac': DateInput(format='%Y-%m-%d', attrs={'class':'form-control input-sm','min':"2002-01-01", 'max':"2009-01-01"}),
                    'telefono': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'id':'phone', 'placeholder':'(264) 512-3456'}),
                    'aula': forms.Select(attrs={'class':'form-control input', 'text-transform':'capitalize', 'id':"exampleFormControlSelect2"}),
                    }
        help_texts = {k:"" for k in fields }

class MateriaForm(ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'
        widgets = { 'codigo': forms.TextInput(attrs={'type':'number','class':'form-control input', 'text-transform':'capitalize', 'min':'1'}),
                    'nombre': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize'}),
                    'cant_horas': forms.TextInput(attrs={'type':'number','class':'form-control input', 'text-transform':'capitalize', 'min':'1'}),
                    }
        help_texts = {k:"" for k in fields }

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        widgets = { 'materia_codigo': forms.Select(attrs={'class':'form-control input'}),
                    'aula_idAula': forms.Select(attrs={'class':'form-control input'}),
                    'dia_clase': forms.SelectMultiple(attrs={'class':'form-control input', 'text-transform':'capitalize'}),
                    }
        help_texts = {k:"" for k in fields }

class TurnoForm(ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'
        widgets = { 'nombre': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize'}),
                    }
        help_texts = {k:"" for k in fields }

class TieneForm(ModelForm):
    class Meta:
        model = Tiene
        fields = '__all__'
        widgets = { 'aula_idAula': forms.Select(attrs={'class':'form-control input'}),
                    'turno_idTurno': forms.Select(attrs={'class':'form-control input'}),
                    'hora_ingreso': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'placeholder':'00:00'}),
                    'hora_egreso': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'placeholder':'00:00'}),
                    }
        help_texts = {k:"" for k in fields }

class RindeForm(ModelForm):
    class Meta:
        model = Rinde
        fields = '__all__'
        widgets = { 'materia_codigo': forms.Select(attrs={'class':'form-control input'}),
                    'alumno_nro_registro': forms.Select(attrs={'class':'form-control input'}),
                    'nota_1': forms.TextInput(attrs={'type':'number','class':'form-control input', 'text-transform':'capitalize', 'min':'1'}),
                    'nota_2': forms.TextInput(attrs={'type':'number','class':'form-control input', 'text-transform':'capitalize', 'min':'1'}),
                    'nota_3': forms.TextInput(attrs={'type':'number','class':'form-control input', 'text-transform':'capitalize', 'min':'1'}),
                    }
        help_texts = {k:"" for k in fields }

class ProfesorForm(ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'
        widgets = { 'nombre': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize'}),
                    'apellido': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize'}),
                    'num_doc': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'id':'dni', 'placeholder':'12.345.678'}),
                    'num_cuil': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'id':'cuit', 'placeholder':'12-34.567.890-1'}),
                    'fecha_nac': DateInput(format='%Y-%m-%d', attrs={'class':'form-control input-sm','min':"2002-01-01", 'max':"2009-01-01"}),
                    'telefono': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'id':'phone', 'placeholder':'(264) 512-3456'}),
                    'direccion': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'placeholder':'Las Heras 430 Este'}),
                    }
        help_texts = {k:"" for k in fields }

class DictaForm(ModelForm):
    class Meta:
        model = Dicta
        fields = '__all__'
        widgets = { 'profesor_id_profesor': forms.Select(attrs={'class':'form-control input'}),
                    'materia_codigo': forms.Select(attrs={'class':'form-control input'}),
                    'cargo': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'placeholder':'Titular'}),
                    }
        help_texts = {k:"" for k in fields }