from django.db import models

# Create your models here.
from users.models import User
from suscriptions.models import membresia
from django.core.validators import MinValueValidator, MaxValueValidator



class home1(models.Model):
    nombreProyecto= models.CharField(primary_key=True, max_length=60, editable=True) 
    ciudadProyecto = models.CharField(max_length=40) 
    fecha= models.DateField(max_length=40)
    ingenieroEncargado = models.CharField(max_length=40)
    iduser = models.ForeignKey(User, on_delete=models.CASCADE)
    idmembresia = models.ForeignKey(membresia, on_delete=models.CASCADE)
    cantidad = models.PositiveBigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    def __str__(self):
        return self.nombreProyecto


