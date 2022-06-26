from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic import FormView, RedirectView
import prj_escuela.settings as setting
from .forms import UserRegisterForm,PreceptorForm,AulaForm,AlumnoForm,MateriaForm,CursoForm,TurnoForm,TieneForm,RindeForm,ProfesorForm,DictaForm
from .models import Preceptor,Aula,Alumno,Materia,Curso,Turno,Tiene,Rinde,Profesor,Dicta
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

'''@login_required
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
    return render(request,template_name,dato)'''

'''def nuevo_genero(request,template_name='escuela/genero_form.html'):
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
    return render(request,template_name,dato)'''

def nuevo_preceptor(request,template_name='escuela/preceptor_form.html'):
    if request.method=='POST':
        form = PreceptorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = PreceptorForm()
    dato={'form':form}
    return render(request,template_name,dato)

def nueva_aula(request,template_name='escuela/aula_form.html'):
    if request.method=='POST':
        form = AulaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = AulaForm()
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

def nueva_materia(request,template_name='escuela/materia_form.html'):
    if request.method=='POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = MateriaForm()
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

def nuevo_tiene(request,template_name='escuela/tiene_form.html'):
    if request.method=='POST':
        form = TieneForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = TieneForm()
    dato={'form':form}
    return render(request,template_name,dato)

def nuevo_rinde(request,template_name='escuela/rinde_form.html'):
    if request.method=='POST':
        form = RindeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = RindeForm()
    dato={'form':form}
    return render(request,template_name,dato)

def nuevo_profesor(request,template_name='escuela/profesor_form.html'):
    if request.method=='POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = ProfesorForm()
    dato={'form':form}
    return render(request,template_name,dato)

def nuevo_dicta(request,template_name='escuela/dicta_form.html'):
    if request.method=='POST':
        form = DictaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index') # invoca al nombre del name='...' en urls.py
        else:
            print(form.errors)
    else:
        form = DictaForm()
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

def listar_preceptores(request, template_name='escuela/preceptores.html'):
    preceptores = Preceptor.objects.all()
    for preceptor in preceptores:
        preceptor.edad = relativedelta(datetime.now(), preceptor.fecha_nac).years
    dato = {'preceptores': preceptores}
    return render(request,template_name,dato)

def listar_aulas(request, template_name='escuela/aulas.html'):
    aulas = Aula.objects.all()
    dato = {'aulas': aulas}
    return render(request,template_name,dato)

def listar_alumnos(request, template_name='escuela/alumnos.html'):
    alumnos = Alumno.objects.all()
    for alumno in alumnos:
        alumno.edad = relativedelta(datetime.now(), alumno.fecha_nac).years
    dato = {'alumnos': alumnos}
    return render(request,template_name,dato)

def listar_materias(request, template_name='escuela/materias.html'):
    materias = Materia.objects.all()
    dato = {'materias': materias}
    return render(request,template_name,dato)

def listar_cursos(request, template_name='escuela/cursos.html'):
    cursos = Curso.objects.all()
    dato = {'cursos': cursos}
    return render(request,template_name,dato)

def listar_turnos(request, template_name='escuela/turnos.html'):
    turnos = Turno.objects.all()
    dato = {'turnos': turnos}
    return render(request,template_name,dato)

def listar_tienen(request, template_name='escuela/tienen.html'):
    tienen = Tiene.objects.all()
    dato = {'tienen': tienen}
    return render(request,template_name,dato)

def listar_rinden(request, template_name='escuela/rinden.html'):
    rinden = Rinde.objects.all()
    dato = {'rinden': rinden}
    return render(request,template_name,dato)

def listar_profesores(request, template_name='escuela/profesores.html'):
    profesores = profesor.objects.all()
    for profesor in profesores:
        profesor.edad = relativedelta(datetime.now(), profesor.fecha_nac).years
    dato = {'profesors': profesores}
    return render(request,template_name,dato)

def listar_dictan(request, template_name='escuela/dictan.html'):
    dictan = Dicta.objects.all()
    dato = {'dictan': dictan}
    return render(request,template_name,dato)

