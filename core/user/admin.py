from django.contrib import admin

# Register your models here.

from core.user.models import TipoUsuario,User

admin.site.register(User)
admin.site.register(TipoUsuario)