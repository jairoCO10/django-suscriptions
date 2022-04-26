from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.
from .models import servicios,dimensionesPersonalizadas,datosIniciales
from rest_framework import viewsets
from .serializers import DatosinicialesSerializer,dimesionesSerializer,serviciosSerializer
from geotechnical_profile.models import perfilGeotecnico
import pandas as pd
import numpy as np
import math
class datosinicialesViewSet(viewsets.ModelViewSet):
    serializer_class = DatosinicialesSerializer
    queryset = datosIniciales.objects.all()
    def perform_create(self, serializer):
        serializer.save() 
    def get_queryset(self):
        return self.queryset.filter()


class serviciosViewSet(viewsets.ModelViewSet):
    serializer_class = serviciosSerializer
    queryset = servicios.objects.all()
    def perform_create(self, serializer):
        serializer.save() 
    def get_queryset(self):
        return self.queryset.filter()

class dimensionesViewSet(viewsets.ModelViewSet):
    serializer_class = dimesionesSerializer
    queryset = dimensionesPersonalizadas.objects.all()
    def perform_create(self, serializer):
        serializer.save() 
    def get_queryset(self):
        return self.queryset.filter()


#####################################################################

# def RichardsNg(kh,fr):
#     ii = kh
#     x =[0,0.1,0.2,0.3,0.4,0.5,0.6]
#     jj =fr
#     y =[20,25,30,35,40] 
#     xy=np.zeros((7, 5))

#     xy[0, 0] = 7
#     xy[1, 0] = 6.5
#     xy[2, 0] = 4
#     xy[3, 0] = 1
#     xy[4, 0] = 1
#     xy[5, 0] = 1
#     xy[6, 0] = 1

#     xy[0, 1] = 11
#     xy[1, 1] = 9
#     xy[2, 1] = 7
#     xy[3, 1] = 4
#     xy[4, 1] = 1
#     xy[5, 1] = 1
#     xy[6, 1] = 1

#     xy[0, 2] = 30
#     xy[1, 2] = 22.5
#     xy[2, 2] = 12
#     xy[3, 2] = 8
#     xy[4, 2] = 4.5
#     xy[5, 2] = 1.2
#     xy[6, 2] = 1.2

#     xy[0, 3] = 67
#     xy[1, 3] = 45
#     xy[2, 3] = 38
#     xy[3, 3] = 28
#     xy[4, 3] = 10
#     xy[5, 3] = 4.5
#     xy[6, 3] = 1.2

#     xy[0, 4] = 100
#     xy[1, 4] = 80
#     xy[2, 4] = 68
#     xy[3, 4] = 46
#     xy[4, 4] = 30
#     xy[5, 4] = 12
#     xy[6, 4] = 8

#     for s in range(len(x)):
#         if x[s]>ii:
#             i=s
#             break
        
        
#     refi='i' in locals()
#     if refi==False:
#         i=len(x)-1
    
#     for s in range(len(y)):
#         if y[s]>jj:
#             j=s
#             break
        
        
#     refj='j' in locals()
#     if refj==False:
#         j=len(y)-1
    

#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i - 1, j - 1]
#     y2 = xy[i - 1, j]
#     y3 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i, j - 1]
#     y2 = xy[i, j]
#     y4 = (y2 - y1)/(x2 - x1) * (jj - x2) + y2
#     NgE = (y4 - y3)/(x[i] - x[i - 1])*(ii - x[i]) + y4
    
#     if NgE<1:
#         NgE=1
#     return  NgE

# # print(RichardsNg(0.4,20))

# def SarmaNg(kh,fr):
#     ii = kh
#     x =[0,0.1,0.2,0.3,0.4,0.5,0.6]
#     jj =fr
#     y =[20,25,30,35,40] 
#     xy=np.zeros((7, 5))

#     xy[0, 0] = 6
#     xy[1, 0] = 5
#     xy[2, 0] = 1.5
#     xy[3, 0] = 1
#     xy[4, 0] = 1
#     xy[5, 0] = 1
#     xy[6, 0] = 1

#     xy[0, 1] = 10
#     xy[1, 1] = 8
#     xy[2, 1] = 6.5
#     xy[3, 1] = 2
#     xy[4, 1] = 1
#     xy[5, 1] = 1
#     xy[6, 1] = 1