'''def modificar_tipo_usuario(request,pk,template_name='escuela/tipo_usuario_form.html'):
    tipo_usuario = TipoUsuario.objects.get(nombre=pk)
    form = TipoUsuarioForm(request.POST or None, instance=tipo_usuario)
    if form.is_valid():
        form.save(commit=True)
        return redirect('tipo_usuarios')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)'''

'''def modificar_usuario(request,pk,template_name='escuela/usuario_form.html'):
    usuario = usuario.objects.get(num_cuit=pk)
    form = UserForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save(commit=True)
        return redirect('usuarios')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)'''
    
'''def modificar_genero(request,pk,template_name='escuela/genero_form.html'):
    genero = Genero.objects.get(nombre=pk)
    form = GeneroForm(request.POST or None, instance=genero)
    if form.is_valid():
        form.save(commit=True)
        return redirect('generos')
    else:
        print(form.errors)
    dato = {'form':form}
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
    return render(request,template_name,dato)'''

def modificar_preceptor(request,pk,template_name='escuela/preceptor_form.html'):
    preceptor = Preceptor.objects.get(num_reg=pk)
    form = PreceptorForm(request.POST or None, instance=preceptor)
    if form.is_valid():
        form.save(commit=True)
        return redirect('preceptores')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

def modificar_aula(request,pk,template_name='escuela/aula_form.html'):
    aula = Aula.objects.get(id=pk)
    form = AulaForm(request.POST or None, instance=aula)
    if form.is_valid():
        form.save(commit=True)
        return redirect('aulas')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

def modificar_alumno(request,pk,template_name='escuela/alumno_form.html'):
    alumno = Alumno.objects.get(num_reg=pk)
    form = AlumnoForm(request.POST or None, instance=alumno)
    if form.is_valid():
        form.save(commit=True)
        return redirect('alumnos')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

def modificar_materia(request,pk,template_name='escuela/materia_form.html'):
    materia = Materia.objects.get(nombre=pk)
    form = MateriaForm(request.POST or None, instance=materia)
    if form.is_valid():
        form.save(commit=True)
        return redirect('materias')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

def modificar_curso(request,pk,template_name='escuela/curso_form.html'):
    curso = Curso.objects.get(id=pk)
    form = CursoForm(request.POST or None, instance=curso)
    if form.is_valid():
        form.save(commit=True)
        return redirect('cursos')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

def modificar_turno(request,pk,template_name='escuela/turno_form.html'):
    turno = Turno.objects.get(nombre=pk)
    form = TurnoForm(request.POST or None, instance=turno)
    if form.is_valid():
        form.save(commit=True)
        return redirect('turnos')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

def modificar_tiene(request,pk,template_name='escuela/tiene_form.html'):
    tiene = Tiene.objects.get(nombre=pk)
    form = TieneForm(request.POST or None, instance=tiene)
    if form.is_valid():
        form.save(commit=True)
        return redirect('tienen')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

def modificar_rinde(request,pk,template_name='escuela/rinde_form.html'):
    rinde = Rinde.objects.get(nombre=pk)
    form = RindeForm(request.POST or None, instance=rinde)
    if form.is_valid():
        form.save(commit=True)
        return redirect('rinden')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

def modificar_profesor(request,pk,template_name='escuela/profesor_form.html'):
    profesor = Profesor.objects.get(num_reg=pk)
    form = ProfesorForm(request.POST or None, instance=profesor)
    if form.is_valid():
        form.save(commit=True)
        return redirect('profesores')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

def modificar_dicta(request,pk,template_name='escuela/dicta_form.html'):
    dicta = Dicta.objects.get(nombre=pk)
    form = DictaForm(request.POST or None, instance=dicta)
    if form.is_valid():
        form.save(commit=True)
        return redirect('dictan')
    else:
        print(form.errors)
    dato = {'form':form}
    return render(request,template_name,dato)

def eliminar_tipo_usuario(request,pk,template_name='escuela/tipo_usuario_confirmar_eliminacion.html'):
    tipo_usuario=TipoUsuario.objects.get(nombre=pk)
    if request.method=='POST':
        tipo_usuario.delete()
        return redirect('tipo_usuarios')
    else:
        dato={'form':tipo_usuario}
        return render(request,template_name,dato)

