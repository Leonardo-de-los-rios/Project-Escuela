# Generated by Django 4.0.2 on 2022-06-25 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('num_reg', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='N° de Registro')),
                ('num_doc', models.CharField(max_length=10, unique=True, verbose_name='N° de documento')),
                ('nombre', models.CharField(max_length=90, verbose_name='Nombre/s')),
                ('apellido', models.CharField(max_length=90, verbose_name='Apellido/s')),
                ('fecha_nac', models.DateField(verbose_name='Fecha de nacimiento')),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('direccion', models.CharField(max_length=120, verbose_name='Calle y número')),
                ('telefono', models.CharField(max_length=14, verbose_name='N° de teléfono')),
            ],
            options={
                'ordering': ['apellido', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('idAula', models.AutoField(primary_key=True, serialize=False)),
                ('año', models.IntegerField(choices=[(1, 'Primero'), (2, 'Segundo'), (3, 'Tercero'), (4, 'Cuarto'), (5, 'Quinto'), (6, 'Sexto')], verbose_name='Año')),
                ('division', models.IntegerField(choices=[(1, 'Primera'), (2, 'Segunda'), (3, 'Tercera'), (4, 'Cuarta'), (5, 'Quinta'), (6, 'Sexta')], verbose_name='División')),
            ],
            options={
                'ordering': ['año', 'division'],
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Código')),
                ('nombre', models.CharField(max_length=90, verbose_name='Nombre')),
                ('cant_horas', models.IntegerField(verbose_name='Cantidad de Horas')),
            ],
            options={
                'ordering': ['codigo'],
            },
        ),
        migrations.CreateModel(
            name='Preceptor',
            fields=[
                ('idPreceptor', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('num_cuil', models.CharField(max_length=15, unique=True, verbose_name='N° de CUIT/CUIL')),
                ('num_doc', models.CharField(max_length=10, unique=True, verbose_name='N° de documento')),
                ('nombre', models.CharField(max_length=90, verbose_name='Nombre/s')),
                ('apellido', models.CharField(max_length=90, verbose_name='Apellido/s')),
                ('fecha_nac', models.DateField(verbose_name='Fecha de nacimiento')),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('direccion', models.CharField(max_length=120, verbose_name='Calle y número')),
                ('telefono', models.CharField(max_length=14, verbose_name='N° de teléfono')),
            ],
            options={
                'ordering': ['apellido', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('idProfesor', models.AutoField(primary_key=True, serialize=False)),
                ('num_cuil', models.CharField(max_length=15, unique=True, verbose_name='N° de CUIT/CUIL')),
                ('num_doc', models.CharField(max_length=10, unique=True, verbose_name='N° de documento')),
                ('nombre', models.CharField(max_length=90, verbose_name='Nombre/s')),
                ('apellido', models.CharField(max_length=90, verbose_name='Apellido/s')),
                ('fecha_nac', models.DateField(verbose_name='Fecha de nacimiento')),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('direccion', models.CharField(max_length=120, verbose_name='Calle y número')),
                ('telefono', models.CharField(max_length=14, verbose_name='N° de teléfono')),
            ],
            options={
                'ordering': ['apellido', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('idTurno', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45, verbose_name='Turno')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Tiene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_ingreso', models.CharField(max_length=45, verbose_name='Hora de Entrada')),
                ('hora_egreso', models.CharField(max_length=45, verbose_name='Hora de Salida')),
                ('aula_idAula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tiene_aula', to='escuela.aula')),
                ('turno_idturno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tiene_turno_idturno', to='escuela.turno')),
            ],
            options={
                'ordering': ['aula_idAula', 'hora_ingreso', 'hora_egreso'],
            },
        ),
        migrations.CreateModel(
            name='Rinde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota_1', models.IntegerField(verbose_name='Nota N° 1')),
                ('nota_2', models.IntegerField(verbose_name='Nota N° 2')),
                ('nota_3', models.IntegerField(verbose_name='Nota N° 3')),
                ('alumno_nro_registro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rinde_alumno', to='escuela.alumno')),
                ('materia_codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rinde_materia', to='escuela.materia')),
            ],
            options={
                'ordering': ['materia_codigo', 'alumno_nro_registro'],
            },
        ),
        migrations.CreateModel(
            name='Dicta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=85, verbose_name='Cargo')),
                ('materia_codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dicta_materia', to='escuela.materia')),
                ('profesor_id_profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dicat_profesor', to='escuela.profesor')),
            ],
            options={
                'ordering': ['profesor_id_profesor', 'materia_codigo', 'cargo'],
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_clase', models.IntegerField(choices=[(1, 'Lunes'), (2, 'Martes'), (3, 'Miércoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sábado'), (7, 'Domingo')], verbose_name='Día de Clase')),
                ('aula_idAula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curso_aula', to='escuela.aula')),
                ('materia_codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curso_materia', to='escuela.materia')),
            ],
            options={
                'ordering': ['dia_clase'],
            },
        ),
        migrations.AddField(
            model_name='aula',
            name='preceptor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aula_preceptor', to='escuela.preceptor'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='aula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alumno_curso', to='escuela.aula'),
        ),
    ]