#     xy[0, 2] = 30
#     xy[1, 2] = 22
#     xy[2, 2] = 11.5
#     xy[3, 2] = 8
#     xy[4, 2] = 4
#     xy[5, 2] = 1
#     xy[6, 2] = 1

#     xy[0, 3] = 67
#     xy[1, 3] = 45
#     xy[2, 3] = 38
#     xy[3, 3] = 28
#     xy[4, 3] = 9
#     xy[5, 3] = 4.5
#     xy[6, 3] = 1.5

#     xy[0, 4] = 200
#     xy[1, 4] = 90
#     xy[2, 4] = 78
#     xy[3, 4] = 56
#     xy[4, 4] = 40
#     xy[5, 4] = 22
#     xy[6, 4] = 8

#     for s in range(len(x)):
#         if x[s]>ii:
#             i=s
#             break
        
        
#     refi='i' in locals()
#     if refi==False:
#         i=len(x)-1
    
#     for s in range(len(y)):
#         if y[s]>jj:
#             j=s
#             break
        
        
#     refj='j' in locals()
#     if refj==False:
#         j=len(y)-1
    

#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i - 1, j - 1]
#     y2 = xy[i - 1, j]
#     y3 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i, j - 1]
#     y2 = xy[i, j]
#     y4 = (y2 - y1)/(x2 - x1) * (jj - x2) + y2
#     NgE = (y4 - y3)/(x[i] - x[i - 1])*(ii - x[i]) + y4
    
#     if NgE<1:
#         NgE=1
#     return  NgE



# def SoubraNg(kh,fr):
#     ii = kh
#     x =[0,0.1,0.2,0.3,0.4,0.5,0.6]
#     jj =fr
#     y =[20,25,30,35,40] 
#     xy=np.zeros((7, 5))

#     xy[0, 0] = 7
#     xy[1, 0] = 5.5
#     xy[2, 0] = 4
#     xy[3, 0] = 1
#     xy[4, 0] = 1
#     xy[5, 0] = 1
#     xy[6, 0] = 1

#     xy[0, 1] = 11
#     xy[1, 1] = 9
#     xy[2, 1] = 7
#     xy[3, 1] = 4
#     xy[4, 1] = 1
#     xy[5, 1] = 1
#     xy[6, 1] = 1

#     xy[0, 2] = 30
#     xy[1, 2] = 22.5
#     xy[2, 2] = 13
#     xy[3, 2] = 9
#     xy[4, 2] = 5.5
#     xy[5, 2] = 1.2
#     xy[6, 2] = 1.2

#     xy[0, 3] = 67
#     xy[1, 3] = 45
#     xy[2, 3] = 39
#     xy[3, 3] = 29
#     xy[4, 3] = 11
#     xy[5, 3] = 7
#     xy[6, 3] = 2

#     xy[0, 4] = 200
#     xy[1, 4] = 90
#     xy[2, 4] = 78
#     xy[3, 4] = 56
#     xy[4, 4] = 40
#     xy[5, 4] = 30
#     xy[6, 4] = 9

#     for s in range(len(x)):
#         if x[s]>ii:
#             i=s
#             break
        
        
#     refi='i' in locals()
#     if refi==False:
#         i=len(x)-1
    
#     for s in range(len(y)):
#         if y[s]>jj:
#             j=s
#             break
        
        
#     refj='j' in locals()
#     if refj==False:
#         j=len(y)-1
    

#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i - 1, j - 1]
#     y2 = xy[i - 1, j]
#     y3 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i, j - 1]
#     y2 = xy[i, j]
#     y4 = (y2 - y1)/(x2 - x1) * (jj - x2) + y2
#     NgE = (y4 - y3)/(x[i] - x[i - 1])*(ii - x[i]) + y4
    
#     if NgE<1:
#         NgE=1
#     return  NgE




# def SoubraNq(kh,fr):
#     ii = kh
#     x =[0,0.1,0.2,0.3,0.4,0.5,0.6]
#     jj =fr
#     y =[20,25,30,35,40] 
#     xy=np.zeros((7, 5))

#     xy[0, 0] = 7
#     xy[1, 0] = 6.5
#     xy[2, 0] = 5
#     xy[3, 0] = 4
#     xy[4, 0] = 1.6
#     xy[5, 0] = 1.6
#     xy[6, 0] = 1.6

#     xy[0, 1] = 11
#     xy[1, 1] = 9
#     xy[2, 1] = 8
#     xy[3, 1] = 6
#     xy[4, 1] = 4.5
#     xy[5, 1] = 1.9
#     xy[6, 1] = 1.8