'''def eliminar_usuario(request,pk,template_name='escuela/usuario_confirmar_eliminacion.html'):
    usuario=User.objects.get(num_cuit=pk)
    if request.method=='POST':
        usuario.delete()
        return redirect('usuarios')
    else:
        dato={'form':usuario}
        return render(request,template_name,dato)'''

'''def eliminar_genero(request,pk,template_name='escuela/genero_confirmar_eliminacion.html'):
    genero=Genero.objects.get(nombre=pk)
    if request.method=='POST':
        genero.delete()
        return redirect('generos')
    else:
        dato={'form':genero}
        return render(request,template_name,dato)

def eliminar_persona(request,pk,template_name='escuela/persona_confirmar_eliminacion.html'):
    persona=Persona.objects.get(num_cuit=pk)
    if request.method=='POST':
        persona.delete()
        return redirect('personas')
    else:
        dato={'form':persona}
        return render(request,template_name,dato)'''

def eliminar_preceptor(request,pk,template_name='escuela/preceptor_confirmar_eliminacion.html'):
    preceptor=Preceptor.objects.get(nombre=pk)
    if request.method=='POST':
        preceptor.delete()
        return redirect('preceptores')
    else:
        dato={'form':preceptor}
        return render(request,template_name,dato)

def eliminar_aula(request,pk,template_name='escuela/aula_confirmar_eliminacion.html'):
    aula=Aula.objects.get(nombre=pk)
    if request.method=='POST':
        aula.delete()
        return redirect('aulas')
    else:
        dato={'form':aula}
        return render(request,template_name,dato)

def eliminar_alumno(request,pk,template_name='escuela/alumno_confirmar_eliminacion.html'):
    alumno=Alumno.objects.get(num_reg=pk)
    if request.method=='POST':
        alumno.delete()
        return redirect('alumnos')
    else:
        dato={'form':alumno}
        return render(request,template_name,dato)

def eliminar_materia(request,pk,template_name='escuela/materia_confirmar_eliminacion.html'):
    materia=Materia.objects.get(num_reg=pk)
    if request.method=='POST':
        materia.delete()
        return redirect('materias')
    else:
        dato={'form':materia}
        return render(request,template_name,dato)

def eliminar_curso(request,pk,template_name='escuela/curso_confirmar_eliminacion.html'):
    curso=Curso.objects.get(id=pk)
    if request.method=='POST':
        curso.delete()
        return redirect('cursos')
    else:
        dato={'form':curso}
        return render(request,template_name,dato)

def eliminar_turno(request,pk,template_name='escuela/turno_confirmar_eliminacion.html'):
    turno=Turno.objects.get(nombre=pk)
    if request.method=='POST':
        turno.delete()
        return redirect('turnos')
    else:
        dato={'form':turno}
        return render(request,template_name,dato)

def eliminar_tiene(request,pk,template_name='escuela/tiene_confirmar_eliminacion.html'):
    tiene=Tiene.objects.get(nombre=pk)
    if request.method=='POST':
        tiene.delete()
        return redirect('tienen')
    else:
        dato={'form':tiene}
        return render(request,template_name,dato)

def eliminar_rinde(request,pk,template_name='escuela/rinde_confirmar_eliminacion.html'):
    rinde=Rinde.objects.get(nombre=pk)
    if request.method=='POST':
        rinde.delete()
        return redirect('rinden')
    else:
        dato={'form':rinde}
        return render(request,template_name,dato)

def eliminar_profesor(request,pk,template_name='escuela/profesor_confirmar_eliminacion.html'):
    profesor=Profesor.objects.get(num_reg=pk)
    if request.method=='POST':
        profesor.delete()
        return redirect('profesors')
    else:
        dato={'form':profesor}
        return render(request,template_name,dato)

def eliminar_dicta(request,pk,template_name='escuela/dicta_confirmar_eliminacion.html'):
    dicta=Dicta.objects.get(nombre=pk)
    if request.method=='POST':
        dicta.delete()
        return redirect('dictan')
    else:
        dato={'form':dicta}
        return render(request,template_name,dato)