from django.contrib.auth.models import AbstractUser
from django.db import models

class TipoUsuario(models.Model):
    nombre = models.CharField('Tipo de Usuario',max_length=100,primary_key=True)

    def __str__(self):
        return f'{self.nombre}'

class User(AbstractUser):
    tipo = models.ForeignKey(TipoUsuario,related_name='user_tipo_usuario' ,on_delete=models.CASCADE,null=True)

    def get_tipo(self):
        return self.tipo.nombre