#     xy[0, 2] = 22.5
#     xy[1, 2] = 20
#     xy[2, 2] = 12
#     xy[3, 2] = 10
#     xy[4, 2] = 8
#     xy[5, 2] = 4.5
#     xy[6, 2] = 2

#     xy[0, 3] = 50
#     xy[1, 3] = 45
#     xy[2, 3] = 35
#     xy[3, 3] = 30
#     xy[4, 3] = 22.55
#     xy[5, 3] = 10
#     xy[6, 3] = 6

#     xy[0, 4] = 67
#     xy[1, 4] = 60
#     xy[2, 4] = 55
#     xy[3, 4] = 50
#     xy[4, 4] = 47
#     xy[5, 4] = 30
#     xy[6, 4] = 15

#     for s in range(len(x)):
#         if x[s]>ii:
#             i=s
#             break
        
        
#     refi='i' in locals()
#     if refi==False:
#         i=len(x)-1
    
#     for s in range(len(y)):
#         if y[s]>jj:
#             j=s
#             break
        
        
#     refj='j' in locals()
#     if refj==False:
#         j=len(y)-1
    

#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i - 1, j - 1]
#     y2 = xy[i - 1, j]
#     y3 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i, j - 1]
#     y2 = xy[i, j]
#     y4 = (y2 - y1)/(x2 - x1) * (jj - x2) + y2
#     NqE = (y4 - y3)/(x[i] - x[i - 1])*(ii - x[i]) + y4
    
#     if NqE<1:
#         NqE=1
#     return  NqE





# def SarmaNq(kh,fr):
#     ii = kh
#     x =[0,0.1,0.2,0.3,0.4,0.5,0.6]
#     jj =fr
#     y =[20,25,30,35,40] 
#     xy=np.zeros((7, 5))

#     xy[0, 0] = 7
#     xy[1, 0] = 6.5
#     xy[2, 0] = 5
#     xy[3, 0] = 3.5
#     xy[4, 0] = 1.5
#     xy[5, 0] = 1
#     xy[6, 0] = 1

#     xy[0, 1] = 11
#     xy[1, 1] = 9
#     xy[2, 1] = 8
#     xy[3, 1] = 6
#     xy[4, 1] = 4.5
#     xy[5, 1] = 1.9
#     xy[6, 1] = 1

#     xy[0, 2] = 22.5
#     xy[1, 2] = 20
#     xy[2, 2] = 12
#     xy[3, 2] = 10
#     xy[4, 2] = 8
#     xy[5, 2] = 4.5
#     xy[6, 2] = 1

#     xy[0, 3] = 50
#     xy[1, 3] = 45
#     xy[2, 3] = 35
#     xy[3, 3] = 30
#     xy[4, 3] = 22.55
#     xy[5, 3] = 10
#     xy[6, 3] = 5

#     xy[0, 4] = 67
#     xy[1, 4] = 60
#     xy[2, 4] = 55
#     xy[3, 4] = 50
#     xy[4, 4] = 47
#     xy[5, 4] = 30
#     xy[6, 4] = 15

#     for s in range(len(x)):
#         if x[s]>ii:
#             i=s
#             break
        
        
#     refi='i' in locals()
#     if refi==False:
#         i=len(x)-1
    
#     for s in range(len(y)):
#         if y[s]>jj:
#             j=s
#             break
        
        
#     refj='j' in locals()
#     if refj==False:
#         j=len(y)-1
    

#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i - 1, j - 1]
#     y2 = xy[i - 1, j]
#     y3 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i, j - 1]
#     y2 = xy[i, j]
#     y4 = (y2 - y1)/(x2 - x1) * (jj - x2) + y2
#     NqE = (y4 - y3)/(x[i] - x[i - 1])*(ii - x[i]) + y4
    
#     if NqE<1:
#         NqE=1
#     return  NqE


# def RichardsNq(kh,fr):
#     ii = kh
#     x =[0,0.1,0.2,0.3,0.4,0.5,0.6]
#     jj =fr
#     y =[20,25,30,35,40] 
#     xy=np.zeros((7, 5))

#     xy[0, 0] = 6
#     xy[1, 0] = 5.5
#     xy[2, 0] = 4.5
#     xy[3, 0] = 3.5
#     xy[4, 0] = 1.7
#     xy[5, 0] = 1.7
#     xy[6, 0] = 1.7

