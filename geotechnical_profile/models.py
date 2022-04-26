from django.db import models
from projects.models import home1
# Create your models here.


class correlaciones(models.Model):
    idproyecto = models.ForeignKey(home1, null=False, blank=False, on_delete=models.CASCADE)
    comprensibilidad = models.CharField(max_length=30)
    resistenciaCorte= models.CharField(max_length=30)
    


class parametroSuelo(models.Model):
    idproyecto = models.ForeignKey(home1, null=False, blank=False, on_delete=models.CASCADE)
    compresibilidad = models.CharField(max_length=30)
    resistencia = models.CharField(max_length=30)
    elasticidad = models.CharField(max_length=30)
    porcentajeExpansion = models.CharField(max_length=50)
    promedioExpansion = models.CharField(max_length=40)
    pesoEspecificosolido = models.CharField(max_length=50)
    pesoEspecificoagua = models.CharField(max_length=50)
    resistenciaDrenada = models.CharField(max_length=50)
    resistencianoDrenada = models.CharField(max_length=40) 
    gravedadEspecifica = models.CharField(max_length=50) 
   
class Observaciones(models.Model):
    idproyecto = models.ForeignKey(home1, null=False, blank=False, on_delete=models.CASCADE)
    resumen = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    cantidadMuestras = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=40)
    firmas = models.CharField(max_length=40)


class perfilGeotecnico(models.Model):
    idproyecto = models.ForeignKey(home1, null=False, blank=False, on_delete=models.CASCADE)
    idEstrato=models.CharField(primary_key=True, max_length=10, editable=True)
    espesorEstrato = models.DecimalField(max_digits=10, decimal_places=3,verbose_name='Espesor')
    relacionPoisson = models.DecimalField(max_digits=10, decimal_places=3)
    indiceDeComprension = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Cc')
    pesoEspecifico = models.DecimalField(max_digits=10, decimal_places=3)
    moduloElasticidad =models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Es')
    relacionDeVacioInicial= models.DecimalField(max_digits=10, decimal_places=3, verbose_name='e0')
    presionDepreconsolidacion =  models.DecimalField(max_digits=10, decimal_places=3,verbose_name='Pc')
    indiceDeExpansibilidad=models.DecimalField(max_digits=10, decimal_places=3,verbose_name='Cs')
    cohesionSuelo = models.DecimalField(max_digits=10, decimal_places=4,verbose_name='Cohesion')
    friccionSuelo = models.DecimalField(max_digits=10, decimal_places=4,verbose_name='Friccion')


