from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from Apps.seguridad.usuario.models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    pass

# Register your models here.