#     xy[0, 1] = 11
#     xy[1, 1] = 9
#     xy[2, 1] = 8
#     xy[3, 1] = 6
#     xy[4, 1] = 4.5
#     xy[5, 1] = 1.9
#     xy[6, 1] = 1.8

#     xy[0, 2] = 22
#     xy[1, 2] = 19.5
#     xy[2, 2] = 11.5
#     xy[3, 2] = 9.5
#     xy[4, 2] = 7.5
#     xy[5, 2] = 4.5
#     xy[6, 2] = 2

#     xy[0, 3] = 50
#     xy[1, 3] = 45
#     xy[2, 3] = 35
#     xy[3, 3] = 30
#     xy[4, 3] = 22.55
#     xy[5, 3] = 10
#     xy[6, 3] = 6

#     xy[0, 4] = 67
#     xy[1, 4] = 60
#     xy[2, 4] = 55
#     xy[3, 4] = 50
#     xy[4, 4] = 47
#     xy[5, 4] = 30
#     xy[6, 4] = 15

#     for s in range(len(x)):
#         if x[s]>ii:
#             i=s
#             break
        
        
#     refi='i' in locals()
#     if refi==False:
#         i=len(x)-1
    
#     for s in range(len(y)):
#         if y[s]>jj:
#             j=s
#             break
        
        
#     refj='j' in locals()
#     if refj==False:
#         j=len(y)-1
    

#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i - 1, j - 1]
#     y2 = xy[i - 1, j]
#     y3 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i, j - 1]
#     y2 = xy[i, j]
#     y4 = (y2 - y1)/(x2 - x1) * (jj - x2) + y2
#     NqE = (y4 - y3)/(x[i] - x[i - 1])*(ii - x[i]) + y4
    
#     if NqE<1:
#         NqE=1
#     return  NqE


# def RichardsNc(kh,fr):
#     ii = kh
#     x =[0,0.1,0.2,0.3,0.4,0.5,0.6]
#     jj =fr
#     y =[20,25,30,35,40] 
#     xy=np.zeros((7, 5))

#     xy[0, 0] = 22
#     xy[1, 0] = 9
#     xy[2, 0] = 8
#     xy[3, 0] = 5
#     xy[4, 0] = 1
#     xy[5, 0] = 1
#     xy[6, 0] = 1

#     xy[0, 1] = 26
#     xy[1, 1] = 24
#     xy[2, 1] = 20
#     xy[3, 1] = 17
#     xy[4, 1] = 11
#     xy[5, 1] = 9
#     xy[6, 1] = 8

#     xy[0, 2] = 38
#     xy[1, 2] = 30
#     xy[2, 2] = 17
#     xy[3, 2] = 14
#     xy[4, 2] = 9
#     xy[5, 2] = 6
#     xy[6, 2] = 3

#     xy[0, 3] = 60
#     xy[1, 3] = 55
#     xy[2, 3] = 45
#     xy[3, 3] = 38
#     xy[4, 3] = 28
#     xy[5, 3] = 20
#     xy[6, 3] = 17

#     xy[0, 4] = 80
#     xy[1, 4] = 70
#     xy[2, 4] = 60
#     xy[3, 4] = 28
#     xy[4, 4] = 25
#     xy[5, 4] = 19
#     xy[6, 4] = 12

#     for s in range(len(x)):
#         if x[s]>ii:
#             i=s
#             break
        
        
#     refi='i' in locals()
#     if refi==False:
#         i=len(x)-1
    
#     for s in range(len(y)):
#         if y[s]>jj:
#             j=s
#             break
        
        
#     refj='j' in locals()
#     if refj==False:
#         j=len(y)-1
    

#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i - 1, j - 1]
#     y2 = xy[i - 1, j]
#     y3 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i, j - 1]
#     y2 = xy[i, j]
#     y4 = (y2 - y1)/(x2 - x1) * (jj - x2) + y2
#     Nc = (y4 - y3)/(x[i] - x[i - 1])*(ii - x[i]) + y4
    
#     if Nc<1:
#         Nc=1
#     return  Nc

# #######
# def SarmaNc(kh,fr):
#     ii = kh
#     x =[0,0.1,0.2,0.3,0.4,0.5,0.6]
#     jj =fr
#     y =[20,25,30,35,40] 
#     xy=np.zeros((7, 5))

