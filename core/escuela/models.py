from django.db import models
from core.user.models import User

class Genero(models.Model):
    nombre = models.CharField('Género', max_length=100, primary_key=True)

    def __str__(self):
        return f'{self.nombre}'

class Persona(models.Model):
    num_cuit = models.CharField('N° de CUIT/CUIL', max_length=15, primary_key=True, unique=True)
    num_doc = models.CharField('N° de documento', max_length=10)
    apellido = models.CharField('Apellido/s',max_length=90)
    nombre = models.CharField('Nombre/s', max_length=90)
    fecha_nac = models.DateField('Fecha de nacimiento')
    edad = models.IntegerField(null=True, blank=True) # se calcula cuando se hace el listado de personas
    direccion = models.CharField('Calle y número', max_length=120)
    telefono = models.CharField('N° de teléfono', max_length=14)
    email = models.EmailField('E-mail', null=True, blank=True, unique=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='persona_genero') # objetos que acceden a una clase foranea
    usuario = models.OneToOneField(User, related_name='persona_usuario',on_delete=models.CASCADE)

    class Meta:
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

class Turno(models.Model):
    nombre = models.CharField('Turno', max_length=20, primary_key=True)

    def __str__(self):
        return f'{self.nombre}'

class Curso(models.Model):
    AÑO_CHOICE = (
    (1, 'Primero'),
    (2, 'Segundo'),
    (3, 'Tercero'),
    (4, 'Cuarto'),
    (5, 'Quinto'),
    (6, 'Sexto'),
    )

    DIVISION_CHOICE = (
    (1, 'Primera'),
    (2, 'Segunda'),
    (3, 'Tercera'),
    (4, 'Cuarta'),
    (5, 'Quinta'),
    (6, 'Sexta'),
    )

    año = models.IntegerField('Año', choices=AÑO_CHOICE) # se almacena como entero pero se muestra como select en el forms
    division = models.IntegerField('División', choices=DIVISION_CHOICE)
    turno = models.ForeignKey(Turno, on_delete=models.PROTECT, related_name='curso_turno')
    cant_alumnos = models.IntegerField('Cantidad de Alumnos')
    #materia = models.ForeignKey(Materia, on_delete=models.PROTECT, related_name='curso_materia')
    
    class Meta:
        ordering = ['año', 'division']

    def __str__(self):
        return f'{self.año}°  -  {self.division}°'

class Alumno(models.Model):
    num_reg = models.CharField('N° de Registro', max_length=6, primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='alumno_persona')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='alumno_curso')

    class Meta:
        ordering = ['num_reg']

    def __str__(self):
        return f'{self.persona.apellido}, {self.persona.nombre}'