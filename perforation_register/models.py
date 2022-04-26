from django.db import models
from projects.models import home1
# Create your models here.

class Sondeo(models.Model):
    idSondeos = models.CharField(primary_key=True, max_length=9, editable=True)
    idproyecto = models.ForeignKey(home1, null=False, blank=False, on_delete=models.CASCADE)
    coordenadas = models.CharField(max_length=100)
    horaInicial = models.CharField(max_length=30)
    horafinal = models.CharField(max_length=40)
    absisa = models.CharField(max_length=40)
    def __str__(self):
        return self.idSondeos
    

class registroDePerforacion(models.Model): 
    idSondeos = models.ForeignKey(Sondeo,null=False,blank=False, on_delete=models.CASCADE)
    idMuestra = models.CharField(max_length=30)
    profundidadInicial=models.CharField(max_length=20)
    profundidadFinal = models.CharField(max_length=20)
    spt6 =models.CharField(max_length=4)
    spt12=models.CharField(max_length=5)
    spt18=models.CharField(max_length=10)
    tipoMuestra= models.CharField(max_length=23)
    clasificacionesPrimarias = models.CharField(max_length=250)
    def __str__(self):
        return self.idMuestra