#     xy[0, 0] = 22
#     xy[1, 0] = 17
#     xy[2, 0] = 11
#     xy[3, 0] = 9.5
#     xy[4, 0] = 8
#     xy[5, 0] = 7
#     xy[6, 0] = 6

#     xy[0, 1] = 38
#     xy[1, 1] = 30
#     xy[2, 1] = 25
#     xy[3, 1] = 22
#     xy[4, 1] = 11
#     xy[5, 1] = 10
#     xy[6, 1] = 9

#     xy[0, 2] = 40
#     xy[1, 2] = 38
#     xy[2, 2] = 35
#     xy[3, 2] = 30
#     xy[4, 2] = 23
#     xy[5, 2] = 20
#     xy[6, 2] = 12

#     xy[0, 3] = 67
#     xy[1, 3] = 60
#     xy[2, 3] = 55
#     xy[3, 3] = 45
#     xy[4, 3] = 38
#     xy[5, 3] = 30
#     xy[6, 3] = 22

#     xy[0, 4] = 79
#     xy[1, 4] = 71
#     xy[2, 4] = 65
#     xy[3, 4] = 60
#     xy[4, 4] = 25
#     xy[5, 4] = 19
#     xy[6, 4] = 12

#     for s in range(len(x)):
#         if x[s]>ii:
#             i=s
#             break
        
        
#     refi='i' in locals()
#     if refi==False:
#         i=len(x)-1
    
#     for s in range(len(y)):
#         if y[s]>jj:
#             j=s
#             break
        
        
#     refj='j' in locals()
#     if refj==False:
#         j=len(y)-1
    

#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i - 1, j - 1]
#     y2 = xy[i - 1, j]
#     y3 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i, j - 1]
#     y2 = xy[i, j]
#     y4 = (y2 - y1)/(x2 - x1) * (jj - x2) + y2
#     Nc = (y4 - y3)/(x[i] - x[i - 1])*(ii - x[i]) + y4
    
#     if Nc<1:
#         Nc=1
#     return  Nc


# def Cap(portante=False,cohesion=False,Friccion=False,bcp=False,v=False,p=False,m=False):
#     estratos = pd.DataFrame(perfilGeotecnico.objects.all().values())
#     datosI=pd.DataFrame(datosIniciales.objects.all().values())
    
#     servicio=pd.DataFrame(servicios.objects.all().values())

#     if len(servicio.index)>0 and len(datosI.index)>0 and len(estratos.index)>0:

#         F3=pd.to_numeric(servicio['fuerza3'])
#         hj=pd.to_numeric(estratos['espesorEstrato'])
#         Gama=pd.to_numeric(estratos['pesoEspecifico'])
#         Fi=pd.to_numeric(list(estratos['friccionSuelo']))
#         C1=pd.to_numeric(list(estratos['cohesionSuelo']))
#         prof=pd.to_numeric(datosI['profundidadCimentacion'])[0]
#         kv=pd.to_numeric(datosI['kv'])[0]
#         kh=pd.to_numeric(datosI['kh'])[0]
#         modelo=datosI['modelo'][0]
#         FS=pd.to_numeric(datosI['factorResistencia'])[0]

#         h=np.repeat([float(0)],len(hj), axis=0)
        
#         for i in range(1,len(hj)):
#             h[0]=hj[0]
#             if i>0:
#                 h[i]=h[i-1]+hj[i]
        
#         j=0
#         q=np.repeat(float(0), [len(hj)], axis=0)

#         fi=Fi[j]
#         C=C1[j] 
        
#         while j<len(hj):
#             q[0]=Gama[0]*prof

#             if prof<=h[j]:
#                 q[j]=q[j-1]+ hj[j]*Gama[j] +(prof-hj[j])*Gama[j]
#                 fi=Fi[j]
#                 C=C1[j]             
               
#             j=j+1  


#         q=max(q)
#         Gama=(q/prof)

        
        
#         B=np.repeat(float(0), [len(F3)], axis=0)
#         Nq=math.exp(math.pi*math.tan(fi*(math.pi/180)))*pow(math.tan(math.pi/4+(fi/2)*(math.pi/180)),2)
#         Nc=(Nq-1)/math.tan(fi*(math.pi/180))

