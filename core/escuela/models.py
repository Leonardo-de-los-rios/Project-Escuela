from django.db import models
from core.user.models import User

class Preceptor(models.Model):
    idPreceptor = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    num_cuil = models.CharField('N° de CUIT/CUIL', max_length=15, unique=True)
    num_doc = models.CharField('N° de documento', max_length=10, unique=True)
    nombre = models.CharField('Nombre/s', max_length=90)
    apellido = models.CharField('Apellido/s',max_length=90)
    fecha_nac = models.DateField('Fecha de nacimiento')
    edad = models.IntegerField(null=True, blank=True) # se calcula cuando se hace el listado de personas
    direccion = models.CharField('Calle y número', max_length=120)
    telefono = models.CharField('N° de teléfono', max_length=14)

    class Meta:
        verbose_name_plural = 'Preceptores'
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

class Aula(models.Model):
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

    idAula = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    año = models.IntegerField('Año', choices=AÑO_CHOICE) # se almacena como entero pero se muestra como select en el forms
    division = models.IntegerField('División', choices=DIVISION_CHOICE)
    preceptor = models.ForeignKey(Preceptor, on_delete=models.CASCADE, related_name='aula_preceptor')
    
    class Meta:
        ordering = ['año', 'division']

    def __str__(self):
        return f'{self.año}°  -  {self.division}°'

class Alumno(models.Model):
    num_reg = models.CharField('N° de Registro', max_length=6, primary_key=True)
    num_doc = models.CharField('N° de documento', max_length=10, unique=True)
    nombre = models.CharField('Nombre/s', max_length=90)
    apellido = models.CharField('Apellido/s',max_length=90)
    fecha_nac = models.DateField('Fecha de nacimiento')
    edad = models.IntegerField(null=True, blank=True) # se calcula cuando se hace el listado de personas
    direccion = models.CharField('Calle y número', max_length=120)
    telefono = models.CharField('N° de teléfono', max_length=14)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, related_name='alumno_curso')

    class Meta:
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f'{self.apellido}, {self.nombre} - {self.num_reg}'

class Materia(models.Model):
    codigo = models.IntegerField('Código', primary_key=True, unique=True)
    nombre = models.CharField('Nombre', max_length=90)
    cant_horas = models.IntegerField('Cantidad de Horas')

    class Meta:
        ordering = ['codigo']

    def __str__(self):
        return f'{self.codigo} - {self.nombre}'

class Curso(models.Model):
    DIA_CHOICE = (
    (1, 'Lunes'),
    (2, 'Martes'),
    (3, 'Miércoles'),
    (4, 'Jueves'),
    (5, 'Viernes'),
    (6, 'Sábado'),
    (7, 'Domingo')
    )

    materia_codigo = models.ForeignKey(Materia,on_delete=models.CASCADE,related_name='curso_materia')
    aula_idAula = models.ForeignKey(Aula,on_delete=models.CASCADE,related_name='curso_aula')
    dia_clase = models.IntegerField('Día de Clase', choices=DIA_CHOICE)

    class Meta:
        ordering = ['dia_clase']

    def __str__(self):
        return f'{self.materia_codigo} - {self.aula_idAula}'

class Turno(models.Model):
    idTurno = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nombre = models.CharField('Turno', max_length=45)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre}'

class Tiene(models.Model):
    aula_idAula = models.ForeignKey(Aula,on_delete=models.CASCADE,related_name='tiene_aula')
    turno_idturno = models.ForeignKey(Turno,on_delete=models.CASCADE,related_name='tiene_turno_idturno')
    hora_ingreso = models.CharField('Hora de Entrada', max_length=45)
    hora_egreso = models.CharField('Hora de Salida', max_length=45)

    class Meta:
        verbose_name_plural = 'Tienen'
        ordering = ['aula_idAula', 'hora_ingreso', 'hora_egreso']

    def __str__(self):
        return f'{self.aula_idAula} - {self.turno_idTurno}'

class Rinde(models.Model):
    materia_codigo = models.ForeignKey(Materia,on_delete=models.CASCADE,related_name='rinde_materia')
    alumno_nro_registro = models.ForeignKey(Alumno,on_delete=models.CASCADE,related_name='rinde_alumno')
    nota_1 = models.IntegerField('Nota N° 1')
    nota_2 = models.IntegerField('Nota N° 2')
    nota_3 = models.IntegerField('Nota N° 3')

    class Meta:
        verbose_name_plural = 'Rinden'
        ordering = ['materia_codigo', 'alumno_nro_registro']

    def __str__(self):
        return f'{self.aula_idAula} - {self.turno_idTurno}'

class Profesor(models.Model):
    idProfesor = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    num_cuil = models.CharField('N° de CUIT/CUIL', max_length=15, unique=True)
    num_doc = models.CharField('N° de documento', max_length=10, unique=True)
    nombre = models.CharField('Nombre/s', max_length=90)
    apellido = models.CharField('Apellido/s',max_length=90)
    fecha_nac = models.DateField('Fecha de nacimiento')
    edad = models.IntegerField(null=True, blank=True) # se calcula cuando se hace el listado de personas
    direccion = models.CharField('Calle y número', max_length=120)
    telefono = models.CharField('N° de teléfono', max_length=14)

    class Meta:
        verbose_name_plural = 'Profesores'
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

class Dicta(models.Model):
    profesor_id_profesor = models.ForeignKey(Profesor,on_delete=models.CASCADE,related_name='dicat_profesor')
    materia_codigo = models.ForeignKey(Materia,on_delete=models.CASCADE,related_name='dicta_materia')
    cargo = models.CharField('Cargo', max_length=85)

    class Meta:
        verbose_name_plural = 'Dictan'
        ordering = ['profesor_id_profesor', 'materia_codigo', 'cargo']

    def __str__(self):
        return f'{self.cargo}'