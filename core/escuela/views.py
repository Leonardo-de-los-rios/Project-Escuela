from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic import FormView, RedirectView
import prj_escuela.settings as setting
from .forms import PersonaForm,GeneroForm,TurnoForm,CursoForm,AlumnoForm,TipoUsuarioForm,UserRegisterForm
from .models import Genero,Persona,Turno,Curso,Alumno
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.user.models import TipoUsuario,User
from datetime import datetime
from dateutil.relativedelta import relativedelta # calcula la edad

def index(request,template_name='escuela/index.html'):
    return render(request,template_name)

def index_admin(request,template_name='escuela/index_admin.html'):
    return render(request,template_name)

def register(request,username=None,template_name='escuela/register.html'):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			user = User.objects.get(username=username)
			messages.success(request, f'Usuario {username} creado.')
			return redirect('index') #
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, template_name, context)

@login_required
def nuevo_tipo_usuario(request,template_name='escuela/tipo_usuario_form.html'):
    if request.method=='POST':
        form = TipoUsuarioForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = TipoUsuarioForm()
    dato={'form':form}
    return render(request,template_name,dato)

def nuevo_genero(request,template_name='escuela/genero_form.html'):
    if request.method=='POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = GeneroForm()
    dato={'form':form}
    return render(request,template_name,dato)

def nueva_persona(request,template_name='escuela/persona_form.html'):
    if request.method=='POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = PersonaForm()
    dato={'form':form}
    return render(request,template_name,dato)

def nuevo_turno(request,template_name='escuela/turno_form.html'):
    if request.method=='POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = TurnoForm()
    dato={'form':form}
    return render(request,template_name,dato)

def nuevo_curso(request,template_name='escuela/curso_form.html'):
    if request.method=='POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = CursoForm()
    dato={'form':form}
    return render(request,template_name,dato)

def nuevo_alumno(request,template_name='escuela/alumno_form.html'):
    if request.method=='POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = AlumnoForm()
    dato={'form':form}
    return render(request,template_name,dato)

def listar_tipos_usuario(request, template_name='escuela/tipos_usuario.html'):
    tipos_usuario = TipoUsuario.objects.all()
    dato = {'tipos_usuario': tipos_usuario}
    return render(request,template_name,dato)

def listar_usuarios(request, template_name='escuela/usuarios.html'):
    usuarios = User.objects.all()
    dato = {'usuarios': usuarios}
    return render(request,template_name,dato)

def listar_generos(request, template_name='escuela/generos.html'):
    generos = Genero.objects.all()
    dato = {'generos': generos}
    return render(request,template_name,dato)

def listar_personas(request, template_name='escuela/personas.html'):
    personas = Persona.objects.all()
    for persona in personas:
        persona.edad = relativedelta(datetime.now(), persona.fecha_nac).years
    dato = {'personas': personas}
    return render(request,template_name,dato)

def listar_turnos(request, template_name='escuela/turnos.html'):
    turnos = Turno.objects.all()
    dato = {'turnos': turnos}
    return render(request,template_name,dato)

def listar_cursos(request, template_name='escuela/cursos.html'):
    cursos = Curso.objects.all()
    dato = {'cursos': cursos}
    return render(request,template_name,dato)

def listar_alumnos(request, template_name='escuela/alumnos.html'):
    alumnos = Alumno.objects.all()
    for alumno in alumnos:
        alumno.persona.edad = relativedelta(datetime.now(), alumno.persona.fecha_nac).years
    dato = {'alumnos': alumnos}
    return render(request,template_name,dato)

def modificar_persona(request,pk,template_name='escuela/persona_form.html'):
    persona = Persona.objects.get(num_cuit=pk)
    form = PersonaForm(request.POST or None, instance=persona)
    if form.is_valid():
        form.save(commit=True)
        return redirect('personas')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

def eliminar_persona(request,pk,template_name='escuela/persona_confirmar_eliminacion.html'):
    persona=Persona.objects.get(num_cuit=pk)
    if request.method=='POST':
        persona.delete()
        return redirect('personas')
    else:
        dato={'form':persona}
        return render(request,template_name,dato)