#         if modelo=='hansen':
#             Nq=math.exp(math.pi*math.tan(fi*(math.pi/180)))*pow(math.tan(math.pi/4+(fi/2)*(math.pi/180)),2)
#             Nc=(Nq-1)/math.tan(fi*(math.pi/180))
#             Ny=1.5*(Nq-1)*math.tan(fi*(math.pi/180))
#         elif modelo=='vesic':
#             Nq=math.exp(math.pi*math.tan(fi*(math.pi/180)))*pow(math.tan(math.pi/4+(fi/2)*(math.pi/180)),2)
#             Nc=(Nq-1)/math.tan(fi*(math.pi/180))
#             Ny=2*(Nq+1)*math.tan(fi*(math.pi/180))
        
#         elif modelo=='richards':
#             Nq=math.exp(math.pi*math.tan(fi*(math.pi/180)))*pow(math.tan(math.pi/4+(fi/2)*(math.pi/180)),2)
#             Nc=(Nq-1)/math.tan(fi*(math.pi/180))
#             Ny=2*(Nq+1)*math.tan(fi*(math.pi/180))
        
#         elif modelo=='soubra':
#             Nq=math.exp(math.pi*math.tan(fi*(math.pi/180)))*pow(math.tan(math.pi/4+(fi/2)*(math.pi/180)),2)
#             Nc=(Nq-1)/math.tan(fi*(math.pi/180))
#             Ny=2*(Nq+1)*math.tan(fi*(math.pi/180))
        
#         elif modelo=='sarma':
#             Nq=math.exp(math.pi*math.tan(fi*(math.pi/180)))*pow(math.tan(math.pi/4+(fi/2)*(math.pi/180)),2)
#             Nc=(Nq-1)/math.tan(fi*(math.pi/180))
#             Ny=2*(Nq+1)*math.tan(fi*(math.pi/180))

#         elif modelo=='budhu':
#             Nq=math.exp(math.pi*math.tan(fi*(math.pi/180)))*pow(math.tan(math.pi/4+(fi/2)*(math.pi/180)),2)
#             Nc=(Nq-1)/math.tan(fi*(math.pi/180))
#             Ny=2*(Nq+1)*math.tan(fi*(math.pi/180))



        
        

        
#         qu= [C*Nc+q*Nq+Gama*i*Ny/2 for i in B]
#         qa=[i/FS for i in qu]   

#         for i in range(len(F3)):
#             while qa[i]*pow(B[i],2)<F3[i]:
#                 B[i]=B[i]+0.01
#                 qu= [C*Nc+q*Nq+Gama*i*Ny/2 for i in B]
#                 qa=[i/FS for i in qu]
                
        
        
#         Personalizado=pd.DataFrame(dimensionesPersonalizadas.objects.all().values())
#         cuantia=pd.DataFrame(datosIniciales.objects.all().values()) 

#         if p==True and len(Personalizado.index)>0 and len(cuantia.index)>0 and cuantia['personalizado'][0]=='si':
            
#             B=list(pd.to_numeric(Personalizado['bpersonalizado']))
#             Nq=math.exp(math.pi*math.tan(fi*(math.pi/180)))*pow(math.tan(math.pi/4+(fi/2)*(math.pi/180)),2)
#             Nc=(Nq-1)/math.tan(fi*(math.pi/180))
#             if modelo=='hansen':
#                 Ny=1.5*(Nq-1)*math.tan(fi*(math.pi/180))
#             elif modelo=='Vesic':
#                 Ny=2*(Nq+1)*math.tan(fi*(math.pi/180))
#             qu= [C*Nc+q*Nq+Gama*i*Ny/2 for i in B]
#             qa=[i/FS for i in qu]    

#         if portante==True:
#             return qa
#         if cohesion==True:
#             return C
        
#         if cohesion==True:
#             return C
        
#         if Friccion==True:
#             return fi

#         if bcp==True:
#             return list(B)
#         if m==True:
#             return modelo

#         return JsonResponse(pd.DataFrame({'B':list(B)}).to_dict('records'), safe=False)
       
#     else:
#         if v==True:
#             return [0]
#         return JsonResponse({})


# def gf(s=False):
#     B=Cap(bcp=True,v=True)
#     qa=Cap(portante=True,v=True)
#     if sum(B)>0:
#         data=pd.DataFrame({'B':B,'qa':qa})

#         return JsonResponse(data.to_dict('records'), safe=False)
    
#     else:
#         return JsonResponse({})






# #print(Cap(m=True,v=True))
