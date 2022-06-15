from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',views.index,name='index'),
    #path('<str:username>/',views.index,name='index'),
    path('register/', views.register, name='register'),
	path('login/', LoginView.as_view(template_name='escuela/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='escuela/logout.html'), name='logout'),
    path('nuevo-tipo-usuario/',views.nuevo_tipo_usuario,name='nuevo_tipo_usuario'),
    path('nuevo-genero/',views.nuevo_genero,name='nuevo_genero'),
    path('nueva-persona/',views.nueva_persona,name='nueva_persona'),
    path('nuevo-turno/',views.nuevo_turno,name='nuevo_turno'),
    path('nuevo-curso/',views.nuevo_curso,name='nuevo_curso'),
    path('nuevo-alumno/',views.nuevo_alumno,name='nuevo_alumno'),
    path('tipos-usuario/',views.listar_tipos_usuario,name='tipos_usuario'),
    path('usuarios/',views.listar_usuarios,name='usuarios'),
    path('generos/',views.listar_generos,name='generos'),
    path('personas/',views.listar_personas,name='personas'),
    path('turnos/',views.listar_turnos,name='turnos'),
    path('cursos/',views.listar_cursos,name='cursos'),
    path('alumnos/',views.listar_alumnos,name='alumnos'),
    path('modificar-persona/<str:pk>', views.modificar_persona, name='modificar_persona'),
    path('eliminar-persona/<str:pk>', views.eliminar_persona, name='eliminar_persona'),
]
