from django.contrib import admin
from . import models
# Register your models here.

class estratomodel(admin.ModelAdmin):
    list_display = ('idEstrato','espesorEstrato', 'relacionPoisson', 'indiceDeComprension', 'pesoEspecifico','moduloElasticidad','relacionDeVacioInicial','presionDepreconsolidacion', 'indiceDeExpansibilidad','cohesionSuelo','friccionSuelo')
    ordering = ('idEstrato', )
    

admin.site.register(models.perfilGeotecnico,estratomodel),
admin.site.register(models.correlaciones),
admin.site.register(models.parametroSuelo),
admin.site.register(models.Observaciones),

