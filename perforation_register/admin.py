from django.contrib import admin

# Register your models here.

from . import models




class registerPerforarionmodel(admin.ModelAdmin):
    list_display = ('idSondeos', 'idMuestra', 'profundidadInicial', 'profundidadFinal', 'spt6','spt12','spt18','tipoMuestra', 'clasificacionesPrimarias')
    ordering = ('idSondeos', )
    list_filter = ('idSondeos',)
    search_field =('idMuestra',)


class adminmodelsondeos(admin.ModelAdmin):
    list_display = ('idproyecto','idSondeos','coordenadas','horaInicial','horafinal','absisa')
    ordering = ('idSondeos', )
    search_field =('idSondeos',)
    list_filter = ('idproyecto',)
        

admin.site.register(models.Sondeo, adminmodelsondeos),
admin.site.register(models.registroDePerforacion, registerPerforarionmodel )
