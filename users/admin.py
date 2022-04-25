from django.contrib import admin
from . import models
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)
    

class usermodel(admin.ModelAdmin):
    list_display = ('email', 'name', 'lastName', 'dni', 'cellPhone','is_admin')
    list_filter = ('email', 'dni','is_admin')
    search_fields = ('dni','email')
    list_editable=('name','lastName','dni','cellPhone','is_admin',)
   

admin.site.register(models.User, UserAdmin,)
# # admin.site.register(models.Organizacion)
# admin.site.register(models.Usuarios,usermodel)
# # admin.site.register(models.laboratorista)
