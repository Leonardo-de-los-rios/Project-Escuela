# Generated by Django 4.0.2 on 2022-06-14 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('escuela', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='persona_usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='curso',
            name='turno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='curso_turno', to='escuela.turno'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alumno_curso', to='escuela.curso'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alumno_persona', to='escuela.persona'),
        ),
    ]
