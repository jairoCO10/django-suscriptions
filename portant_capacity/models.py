from django.db import models
from projects.models import home1
# Create your models here.


class servicios(models.Model):
    idproyecto = models.ForeignKey(home1, null=False, blank=False, on_delete=models.CASCADE)
    joints   =  models.CharField(primary_key=True, max_length=10, editable=True)
    fuerza1  = models.DecimalField(max_digits=10, decimal_places=3)
    fuerza2  = models.DecimalField(max_digits=10, decimal_places=3)
    fuerza3  = models.DecimalField(max_digits=10, decimal_places=3)
    momento1 = models.DecimalField(max_digits=10, decimal_places=3)
    momento2 = models.DecimalField(max_digits=10, decimal_places=3)
    momento3 = models.DecimalField(max_digits=10, decimal_places=3)
    def __str__(self):
            return self.joints

class dimensionesPersonalizadas(models.Model):
    idproyecto = models.ForeignKey(home1, null=False, blank=False, on_delete=models.CASCADE)
    
    joints= models.ForeignKey(servicios,null=False,blank=False, on_delete=models.CASCADE)
    bpersonalizado=models.DecimalField(max_digits=10,decimal_places=3)
    lpersonalizado=models.DecimalField(max_digits=10,decimal_places=3)

    
CHOICES3 = [
    ('mayorBL','MayorBL'),
    ('menorBL','MayorBL'),
    
]

CHOICES2 = [
    ('si','SI'),
    ('no','NO'),
    
]



CHOICES1 = [
    ('hansen','Hansen'),
    ('vesic','Vesic'),
    
]


class datosIniciales(models.Model):
    idproyecto = models.ForeignKey(home1, null=False, blank=False, on_delete=models.CASCADE)
    nivelFeatico = models.DecimalField(max_digits=10, decimal_places=4)    
    profundidadCimentacion = models.DecimalField(max_digits=10, decimal_places=4)
    factorResistencia = models.DecimalField(max_digits=10, decimal_places=4)
    modelo=models.CharField(choices=CHOICES1,max_length=32)
    asentamimientoMaximo = models.DecimalField(max_digits=10,decimal_places=3)
    OCR=models.CharField(choices=CHOICES2,max_length=32)
    h=models.DecimalField(max_digits=10,decimal_places=3)
    aumentoB = models.DecimalField(max_digits=10, decimal_places=4)
    cifrasDecimales = models.IntegerField()
    salto=models.DecimalField(max_digits=10,decimal_places=3)
    personalizado=models.CharField(choices=CHOICES2,max_length=32)
    

