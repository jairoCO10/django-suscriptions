from django.db import models
from perforation_register.models import registroDePerforacion

# Create your models here.



class laboratory(models.Model):
    recovery =models.CharField(max_length=20) # recobro
    wPercentage = models.CharField(max_length=20)#wporcentaje
    waterLimit = models.CharField(max_length=20)
    wp = models.CharField(max_length=20)
    plasticityIndex =models.CharField(max_length=20)
    usc = models.CharField(max_length=20)
    classificationAashto = models.CharField(max_length=20)
    volumen = models.CharField(max_length=20)
    percentageGravas = models.CharField(max_length=20)
    percentageArenas = models.CharField(max_length=20)
    percentageFinos  = models.CharField(max_length=20)  
    idMuestra = models.ForeignKey(registroDePerforacion,null=False,blank=False, on_delete=models.CASCADE)
    