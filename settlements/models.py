from django.db import models
from projects.models import home1
# Create your models here. 

CHOICES1 = [
    ('hansen','HANSEN'),
    ('vesic','VESIC'),
    ('richards','RICHARDS'),
    ('soubra','SOUBRA'),
    ('sarma','SARMA'),
    ('budhu','BUDHU'),
]


CHOICES2 = [
    ('si','SI'),
    ('no','NO'),
    
]

CHOICES3 = [
    ('mayorBL','MayorBL'),
    ('menorBL','MayorBL'),
    
]

CHOICES4 = [
    ('CL','Converse-Labarre'),
    ('GA','Group Action'),
    ('SK','Seiler Keeney 1944'),
    ('Min','Minimo'),
    ('Max','Maximo'),
    ('Med','Mediano'),
    ('Media','Promedio'),
    
]

CHOICES5 = [
    ('Pilotes','pilotes'),
    ('Barretes','barretes'),
    ('Caissons','caissons'),
    
]

CHOICES6= [
    ('1','1'),
    ('0','0'),
    
    
]

CHOICES7= [
    ('Concreto','concreto'),
    ('Madera','madera'),
    ('Acero','acero'),
    
    
]

CHOICES8= [
    ('Friccion','friccion'),
    ('Punta','punta'),
    ('Minimo','mínimo'),
    ('Maximo','máximo'), 
    ('Promedio','promedio'), 
    
]


class diferenciales(models.Model):
    joints = models.IntegerField(verbose_name='JOINTS')
    vecinos = models.IntegerField()
    idproyecto = models.ForeignKey(home1, null=False, blank=False, on_delete=models.CASCADE)
    distancias = models.DecimalField(max_digits=10,decimal_places=3)
    criterioDiferencial=models.DecimalField(max_digits=10, decimal_places=4)

class preciosUnitarios(models.Model):
    idproyecto = models.ForeignKey(home1, null=False, blank=False, on_delete=models.CASCADE)
    precioExc=models.DecimalField(max_digits=10,decimal_places=3)
    precioConcZ=models.DecimalField(max_digits=10,decimal_places=3)
    precioConcP=models.DecimalField(max_digits=10,decimal_places=3)
    precioRelleno=models.DecimalField(max_digits=10,decimal_places=3)
    preciosolado=models.DecimalField(max_digits=10,decimal_places=3)
    precioAceroZapata=models.DecimalField(max_digits=10,decimal_places=3)
    precioAceroPedestal=models.DecimalField(max_digits=10,decimal_places=3)

class datosPrimary(models.Model):

    idproyecto = models.ForeignKey(home1, null=False, blank=False, on_delete=models.CASCADE)
    espesorZapata=models.DecimalField(max_digits=10,decimal_places=3)
    espesorSolado=models.DecimalField(max_digits=10,decimal_places=3)
    espesorPedestal=models.DecimalField(max_digits=10,decimal_places=3)
    condicion=models.CharField(choices=CHOICES3,max_length=32)
    cuantiaAceroZapata=models.DecimalField(max_digits=10,decimal_places=3)
    cuantiaAceroPedestal=models.DecimalField(max_digits=10,decimal_places=3)

class eficiencia(models.Model):
    idproyecto = models.ForeignKey(home1, null=False, blank=False, on_delete=models.CASCADE)
    autor=models.CharField(choices=CHOICES4,max_length=32)    
    sepx=models.DecimalField(max_digits=10, decimal_places=3)
    sepy=models.DecimalField(max_digits=10, decimal_places=3)
    offsetX=models.DecimalField(max_digits=10, decimal_places=3)
    offsetY=models.DecimalField(max_digits=10, decimal_places=3)

class precioMaterialCimentacionProfunda(models.Model):
    idproyecto = models.ForeignKey(home1, null=False, blank=False, on_delete=models.CASCADE)
    
    Madera=models.DecimalField(max_digits=10, decimal_places=3)
    Acero=models.DecimalField(max_digits=10, decimal_places=3)

class datosConsProfunda(models.Model):
    idproyecto = models.ForeignKey(home1, null=False, blank=False, on_delete=models.CASCADE)
    
    Bdado=models.DecimalField(max_digits=10, decimal_places=3,verbose_name='Lado horizontal del dado')
    Ldado=models.DecimalField(max_digits=10, decimal_places=3,verbose_name='Lado vertical del dado')
    H=models.DecimalField(max_digits=10, decimal_places=3,verbose_name='H (en centímetros)')
    Amax=models.DecimalField(max_digits=10, decimal_places=3,verbose_name='Asentamiento Máximo')
    CargaMax=models.DecimalField(max_digits=10, decimal_places=3,verbose_name='Carga Máxima')

class rangoDimensiones(models.Model):
    idproyecto = models.ForeignKey(home1, null=False, blank=False, on_delete=models.CASCADE)
    
    Bmin=models.DecimalField(max_digits=10, decimal_places=3,verbose_name='B mínimo')
    Bmax=models.DecimalField(max_digits=10, decimal_places=3,verbose_name='B máximo')
    each=models.DecimalField(max_digits=10, decimal_places=3)

class relacionCarga(models.Model):
    idproyecto = models.ForeignKey(home1, null=False, blank=False, on_delete=models.CASCADE)
    
    rbl=models.DecimalField(max_digits=10, decimal_places=3,verbose_name='Relación entre B y L')
    carga=models.DecimalField(max_digits=10, decimal_places=3,verbose_name='Carga F3')

class geometriaCimentacionProfunda(models.Model):
    idproyecto = models.ForeignKey(home1, null=False, blank=False, on_delete=models.CASCADE)
    
    idDado = models.CharField(primary_key=True, max_length=10, editable=True)
    diametroI = models.DecimalField(max_digits=10, decimal_places=3)
    diametrof=models.DecimalField(max_digits=10, decimal_places=3)
    material = models.CharField(choices=CHOICES7,max_length=32)
    resistenciaConcreto  = models.DecimalField(max_digits=10, decimal_places=3)
    Carga=models.DecimalField(max_digits=10, decimal_places=3)
    Ep=models.DecimalField(max_digits=10, decimal_places=3)
    Eb=models.DecimalField(max_digits=10, decimal_places=3)
    ModuloMaterial=models.DecimalField(max_digits=10, decimal_places=3)
    tipoElemento=models.CharField(choices=CHOICES5,max_length=32)
    transCarga = models.CharField(choices=CHOICES8,max_length=32)
    B=models.DecimalField(max_digits=10, decimal_places=3,verbose_name='B: 0.6')
    R=models.DecimalField(max_digits=10, decimal_places=3,verbose_name='H: 2')
    peso=models.CharField(choices=CHOICES6,max_length=32)
    prof=models.DecimalField(max_digits=10, decimal_places=3,verbose_name='Profundidad cimentacion')
    def __str__(self):
            return self.idDado
