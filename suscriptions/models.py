from django.db import models

# Create your models here.



CHOICES = [
    ('menbresia1','logger'),
    ('menbresia2','users'),
    ('menbresia3','pro'),
    ]

class membresia (models.Model):
    idmembresia = models.IntegerField(primary_key=True,auto_created=True)
    tipomenbresia = models.CharField(choices=CHOICES, max_length=40)
    