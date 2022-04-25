from django.contrib import admin

# Register your models here.
from . import models



class adminmodelhome(admin.ModelAdmin):
    list_display = ('nombreProyecto','ciudadProyecto','fecha','ingenieroEncargado')
    ordering = ('nombreProyecto', 'fecha', )
    search_field =('nombreProyecto',)
    list_filter = ('fecha','nombreProyecto')


admin.site.register(models.home1, adminmodelhome),
