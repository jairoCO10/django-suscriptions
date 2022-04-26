from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.
from .models import datosPrimary,diferenciales,preciosUnitarios,datosConsProfunda,eficiencia,precioMaterialCimentacionProfunda,geometriaCimentacionProfunda,rangoDimensiones,relacionCarga
from rest_framework import viewsets
from .serializers import DatosPrimarySerializer,diferencialesSerializer,preciosUnitariosSerializer,datosConsProfundaSerializer,geometriaCimentacionProfundaSerializer,precioMaterialCimentacionProfundaSerializer,eficienciaSerializer,rangoDimensionesSerializer,relacionCargaSerializer
import pandas as pd
import numpy as np
from portant_capacity.models import servicios, datosIniciales,dimensionesPersonalizadas
from geotechnical_profile.models import perfilGeotecnico
import math
from cmath import atan, exp, log10, nan, pi, sin, sqrt
from numpy.core.fromnumeric import mean
import statistics



class datosPrimaryViewSet(viewsets.ModelViewSet):
    serializer_class = DatosPrimarySerializer
    queryset = datosPrimary.objects.all()
    def perform_create(self, serializer):
        serializer.save() 
    def get_queryset(self):
        return self.queryset.filter()


class diferencialesViewSet(viewsets.ModelViewSet):
    serializer_class = diferencialesSerializer
    queryset = diferenciales.objects.all()
    def perform_create(self, serializer):
        serializer.save() 
    def get_queryset(self):
        return self.queryset.filter()

class preciosUnitariosViewSet(viewsets.ModelViewSet):
    serializer_class = preciosUnitariosSerializer
    queryset = preciosUnitarios.objects.all()
    def perform_create(self, serializer):
        serializer.save() 
    def get_queryset(self):
        return self.queryset.filter()


class eficienciaViewSet(viewsets.ModelViewSet):
    serializer_class = eficienciaSerializer
    queryset = eficiencia.objects.all()
    def perform_create(self, serializer):
        serializer.save() 
    def get_queryset(self):
        return self.queryset.filter()



class datosConsProfundaViewSet(viewsets.ModelViewSet):
    serializer_class = datosConsProfundaSerializer
    queryset = datosConsProfunda.objects.all()
    def perform_create(self, serializer):
        serializer.save() 
    def get_queryset(self):
        return self.queryset.filter()



class geometriaCimentacionProfundaViewSet(viewsets.ModelViewSet):
    serializer_class = geometriaCimentacionProfundaSerializer
    queryset = geometriaCimentacionProfunda.objects.all()
    def perform_create(self, serializer):
        serializer.save() 
    def get_queryset(self):
        return self.queryset.filter()



class precioMaterialCimentacionProfundaViewSet(viewsets.ModelViewSet):
    serializer_class = precioMaterialCimentacionProfundaSerializer
    queryset = precioMaterialCimentacionProfunda.objects.all()
    def perform_create(self, serializer):
        serializer.save() 
    def get_queryset(self):
        return self.queryset.filter()




class  rangoDimensionesViewSet(viewsets.ModelViewSet):
    serializer_class =  rangoDimensionesSerializer
    queryset =  rangoDimensiones.objects.all()
    def perform_create(self, serializer):
        serializer.save() 
    def get_queryset(self):
        return self.queryset.filter()





class  relacionCargaViewSet(viewsets.ModelViewSet):
    serializer_class = relacionCargaSerializer
    queryset =  relacionCarga.objects.all()
    def perform_create(self, serializer):
        serializer.save() 
    def get_queryset(self):
        return self.queryset.filter()


# ###############################
# # def BoxplotFuerza(r=False):
# #     servicio = pd.DataFrame(servicios.objects.all().values())

# #     if len(servicio.index)>0:
# #         F1=list(pd.to_numeric(list(servicio['fuerza1']),errors='coerce'))           
# #         F2=list(pd.to_numeric(list(servicio['fuerza2']),errors='coerce'))
# #         F3=list(pd.to_numeric(list(servicio['fuerza3']),errors='coerce'))
# #         dataF=pd.DataFrame({'F1':F1,'F2':F2,'F3':F3})

# #         Min=list(dataF.min())
# #         Max=list(dataF.max())
# #         mediana=list(dataF.median())


# #         q1=[list(dataF.F1.quantile([.25]).values)[0],list(dataF.F2.quantile([.25]).values)[0],list(dataF.F3.quantile([.25]).values)[0]]
# #         q3=[list(dataF.F1.quantile([.75]).values)[0],list(dataF.F2.quantile([.75]).values)[0],list(dataF.F3.quantile([.75]).values)[0]]
# #         data=pd.DataFrame({'Min':Min,'Mediana':mediana, 'Max':Max,'Q1':q1,'Q3':q3})

# #         return JsonResponse(data.to_dict('records'),safe=False)
    
# #     else:
# #         JsonResponse()

# # print(BoxplotFuerza(r=False))



# # def BoxplotMomento(r=False):
# #     servicio = pd.DataFrame(servicios.objects.all().values())

# #     if len(servicio.index)>0:
        
# #         m1=list(pd.to_numeric(list(servicio['momento1']),errors='coerce'))
# #         m2=list(pd.to_numeric(list(servicio['momento2']),errors='coerce'))
# #         m3=list(pd.to_numeric(list(servicio['momento3']),errors='coerce'))
# #         dataM=pd.DataFrame({'M1':m1,'M2':m2,'M3':m3})

# #         Min=list(dataM.min())
# #         Max=list(dataM.max())
# #         mediana=list(dataM.median())

# #         q1=[list(dataM.M1.quantile([.25]).values)[0],list(dataM.M2.quantile([.25]).values)[0],list(dataM.M3.quantile([.25]).values)[0]]
# #         q3=[list(dataM.M1.quantile([.75]).values)[0],list(dataM.M2.quantile([.75]).values)[0],list(dataM.M3.quantile([.75]).values)[0]]
# #         data=pd.DataFrame({'Min':Min,'Mediana':mediana, 'Max':Max,'Q1':q1,'Q3':q3})

# #         return  JsonResponse(data.to_dict('records'),safe=False)
# #     else:
# #         return JsonResponse()



# #Calculos
# ##############################################



# ref='B' in locals()
# if ref==False:
#     servicio = pd.DataFrame(servicios.objects.all().values())
#     B=list(np.repeat([float(0.01)],len(servicio.index), axis=0))
#     L=B


# def Asentamiento(B,L,aSi=False,aSc=False,aSt=False,v=False, salida=False,s1=False):

#     servicio = pd.DataFrame(servicios.objects.all().values())

#     estratos=pd.DataFrame(perfilGeotecnico.objects.all().values())
#     datosI=pd.DataFrame(datosIniciales.objects.all().values())

#     if len(datosI.index)>0 and len(estratos.index)>0 and len(servicio.index)>0:

#         F3=list(pd.to_numeric(list(servicio['fuerza3'])))

#         prof=pd.to_numeric(datosI['profundidadCimentacion'])[0]
#         NF=pd.to_numeric(datosI['nivelFeatico'])[0]
#         estratos=estratos.sort_values('idEstrato')

#         Lx=[L[i]/2 for i in range(len(L))]
#         Bx=[B[i]/2 for i in range(len(B))]
#         product = [x*y for x,y in zip(B,L)]
#         q=[F3[x]/product[x] for x in range(len(product))]

#         u=pd.to_numeric(list(estratos['relacionPoisson']))
#         Es=pd.to_numeric(list(estratos['moduloElasticidad']))
#         Cc=pd.to_numeric(list(estratos['indiceDeComprension']))
#         Cr=pd.to_numeric(list(estratos['indiceDeExpansibilidad']))
#         Sp=pd.to_numeric(list(estratos['presionDepreconsolidacion']))
#         e0=pd.to_numeric(list(estratos['relacionDeVacioInicial']))
#         hj=pd.to_numeric(list(estratos['espesorEstrato']))
#         Gama=pd.to_numeric(list(estratos['pesoEspecifico']))

#         ZI=np.arange(pd.to_numeric(datosI['h'])[0],sum(hj),pd.to_numeric(datosI['h'])[0])
#         hi=np.repeat([float(0)],len(ZI), axis=0)
#         hi[0]=ZI[0]
#         for i in range(1,len(ZI)):
#             hi[i]=pd.to_numeric(datosI['h'])[0]

#         Zcarg=[ZI[i]-prof for i in range(len(ZI))]
#         for i in range(len(Zcarg)):
#             if Zcarg[i]<0:
#                 Zcarg[i]=0


#         Crr=np.repeat([float(0)],len(ZI), axis=0)
#         Ccc=np.repeat([float(0)],len(ZI), axis=0)
#         SP=np.repeat([float(0)],len(ZI), axis=0)
#         E0=np.repeat([float(0)],len(ZI), axis=0)
#         Hj=np.repeat([float(0)],len(ZI), axis=0)
#         GAMA=np.repeat([float(0)],len(ZI), axis=0)
#         ES=np.repeat([float(0)],len(ZI), axis=0)
#         uu=np.repeat([float(0)],len(ZI), axis=0)

#         h=np.repeat([float(0)],len(hj), axis=0)
#         h[0]=hj[0]
#         for i in range(1,len(hj)):
#             h[i]=h[i-1]+hj[i]


#         s=0
#         for i in range(len(ZI)):

#             if ZI[i]<=h[s]:
#                 Crr[i]=Cr[s]
#                 Ccc[i]=Cc[s]
#                 E0[i]=e0[s]
#                 GAMA[i]=Gama[s]
#                 SP[i]=Sp[s]
#                 Hj[i]=hj[s]
#                 ES[i]=Es[s]
#                 uu[i]=u[s]
#             else:
#                 s=s+1
#                 Crr[i]=Cr[s]
#                 Ccc[i]=Cc[s]
#                 E0[i]=e0[s]
#                 GAMA[i]=Gama[s]
#                 SP[i]=Sp[s]
#                 Hj[i]=hj[s]
#                 ES[i]=Es[s]
#                 uu[i]=u[s]


#         for i in range(len(ZI)):
#             if ZI[i]<=prof:
#                 Ccc[i]=0
#                 Crr[i]=0

#         iSz=[hi[i]*GAMA[i] for i in range(len(hi))]
#         Sz=np.repeat([float(0)],len(iSz), axis=0)
#         Sz[0]=iSz[0]
#         for i in range(1,len(Sz)):
#             Sz[i]=Sz[i-1]+iSz[i]

#         gw=9.81
#         hw=[ZI[i]-NF for i in range(len(ZI))]
#         for i in range(len(hw)):
#             if hw[i]<0:
#                 hw[i]=0
#         U=[gw*x for x in hw]


#         #esfuerzos efectivos

#         Szp=[Sz[i]-U[i] for i in range(len(U))]
#         R1=np.repeat([float(0)],len(Zcarg), axis=0)
#         R2=np.repeat([float(0)],len(Zcarg), axis=0)
#         R3=np.repeat([float(0)],len(Zcarg), axis=0)
#         dsz=np.repeat([float(0)],len(Zcarg), axis=0)
#         dsx=np.repeat([float(0)],len(Zcarg), axis=0)
#         dsy=np.repeat([float(0)],len(Zcarg), axis=0)
#         DU=np.repeat([float(0)],len(Zcarg), axis=0)
#         dszp=np.repeat([float(0)],len(Zcarg), axis=0)
#         dsxp=np.repeat([float(0)],len(Zcarg), axis=0)
#         dsyp=np.repeat([float(0)],len(Zcarg), axis=0)
#         Dz=np.repeat([float(0)],len(Zcarg), axis=0)

#         ASI=np.repeat([float(0)],len(B), axis=0)
#         ASC=np.repeat([float(0)],len(B), axis=0)
#         AST=np.repeat([float(0)],len(B), axis=0)
#         for j in range(len(B)):
#             for k in range(len(Zcarg)):
#                 R1[k]=math.sqrt(Lx[j]**2+Zcarg[k]**2)
#                 R2[k]=math.sqrt(Bx[j]**2+Zcarg[k]**2)
#                 R3[k]=math.sqrt(Lx[j]**2+Bx[j]**2+Zcarg[k]**2)
#                 if Zcarg[k]==0:
#                     dsz[k]=0
#                     dsx[k]=0
#                     dsy[k]=0
#                 else:

#                     dsz[k]=4*(q[j]/(2*math.pi))*(math.atan(((Lx[j])*(Bx[j]))/(Zcarg[k]*R3[k]))+(((Lx[j])*(Bx[j])*Zcarg[k])/R3[k])*((1/(R1[k]**2))+(1/(R2[k]**2))))
#                     dsx[k]=4*(q[j]/(2*math.pi))*(math.atan((((Lx[j]*Bx[j])/(Zcarg[k]*R3[k]))))- (Lx[j]*Bx[j]*Zcarg[k])/((R1[k]**2)*R3[k]))
#                     dsy[k]=4*(q[j]/(2*math.pi))*(math.atan((((Lx[j]*Bx[j])/(Zcarg[k]*R3[k]))))- (Lx[j]*Bx[j]*Zcarg[k])/((R2[k]**2)*R3[k]))



#                 DU[k]=(dsz[k]+dsy[k]+dsx[k])/3
#                 Dz[k]=((dsz[k]/ES[k])-(uu[k]/ES[k])*(dsx[k]+dsy[k]))*hi[k]

#                 dszp[k]=dsz[k]-DU[k]
#                 dsxp[k]=dsx[k]-DU[k]
#                 dsyp[k]=dsy[k]-DU[k]



#             Szfp=[Szp[i]+dszp[i] for i in range(len(dszp))]



#             Sc=np.repeat([float(0)],len(Szfp), axis=0)
#             for k in range(len(Szfp)):
#                 if datosI['OCR'][0]=="Si":
#                    C1=hi[k]/(1+E0[k])
#                    term1=Ccc[k]*C1
#                    log=math.log10(Szfp[k]/Szp[k])
#                    Sc[k]=term1*log
#                 else:
#                     if SP[k]>Szfp[k] and Szfp[k]/Szp[k]>0:
#                        C1=hi[k]/(1+E0[k])
#                        term1=Crr[k]*C1
#                        log=math.log10(Szfp[k]/Szp[k])
#                        Sc[k]=term1*log
#                     elif SP[k]>Szp[k] and SP[k]<Szfp[k]:
#                        C1=hi[k]/(1+E0[k])
#                        Sc[k]=C1*(Crr[k]*math.log10(SP[k]/Szp[k]) + Ccc[k]*math.log10(Szfp[k]/SP[k]))
#                     elif Szfp[k]/Szp[k]>0:
#                         C1=hi[k]/(1+E0[k])
#                         term1=Ccc[k]*C1
#                         log=math.log10(Szfp[k]/Szp[k])
#                         Sc[k]=term1*log
#                     else:
#                         Sc[k]=0


#             ASI[j]=sum(Dz)
#             ASC[j]=sum(Sc)
#             AST[j]=sum(Dz)+sum(Sc)


#         data=pd.DataFrame({'q':q[0],'L':L[0],'B':B[0],'hi':hi,'Gama':GAMA,'ZI':ZI,'iSz':iSz,'Sz':Sz,'gw':gw,'hw':hw,'U':U,'Szp':Szp,'Zcarg':Zcarg,'R1':R1,'R2':R2,'R3':R3,'dsz':dsz,'dsx':dsx,'dsy':dsy,'DU':DU,'Dz':Dz,'dszp':dszp,'Szfp':Szfp,'Sc':Sc})

#         data2=pd.DataFrame({'joint':servicio['joints'],'B_Asentamiento':B,'L_Asentamiento':L,'AsentamientoInmediatos':ASI,'AsentamientoporConsolidacion':ASC,'Asentamientototal':AST})

#         if salida==True:
#             return data
#         if s1==True:
#             return data2


#         if aSi==True:
#             return ASI
#         elif aSc==True:
#             return ASC
#         elif aSt==True:
#             return  AST

#         return JsonResponse(data2.to_dict('records'),safe=False)

#     else:
#         if v==True:
#             return pd.DataFrame({'B_Asentamiento':[0]})
#         return JsonResponse({})



# def Asentamiento2(s=True):
#     if sum(Asentamiento(B,L,aSt=True,v=True))>0:
#         datosI=pd.DataFrame(datosIniciales.objects.all().values())
#         maxAsen=pd.to_numeric(datosI['asentamimientoMaximo'])[0]
#         Asen_total=Asentamiento(B,L,aSt=True)
#         for i in range(len(Asen_total)):
#             while Asen_total[i]>maxAsen:
#                 B[i]=B[i]+pd.to_numeric(datosI['aumentoB'])[0]
#                 L[i]=L[i]+pd.to_numeric(datosI['aumentoB'])[0]
#                 Asen_total= Asentamiento(B,L,aSt=True)

#         data=Asentamiento(B,L,s1=True)
#         if s==True:
#             return data

#         return JsonResponse(data.to_dict('records'),safe=False)

#     else:
#         if s==True:
#             return JsonResponse(pd.DataFrame({'B_Asentamiento':[0],'L_Asentamiento':[0]}).to_dict('records'),safe=False)
#         return JsonResponse({})


# def AsentRegister(salida=False):

#     bAse=Asentamiento2(s=True)
#     if sum(bAse['B_Asentamiento'])>0:
#         B=bAse['B_Asentamiento']
#         L=bAse['L_Asentamiento']
#         datos=Asentamiento(B,L,salida=True)
#         return JsonResponse(datos.to_dict('records'),safe=False)
#     else:
#         if salida==True:
#             return [0]

#         return JsonResponse({})


# def dimensionMayor(s=False):
#     bAsen=Asentamiento2(s=True)
#     if sum(list(Cap(bcp=True)))>0 and sum(bAsen['B_Asentamiento'])>0:
#         Bcp=list(Cap(bcp=True))
#         bAsen=list(bAsen['B_Asentamiento'])
#         Bmayor=np.repeat([float(0)],len(Bcp), axis=0)
#         for i in range(len(Bcp)):
#             if Bcp[i]>=bAsen[i]:
#                 Bmayor[i]=Bcp[i]
#             else:
#                 Bmayor[i]=bAsen[i]
#         B=Bmayor
#         L=Bmayor
#         Asen=Asentamiento(B,L,s1=True)
#         resultado=pd.DataFrame({'DimensionMayor':Bmayor,'A_Elastico':Asen['AsentamientoInmediatos'],'A_consolidacion':Asen['AsentamientoporConsolidacion'],'A_Total':Asen['Asentamientototal']})
#         if s==True:
#             return resultado
#         return JsonResponse(resultado.to_dict('records'),safe=False)
#     else:
#         if s==True:
#             return pd.DataFrame({'DimensionMayor':[0]})
#         return JsonResponse({})



# def Excentricidades(s=True):
#     DimensionMayor=dimensionMayor(s=True)
#     servicio = pd.DataFrame(servicios.objects.all().values())
#     datosI=pd.DataFrame(datosIniciales.objects.all().values())
#     if sum(DimensionMayor['DimensionMayor'])>0:
#         F3=list(pd.to_numeric(list(servicio['fuerza3'])))
#         M1=pd.to_numeric(servicio["momento1"])
#         M2=pd.to_numeric(servicio["momento2"])
#         lado_neto=list(DimensionMayor['DimensionMayor'])

#         Ex=[abs(M1[i]/F3[i]) for i in range(len(F3))]
#         Ey=[abs(M2[i]/F3[i]) for i in range(len(F3))]
#         Bz=[2*(lado_neto[i]/2+abs(Ex[i])) for i in range(len(lado_neto))]
#         Lz=[2*(lado_neto[i]/2+abs(Ey[i])) for i in range(len(lado_neto))]
#         for j in range(len(F3)):
#             while Ex[j]>(1/6)*Bz[j]:
#                 Bz[j]=Bz[j]+pd.to_numeric(datosI['aumentoB'])[0]

#         for k in range(len(F3)):
#             while Ey[k]>(1/6)*Lz[k]:
#                 Lz[k]=Lz[k]+pd.to_numeric(datosI['aumentoB'])[0]
#         B=Bz
#         L=Lz
#         BL=Asentamiento(B,L,s1=True)

#         data=pd.DataFrame({'joint':servicio['joints'],'B_Excentricidad':Bz,'L_Excentricidad':Lz,'AsentamientoElastico':BL['AsentamientoInmediatos'],'AsentamientoPorConsolidacion':BL['AsentamientoporConsolidacion'],'Asentamientototal':BL['Asentamientototal']})
#         if s==True:
#             return data
#         return JsonResponse(data.to_dict('records'),safe=False)
#     else:
#         if s==True:
#             return pd.DataFrame({'B_Excentricidad':[0],'L_Excentricidad':[0]})
#         return JsonResponse({})




# def AsenD(consola=False):
#     diferencial= pd.DataFrame(diferenciales.objects.all().values())
#     datosI=pd.DataFrame(datosIniciales.objects.all().values())
#     dim=Excentricidades(s=True)

#     if sum(dim['B_Excentricidad'])>0 and len(diferencial.index)>0 and len(dim['B_Excentricidad'])>1:
#         B=list(dim['B_Excentricidad'])
#         L=list(dim['L_Excentricidad'])
#         distancias=pd.to_numeric(diferencial["distancias"])
#         joint2=pd.to_numeric(diferencial["joints"])
#         Vecinos=pd.to_numeric(diferencial["vecinos"])
#         joint=pd.to_numeric(servicio["joints"])
#         Asen_total=Asentamiento(B,L,aSt=True,v=True)
#         criterio=list(pd.to_numeric(diferencial['criterioDiferencial']))

#         DH_DIF_Adm=[distancias[x]/criterio[x] for x in range(len(distancias))]
#         DH_DIF_Cal=np.repeat([float(0)],len(joint2), axis=0)
#         for i in range(len(joint2)):
#             DH_DIF_Cal[i]=float(abs((Asen_total[int(np.where([joint[x]==joint2[i] for x in range(len(joint))])[0])]-Asen_total[int(np.where([joint[x]==Vecinos[i] for x in range(len(joint))])[0])])*1000))


#         for i in range(len(DH_DIF_Adm)):
#             while  DH_DIF_Adm[i]<DH_DIF_Cal[i]:
#                 Joi1=joint[int(np.where([joint[x]==joint2[i] for x in range(len(joint))])[0])]
#                 Joi2=joint[int(np.where([joint[x]==Vecinos[i] for x in range(len(joint))])[0])]
#                 A1=Asen_total[int(np.where([joint[x]==joint2[i] for x in range(len(joint))])[0])]
#                 A2=Asen_total[int(np.where([joint[x]==Vecinos[i] for x in range(len(joint))])[0])]
#                 if A1>A2:
#                     B[int(np.where([joint[x]==Joi1 for x in range(len(joint))])[0])]=B[int(np.where([joint[x]==Joi1 for x in range(len(joint))])[0])]+pd.to_numeric(datosI['aumentoB'])[0]
#                     L[int(np.where([joint[x]==Joi1 for x in range(len(joint))])[0])]=L[int(np.where([joint[x]==Joi1 for x in range(len(joint))])[0])]+pd.to_numeric(datosI['aumentoB'])[0]

#                 elif A2>A1:
#                     B[int(np.where([joint[x]==Joi2 for x in range(len(joint))])[0])]=B[int(np.where([joint[x]==Joi2 for x in range(len(joint))])[0])]+pd.to_numeric(datosI['aumentoB'])[0]
#                     L[int(np.where([joint[x]==Joi2 for x in range(len(joint))])[0])]=L[int(np.where([joint[x]==Joi2 for x in range(len(joint))])[0])]+pd.to_numeric(datosI['aumentoB'])[0]

#                 elif A1==A2:
#                     B[int(np.where([joint[x]==Joi1 for x in range(len(joint))])[0])]=B[int(np.where([joint[x]==Joi1 for x in range(len(joint))])[0])]+pd.to_numeric(datosI['aumentoB'])[0]
#                     B[int(np.where([joint[x]==Joi2 for x in range(len(joint))])[0])]=B[int(np.where([joint[x]==Joi2 for x in range(len(joint))])[0])]+pd.to_numeric(datosI['aumentoB'])[0]
#                     L[int(np.where([joint[x]==Joi1 for x in range(len(joint))])[0])]=L[int(np.where([joint[x]==Joi1 for x in range(len(joint))])[0])]+pd.to_numeric(datosI['aumentoB'])[0]
#                     L[int(np.where([joint[x]==Joi2 for x in range(len(joint))])[0])]=L[int(np.where([joint[x]==Joi2 for x in range(len(joint))])[0])]+pd.to_numeric(datosI['aumentoB'])[0]


#                 Asen_total=Asentamiento(B,L,aSt=True,v=True)
#                 DH_DIF_Cal[i]=abs(A1-A2)*1000

#         ASI=Asentamiento(B,L,aSi=True,v=True)
#         ASC=Asentamiento(B,L,aSc=True,v=True)
#         AST=Asentamiento(B,L,aSt=True,v=True)
#         data= pd.DataFrame({'B':B,'L':L,'A_Elastico':ASI,'A_consolidacion':ASC,'A_Total':AST})
#         if consola==True:
#             return  data

#         return JsonResponse(data.to_dict('records'), safe=False)

#     else:
#         if consola==True:
#             return  pd.DataFrame({'B':[0],'L':[0]})

#         return JsonResponse({})




# def dimensionesConstruccion(s=True):
#     datosI=pd.DataFrame(datosIniciales.objects.all().values())
#     Personalizado=pd.DataFrame(dimensionesPersonalizadas.objects.all().values())
#     BL=AsenD(consola=True)
#     dim=Excentricidades(s=True)
#     Be=dim['B_Excentricidad']
#     Le=dim['L_Excentricidad']
#     Bd=list(BL['B'])
#     Ld=list(BL['L'])
#     if sum(Bd)>0 or sum(Be)>0:
#         if sum(Be)>0 and len(Be)==1:
#             B=Be
#             L=Le
#             B_Const=[round(B[i],int(datosI['cifrasDecimales'][0])) for i in range(len(B))]
#             L_Const=[round(L[i],int(datosI['cifrasDecimales'][0])) for i in range(len(L))]
#         elif sum(Bd)>0 and len(Bd)>1:
#             B=Bd
#             L=Ld
#             B_Const=[round(B[i],int(datosI['cifrasDecimales'][0])) for i in range(len(B))]
#             L_Const=[round(L[i],int(datosI['cifrasDecimales'][0])) for i in range(len(L))]

#         else:
#             dimBL=Asentamiento2(s=True)
#             B=list(dimBL['B_Asentamiento'])
#             L=list(dimBL['L_Asentamiento'])
#             B_Const=[round(B[i],int(datosI['cifrasDecimales'][0])) for i in range(len(B))]
#             L_Const=[round(L[i],int(datosI['cifrasDecimales'][0])) for i in range(len(L))]





#         for i in range(len(B_Const)):
#             if B_Const[i]<1:
#                 B_Const[i]=1
#             if L_Const[i]<1:
#                 L_Const[i]=1
#             if B_Const[i]<B[i]:
#                 B_Const[i]=B_Const[i]+pd.to_numeric(datosI['salto'])[0]
#             if L_Const[i]<L[i]:
#                 L_Const[i]=L_Const[i]+pd.to_numeric(datosI['salto'])[0]


#         if len(Personalizado.index)>0 and datosI['personalizado'][0]=='si':
#             B_Const=list(pd.to_numeric(Personalizado['bpersonalizado']))
#             L_Const=list(pd.to_numeric(Personalizado['lpersonalizado']))

#         ASI=Asentamiento(B_Const,L_Const,aSi=True,v=True)
#         ASC=Asentamiento(B_Const,L_Const,aSc=True,v=True)
#         AST=Asentamiento(B_Const,L_Const,aSt=True,v=True)

#         data=pd.DataFrame({'B_construcion':B_Const,'L_construcion':L_Const,'Asen_Elastico':ASI,'Asen_consolidacion':ASC,'Asen_Total':AST})
#         if s==True:
#             return data

#         return JsonResponse(data.to_dict('records'), safe=False)
#     else:
#         if s==True:
#             return pd.DataFrame({'B_construcion':[0],'L_construcion':[0]})
#         return JsonResponse({})




# def cant_ObraPres(R=False):
#     ValoresUnitarios=pd.DataFrame(preciosUnitarios.objects.all().values())
#     Personalizado=pd.DataFrame(dimensionesPersonalizadas.objects.all().values())
#     datosI=pd.DataFrame(datosIniciales.objects.all().values())
#     datosII=pd.DataFrame(datosPrimary.objects.all().values())

#     BL=dimensionesConstruccion(s=True)

#     if len(ValoresUnitarios.index)>0 and len(datosI.index)>0 and len(datosII.index)>0:
#         if sum(BL['B_construcion'])>0 and datosI['personalizado'][0]=='no':
#             B=BL['B_construcion']
#             L=BL['L_construcion']
#         elif sum(BL['B_construcion'])>=0 and  datosI['personalizado'][0]=='si' and len(Personalizado.index)>0:
#             B=list(pd.to_numeric(Personalizado['bpersonalizado']))
#             L=list(pd.to_numeric(Personalizado['lpersonalizado']))
#         else:
#             return JsonResponse({})


#         prof=pd.to_numeric(datosI['profundidadCimentacion'])[0]
#         EspesorSolado=pd.to_numeric(datosII['espesorSolado'])[0]

#         #Excavación
#         Area=list(np.multiply(list(B),list(L)))
#         Exc=[(prof+EspesorSolado)*i for i in Area]

#         #Solado
#         solado=[EspesorSolado*x for x in Area]

#         #Concreto Zapatas
#         MayorBL=np.repeat([float(0)],len(B), axis=0)
#         MenorBL=np.repeat([float(0)],len(B), axis=0)
#         for i in range(len(B)):
#             if  B[i]>=L[i]:
#                 MayorBL[i]=B[i]
#                 MenorBL[i]=L[i]
#             if L[i]>B[i]:
#                 MayorBL[i]=L[i]
#                 MenorBL[i]=B[i]

#         if datosII['condicion'][0]=='mayorBL':
#             ConcZ=np.multiply([pd.to_numeric(datosII['espesorZapata'])[0]*x for x in MayorBL], Area)
#             ConcP=[prof*pow(pd.to_numeric(datosII['espesorPedestal'])[0]*MayorBL[i],2) for i in range(len(MayorBL))]

#         elif datosII['condicion'][0]=='menorBL':
#             ConcZ=np.multiply([pd.to_numeric(datosII['espesorZapata'])[0]*x for x in MenorBL], Area)
#             ConcP=[prof*pow(pd.to_numeric(datosII['espesorPedestal'])[0]*MenorBL[i],2) for i in range(len(MenorBL))]
#         else:
#             ConcZ=np.multiply([pd.to_numeric(datosII['espesorZapata'])[0]*x for x in MenorBL], Area)
#             ConcP=[prof*pow(pd.to_numeric(datosII['espesorPedestal'])[0]*MenorBL[i],2) for i in range(len(MenorBL))]


#         Relleno=[Exc[i]-solado[i]-ConcP[i]-ConcZ[i] for i in range(len(B))]
#         for i in range(len(Relleno)):
#             if Relleno[i]<=0:
#                 Relleno[i]=0

#         #Presupuesto

#         PrecioExc=pd.to_numeric(ValoresUnitarios['precioExc'])[0]/1000000
#         VPExc=[i*PrecioExc for i in Exc]

#         PrecioConcZ=pd.to_numeric(ValoresUnitarios['precioConcZ'])[0]/1000000
#         VPConcZ=[i*PrecioConcZ for i in ConcZ]

#         PrecioConcP=pd.to_numeric(ValoresUnitarios['precioConcP'])[0]/1000000

#         VPConcP=[i*PrecioConcP for i in list(ConcP)]

#         PrecioRelleno=pd.to_numeric(ValoresUnitarios['precioRelleno'])[0]/1000000

#         VPRelleno=[i*PrecioRelleno for i in Relleno]

#         Preciosolado=pd.to_numeric(ValoresUnitarios['preciosolado'])[0]/1000000
#         VPsolado=[i*Preciosolado for i in solado]
#         AceroZapata=[pd.to_numeric(datosII['cuantiaAceroZapata'])[0]*i for i in ConcZ]
#         AceroPedestal=[pd.to_numeric(datosII['cuantiaAceroPedestal'])[0]*i for i in ConcP]
#         PrecioAceroZapata=pd.to_numeric(ValoresUnitarios['precioAceroZapata'])[0]/1000000
#         PrecioAceroPedestal=pd.to_numeric(ValoresUnitarios['precioAceroPedestal'])[0]/1000000
#         VpAceroZapata=[PrecioAceroZapata*i for i in AceroZapata]
#         VpAceroPedestal=[PrecioAceroPedestal*i for i in AceroPedestal]
#         VPZapata=[VPExc[i]+VPConcZ[i] +VPConcP[i]+VPRelleno[i]+VPsolado[i]+VpAceroZapata[i]+VpAceroPedestal[i] for i in range(len(B))]
#         SubTotal=round(sum(VPZapata),1)
#         data=pd.DataFrame({'Profundidad':prof,'B':[round(i,1) for i in B],'L':[round(i,1) for i in L],'Excavacion':[round(i,1) for i in Exc],'solado':[round(i,2) for i in solado],'ConcretoZapata':[round(i,2) for i in ConcZ],'ConcretoPedestal':[round(i,2) for i in ConcP],'Relleno':[round(i,2) for i in Relleno],'ValorParcialExcavacion':[round(i,2) for i in VPExc],'ValorParcialSolado':[round(i,2) for i in VPsolado],'ValorParcialConcretoZapata':[round(i,2) for i in VPConcZ],'ValorParcialConcretoPedestal':[round(i,2) for i in VPConcP],'VPRelleno':[round(i,2) for i in VPRelleno],'AceroZapata':[round(i,2) for i in AceroZapata],'AceroPedestal':[round(i,2) for i in AceroPedestal],'VpAceroZapata':[round(i,2) for i in VpAceroZapata],'VpAceroPedestal':[round(i,2) for i in VpAceroPedestal],'VPZapata':[round(i,2) for i in VPZapata],'SubTotal':round(SubTotal,1)})

#         if R==True:
#             return data

#         return JsonResponse(data.to_dict('records'), safe=False)

#     else:
#         if R==True:
#             return  pd.DataFrame({'B':[0],'L':[0]})
#         return JsonResponse({})




# def verificar(s=True):
#     diferencial= pd.DataFrame(diferenciales.objects.all().values())
#     Personalizado=pd.DataFrame(dimensionesPersonalizadas.objects.all().values())
#     if len(Personalizado.index)>0 and len(diferencial.index)>0:

#         BL=dimensionesConstruccion(s=True)


#         B=BL['B_construcion']
#         L=BL['L_construcion']



#         Ase_total=Asentamiento(B,L,aSt=True,v=True)
#         distancias=list(pd.to_numeric(diferencial['distancias']))
#         joint2=list(pd.to_numeric(diferencial['joints']))
#         joint=list(pd.to_numeric(servicio['joints']))
#         criterio=list(pd.to_numeric(diferencial['criterioDiferencial']))
#         Vecinos=list(pd.to_numeric(diferencial['vecinos']))
#         DH_DIF_Adm=[distancias[x]/criterio[x] for x in range(len(distancias))]
#         DH_DIF_Cal=np.repeat([float(0)],len(joint2), axis=0)
#         for i in range(len(joint2)):
#             DH_DIF_Cal[i]=float(abs((Ase_total[int(np.where([joint[x]==joint2[i] for x in range(len(joint))])[0])]-Ase_total[int(np.where([joint[x]==Vecinos[i] for x in range(len(joint))])[0])])*1000))

#         prueba=np.repeat([0],len(joint2), axis=0)

#         for i in range(len(DH_DIF_Cal)):
#             if DH_DIF_Adm[i]<DH_DIF_Cal[i]:
#                 prueba[i]=1
#             else:
#                 prueba[i]=0
#         print(prueba)
#         if sum(prueba)>0:
#             return JsonResponse(pd.DataFrame({'Cumple':['No cumple con asentamientos diferenciales']}).to_dict('records'),safe=False)
#         else:
#             return JsonResponse(pd.DataFrame({'Cumple':['Si cumple con asentamientos diferenciales']}).to_dict('records'),safe=False)
#     else:
#         return JsonResponse({})


# def AsentamiendoPersonalizado(s=True):
#     datosI=pd.DataFrame(datosIniciales.objects.all().values())
#     Personalizado=pd.DataFrame(dimensionesPersonalizadas.objects.all().values())
#     BL=Asentamiento2(s=True)
#     if len(Personalizado.index)>0 and sum(BL['B_Asentamiento'])>0 and datosI['personalizado'][0]=='si':
#         B=list(pd.to_numeric(Personalizado['bpersonalizado']))
#         L=list(pd.to_numeric(Personalizado['lpersonalizado']))
#         ASI=Asentamiento(B,L,aSi=True,v=True)
#         ASC=Asentamiento(B,L,aSc=True,v=True)
#         AST=Asentamiento(B,L,aSt=True,v=True)
#         data=pd.DataFrame({'B_pers':B,'L_pers':L,'AsenInmediato':ASI,'AsenConsolidacion':ASC,'AsenTotal':AST})
#         if s==True:
#             return data
#         return JsonResponse(data.to_dict('records'),safe=False)
#     else:
#         if s==True:
#             return pd.DataFrame({'B_pers':[0],'L_pers':[0]})



# def secuencia(R=False):
#     datosI=pd.DataFrame(datosIniciales.objects.all().values())
#     servicio = pd.DataFrame(servicios.objects.all().values())
#     dim=cant_ObraPres(R=True)
#     AsenBL=Asentamiento2(s=True)
#     dim2=Excentricidades(s=True)

#     if sum(list(Cap(bcp=True,p=True)))>0 and len(servicio.index)>0 and len(datosI.index)>0 and sum(list(dim['B']))>0 and sum(list(AsenBL['B_Asentamiento']))>0:
#         prof=pd.to_numeric(datosI['profundidadCimentacion'])[0]
#         Bcp=list(Cap(bcp=True,p=True))
#         qa=Cap(portante=True,p=True)
#         bAsen=list(AsenBL['B_Asentamiento'])
#         Be=dim2['B_Excentricidad']
#         Le=dim2['L_Excentricidad']

#         difBL=AsenD(consola=True)
#         if sum(difBL['B'])>0 and len(Le)>1:
#             Bd=difBL['B']
#             Ld=difBL['L']
#         else:
#             Bd=''
#             Ld=''

#         Bf=list(dim['B'])
#         Lf=list(dim['L'])


#         F3=list(pd.to_numeric(list(servicio['fuerza3'])))

#         AsenTotal=Asentamiento(B,L,aSt=True,v=True)

#         KzAct=[[F3[i]/[B[j]*L[j] for j in range(len(B))][i] for i in range(len(F3)) ][x]/AsenTotal[x] for x in range(len(F3))]
#         KzAdm=[qa[i]/AsenTotal[i] for i in range(len(AsenTotal))]



#         datos=pd.DataFrame({'profundidad':prof,'BCP':[round(i, 3) for i in Bcp],'qa':[round(i, 3) for i in qa],'KzAct':[round(i, 3) for i in KzAct],'KzAdm':[round(i, 3) for i in KzAdm], 'AsenB':[round(i, 3) for i in bAsen],'B_Ex':[round(i, 3) for i in Be],'L_Ex':[round(i, 3) for i in Le],'Bdif':[round(i,3) for i in Bd],'Ldif':[round(i,3) for i in Ld], 'BConstr':Bf,'LConstr':Lf})

#         if R==True:
#             return datos

#         return JsonResponse(datos.to_dict('records'), safe=False)

#     else:
#         if R==True:
#             return "no existe informacion"
#         JsonResponse({})



# #Presupuesto


# def presupuesto(r=False):
#     ValoresUnitarios=pd.DataFrame(preciosUnitarios.objects.all().values())
#     data1=cant_ObraPres(R=True)

#     if len(ValoresUnitarios.index)>0 and sum(data1['B'])>0:
#         precioExc=pd.to_numeric(list(ValoresUnitarios['precioExc']))
#         precioConcZ=pd.to_numeric(ValoresUnitarios['precioConcZ'])
#         precioConcP=pd.to_numeric(ValoresUnitarios['precioConcP'])
#         precioRelleno=pd.to_numeric(ValoresUnitarios['precioRelleno'])
#         preciosolado=pd.to_numeric(ValoresUnitarios['preciosolado'])
#         precioAceroZapata=pd.to_numeric(ValoresUnitarios['precioAceroZapata'])
#         precioAceroPedestal=pd.to_numeric(ValoresUnitarios['precioAceroPedestal'])

#         Exc=[sum(list(data1['Excavacion']))]
#         solado=[sum(list(data1['solado']))]
#         ConcZ=[sum(list(data1['ConcretoZapata']))]
#         ConcP=[sum(list(data1['ConcretoPedestal']))]
#         Relleno=[sum(list(data1['Relleno']))]
#         VPExc=[sum(list(data1['ValorParcialExcavacion']))]
#         VPsolado=[sum(list(data1['ValorParcialSolado']))]
#         VPConcZ=[sum(list(data1['ValorParcialConcretoZapata']))]
#         VPConcP=[sum(list(data1['ValorParcialConcretoPedestal']))]
#         VPRelleno=[sum(list(data1['VPRelleno']))]
#         AceroZapata=[sum(list(data1['AceroZapata']))]
#         AceroPedestal=[sum(list(data1['AceroPedestal']))]
#         VpAceroZapata=[sum(list(data1['VpAceroZapata']))]
#         VpAceroPedestal=[sum(list(data1['VpAceroPedestal']))]
#         VPZapata=[sum(list(data1['VPZapata']))]
#         SubTotal=[sum(list(data1['SubTotal']))]
#         data=pd.DataFrame({'Exc':Exc,'solado':solado,'ConcZ':ConcZ,'ConcP':ConcP,'Relleno':Relleno,'VPExc':VPExc,'VPsolado':VPsolado,'VPConcZ':VPConcZ,'VPConcP':VPConcP,'VPRelleno':VPRelleno,'AceroZapata':AceroZapata,'AceroPedestal':AceroPedestal, 'VpAceroZapata':VpAceroZapata,'VpAceroPedestal':VpAceroPedestal,'VPZapata':VPZapata,'SubTotal':round(SubTotal,1)})


#         data2=pd.DataFrame({'precioExc':precioExc,'precioConcZ':precioConcZ,'precioConcP':precioConcP,'precioRelleno':precioRelleno,'preciosolado':preciosolado,'precioAceroZapata':precioAceroZapata,'precioAceroPedestal':precioAceroPedestal})
#         data3=pd.concat([data2,data], axis=1,)


#         return JsonResponse(data3.to_dict('records'), safe=False)
#     else:
#         return JsonResponse({})


# # #########################################################################################################
# # #################















# # #profundidad vs costo

# def Cap2(prof=1,portante=False,cohesion=False,Friccion=False,bcp=False,v=False,p=False):
#     estratos = pd.DataFrame(perfilGeotecnico.objects.all().values())
#     datosI=pd.DataFrame(datosIniciales.objects.all().values())
    
#     servicio=pd.DataFrame(servicios.objects.all().values())

#     if len(servicio.index)>0 and len(datosI.index)>0 and len(estratos.index)>0:

#         F3=pd.to_numeric(servicio['fuerza3'])
#         hj=pd.to_numeric(estratos['espesorEstrato'])
#         Gama=pd.to_numeric(estratos['pesoEspecifico'])
#         #prof=pd.to_numeric(datosI['profundidadCimentacion'])[0]
#         modelo=datosI['modelo'][0]
#         FS=pd.to_numeric(datosI['factorResistencia'])[0]
        
#         j=0
#         q=np.repeat(float(0), [len(hj)], axis=0)
        
#         while j<len(hj):
#             q[0]=Gama[0]*prof
            
#             S=sum(hj)            

#             if prof<=S:
#                 q[j]=q[j-1]+ hj[j]*Gama[j] +(prof-hj[j])*Gama[j]
#                 fi=pd.to_numeric(list(estratos['friccionSuelo']))[j]
#                 C=pd.to_numeric(list(estratos['cohesionSuelo']))[j]             
               
#             j=j+1  


#         q=max(q)
#         Gama=(q/prof)

#         B=np.repeat(float(0), [len(F3)], axis=0)
#         Nq=math.exp(math.pi*math.tan(fi*(math.pi/180)))*pow(math.tan(math.pi/4+(fi/2)*(math.pi/180)),2)
#         Nc=(Nq-1)/math.tan(fi*(math.pi/180))
#         if modelo=='hansen':
#             Ny=1.5*(Nq-1)*math.tan(fi*(math.pi/180))
#         elif modelo=='Vesic':
#             Ny=2*(Nq+1)*math.tan(fi*(math.pi/180))
#         qu= [C*Nc+q*Nq+Gama*i*Ny/2 for i in B]
#         qa=[i/FS for i in qu]    

#         for i in range(len(F3)):
#             while qa[i]*pow(B[i],2)<F3[i]:
#                 qu= [C*Nc+q*Nq+Gama*i*Ny/2 for i in B]
#                 qa=[i/FS for i in qu]
#                 B[i]=B[i]+0.01
        
#         for i in range(len(B)):
#             B[i]=B[i]+0.01
        
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

#         return JsonResponse(pd.DataFrame({'B':list(B)}).to_dict('records'), safe=False)
       
#     else:
#         if v==True:
#             return [0]
#         return JsonResponse({})






# def Asentamiento1(B,L,prof=1,aSi=False,aSc=False,aSt=False,v=False, salida=False,s1=False):
    
#     servicio = pd.DataFrame(servicios.objects.all().values())
#     estratos=pd.DataFrame(perfilGeotecnico.objects.all().values())
#     datosI=pd.DataFrame(datosIniciales.objects.all().values())

#     if len(datosI.index)>0 and len(estratos.index)>0 and len(servicio.index)>0:

#         F3=list(pd.to_numeric(list(servicio['fuerza3'])))

#         #prof=pd.to_numeric(datosI['profundidadCimentacion'])[0]
#         NF=pd.to_numeric(datosI['nivelFeatico'])[0]
#         estratos=estratos.sort_values('idEstrato')

#         Lx=[L[i]/2 for i in range(len(L))]
#         Bx=[B[i]/2 for i in range(len(B))]
#         product = [x*y for x,y in zip(B,L)]
#         q=[F3[x]/product[x] for x in range(len(product))]

#         u=pd.to_numeric(list(estratos['relacionPoisson']))
#         Es=pd.to_numeric(list(estratos['moduloElasticidad']))
#         Cc=pd.to_numeric(list(estratos['indiceDeComprension']))
#         Cr=pd.to_numeric(list(estratos['indiceDeExpansibilidad']))
#         Sp=pd.to_numeric(list(estratos['presionDepreconsolidacion']))
#         e0=pd.to_numeric(list(estratos['relacionDeVacioInicial']))
#         hj=pd.to_numeric(list(estratos['espesorEstrato']))
#         Gama=pd.to_numeric(list(estratos['pesoEspecifico']))

#         ZI=np.arange(pd.to_numeric(datosI['h'])[0],sum(hj),pd.to_numeric(datosI['h'])[0])
#         hi=np.repeat([float(0)],len(ZI), axis=0)
#         hi[0]=ZI[0]
#         for i in range(1,len(ZI)):
#             hi[i]=pd.to_numeric(datosI['h'])[0]

#         Zcarg=[ZI[i]-prof for i in range(len(ZI))]
#         for i in range(len(Zcarg)):
#             if Zcarg[i]<0:
#                 Zcarg[i]=0


#         Crr=np.repeat([float(0)],len(ZI), axis=0)
#         Ccc=np.repeat([float(0)],len(ZI), axis=0)
#         SP=np.repeat([float(0)],len(ZI), axis=0)
#         E0=np.repeat([float(0)],len(ZI), axis=0)
#         Hj=np.repeat([float(0)],len(ZI), axis=0)
#         GAMA=np.repeat([float(0)],len(ZI), axis=0)
#         ES=np.repeat([float(0)],len(ZI), axis=0)
#         uu=np.repeat([float(0)],len(ZI), axis=0)

#         h=np.repeat([float(0)],len(hj), axis=0)
#         h[0]=hj[0]
#         for i in range(1,len(hj)):
#             h[i]=h[i-1]+hj[i]


#         s=0
#         for i in range(len(ZI)):

#             if ZI[i]<=h[s]:
#                 Crr[i]=Cr[s]
#                 Ccc[i]=Cc[s]
#                 E0[i]=e0[s]
#                 GAMA[i]=Gama[s]
#                 SP[i]=Sp[s]
#                 Hj[i]=hj[s]
#                 ES[i]=Es[s]
#                 uu[i]=u[s]
#             else:
#                 s=s+1
#                 Crr[i]=Cr[s]
#                 Ccc[i]=Cc[s]
#                 E0[i]=e0[s]
#                 GAMA[i]=Gama[s]
#                 SP[i]=Sp[s]
#                 Hj[i]=hj[s]
#                 ES[i]=Es[s]
#                 uu[i]=u[s]


#         for i in range(len(ZI)):
#             if ZI[i]<=prof:
#                 Ccc[i]=0
#                 Crr[i]=0

#         iSz=[hi[i]*GAMA[i] for i in range(len(hi))]
#         Sz=np.repeat([float(0)],len(iSz), axis=0)
#         Sz[0]=iSz[0]
#         for i in range(1,len(Sz)):
#             Sz[i]=Sz[i-1]+iSz[i]

#         gw=9.81
#         hw=[ZI[i]-NF for i in range(len(ZI))]
#         for i in range(len(hw)):
#             if hw[i]<0:
#                 hw[i]=0
#         U=[gw*x for x in hw]


#         #esfuerzos efectivos

#         Szp=[Sz[i]-U[i] for i in range(len(U))]
#         R1=np.repeat([float(0)],len(Zcarg), axis=0)
#         R2=np.repeat([float(0)],len(Zcarg), axis=0)
#         R3=np.repeat([float(0)],len(Zcarg), axis=0)
#         dsz=np.repeat([float(0)],len(Zcarg), axis=0)
#         dsx=np.repeat([float(0)],len(Zcarg), axis=0)
#         dsy=np.repeat([float(0)],len(Zcarg), axis=0)
#         DU=np.repeat([float(0)],len(Zcarg), axis=0)
#         dszp=np.repeat([float(0)],len(Zcarg), axis=0)
#         dsxp=np.repeat([float(0)],len(Zcarg), axis=0)
#         dsyp=np.repeat([float(0)],len(Zcarg), axis=0)
#         Dz=np.repeat([float(0)],len(Zcarg), axis=0)

#         ASI=np.repeat([float(0)],len(B), axis=0)
#         ASC=np.repeat([float(0)],len(B), axis=0)
#         AST=np.repeat([float(0)],len(B), axis=0)
#         for j in range(len(B)):
#             for k in range(len(Zcarg)):
#                 R1[k]=math.sqrt(Lx[j]**2+Zcarg[k]**2)
#                 R2[k]=math.sqrt(Bx[j]**2+Zcarg[k]**2)
#                 R3[k]=math.sqrt(Lx[j]**2+Bx[j]**2+Zcarg[k]**2)
#                 if Zcarg[k]==0:
#                     dsz[k]=0
#                     dsx[k]=0
#                     dsy[k]=0
#                 else:

#                     dsz[k]=4*(q[j]/(2*math.pi))*(math.atan(((Lx[j])*(Bx[j]))/(Zcarg[k]*R3[k]))+(((Lx[j])*(Bx[j])*Zcarg[k])/R3[k])*((1/(R1[k]**2))+(1/(R2[k]**2))))
#                     dsx[k]=4*(q[j]/(2*math.pi))*(math.atan((((Lx[j]*Bx[j])/(Zcarg[k]*R3[k]))))- (Lx[j]*Bx[j]*Zcarg[k])/((R1[k]**2)*R3[k]))
#                     dsy[k]=4*(q[j]/(2*math.pi))*(math.atan((((Lx[j]*Bx[j])/(Zcarg[k]*R3[k]))))- (Lx[j]*Bx[j]*Zcarg[k])/((R2[k]**2)*R3[k]))



#                 DU[k]=(dsz[k]+dsy[k]+dsx[k])/3
#                 Dz[k]=((dsz[k]/ES[k])-(uu[k]/ES[k])*(dsx[k]+dsy[k]))*hi[k]

#                 dszp[k]=dsz[k]-DU[k]
#                 dsxp[k]=dsx[k]-DU[k]
#                 dsyp[k]=dsy[k]-DU[k]



#             Szfp=[Szp[i]+dszp[i] for i in range(len(dszp))]



#             Sc=np.repeat([float(0)],len(Szfp), axis=0)
#             for k in range(len(Szfp)):
#                 if datosI['OCR'][0]=="Si":
#                    C1=hi[k]/(1+E0[k])
#                    term1=Ccc[k]*C1
#                    log=math.log10(Szfp[k]/Szp[k])
#                    Sc[k]=term1*log
#                 else:
#                     if SP[k]>Szfp[k] and Szfp[k]/Szp[k]>0:
#                        C1=hi[k]/(1+E0[k])
#                        term1=Crr[k]*C1
#                        log=math.log10(Szfp[k]/Szp[k])
#                        Sc[k]=term1*log
#                     elif SP[k]>Szp[k] and SP[k]<Szfp[k]:
#                        C1=hi[k]/(1+E0[k])
#                        Sc[k]=C1*(Crr[k]*math.log10(SP[k]/Szp[k]) + Ccc[k]*math.log10(Szfp[k]/SP[k]))
#                     elif Szfp[k]/Szp[k]>0:
#                         C1=hi[k]/(1+E0[k])
#                         term1=Ccc[k]*C1
#                         log=math.log10(Szfp[k]/Szp[k])
#                         Sc[k]=term1*log
#                     else:
#                         Sc[k]=0


#             ASI[j]=sum(Dz)
#             ASC[j]=sum(Sc)
#             AST[j]=sum(Dz)+sum(Sc)


#         data=pd.DataFrame({'q':q[0],'L':L[0],'B':B[0],'hi':hi,'Gama':GAMA,'ZI':ZI,'iSz':iSz,'Sz':Sz,'gw':gw,'hw':hw,'U':U,'Szp':Szp,'Zcarg':Zcarg,'R1':R1,'R2':R2,'R3':R3,'dsz':dsz,'dsx':dsx,'dsy':dsy,'DU':DU,'Dz':Dz,'dszp':dszp,'Szfp':Szfp,'Sc':Sc})

#         data2=pd.DataFrame({'joint':servicio['joints'],'B_Asentamiento':B,'L_Asentamiento':L,'AsentamientoInmediatos':ASI,'AsentamientoporConsolidacion':ASC,'Asentamientototal':AST})

#         if salida==True:
#             return data
#         if s1==True:
#             return data2


#         if aSi==True:
#             return ASI
#         elif aSc==True:
#             return ASC
#         elif aSt==True:
#             return  AST

#         return JsonResponse(data2.to_dict('records'),safe=False)

#     else:
#         if v==True:
#             return pd.DataFrame({'B_Asentamiento':[0]})
#         return JsonResponse({})



# def Asentamiento3(prof=1,s=True):
#     if sum(Asentamiento1(B,L,prof=prof,aSt=True,v=True))>0:
#         datosI=pd.DataFrame(datosIniciales.objects.all().values())
#         maxAsen=pd.to_numeric(datosI['asentamimientoMaximo'])[0]
#         Asen_total=Asentamiento1(B,L,prof=prof,aSt=True)
#         for i in range(len(Asen_total)):
#             while Asen_total[i]>maxAsen:
#                 B[i]=B[i]+pd.to_numeric(datosI['aumentoB'])[0]
#                 L[i]=L[i]+pd.to_numeric(datosI['aumentoB'])[0]
#                 Asen_total= Asentamiento1(B,L,prof=prof,aSt=True)

#         data=Asentamiento1(B,L,prof=prof,s1=True)
#         if s==True:
#             return data

#         return JsonResponse(data.to_dict('records'),safe=False)

#     else:
#         if s==True:
#             return JsonResponse(pd.DataFrame({'B_Asentamiento':[0],'L_Asentamiento':[0]}).to_dict('records'),safe=False)
#         return JsonResponse({})


# def dimensionMayor2(prof=1,s=False):
#     bAsen=Asentamiento3(prof=prof,s=True)
#     if sum(list(Cap2(prof=prof,bcp=True)))>0 and sum(bAsen['B_Asentamiento'])>0:
#         Bcp=list(Cap2(prof=prof,bcp=True))
#         bAsen=list(bAsen['B_Asentamiento'])
#         Bmayor=np.repeat([float(0)],len(Bcp), axis=0)
#         for i in range(len(Bcp)):
#             if Bcp[i]>=bAsen[i]:
#                 Bmayor[i]=Bcp[i]
#             else:
#                 Bmayor[i]=bAsen[i]
#         B=Bmayor
#         L=Bmayor
#         Asen=Asentamiento1(B,L,prof=prof,s1=True)
#         resultado=pd.DataFrame({'DimensionMayor':Bmayor,'A_Elastico':Asen['AsentamientoInmediatos'],'A_consolidacion':Asen['AsentamientoporConsolidacion'],'A_Total':Asen['Asentamientototal']})
#         if s==True:
#             return resultado
#         return JsonResponse(resultado.to_dict('records'),safe=False)
#     else:
#         if s==True:
#             return pd.DataFrame({'DimensionMayor':[0]})
#         return JsonResponse({})



# def Excentricidades2(prof=1,s=True):
#     DimensionMayor=dimensionMayor2(prof=prof,s=True)
#     servicio = pd.DataFrame(servicios.objects.all().values())
#     datosI=pd.DataFrame(datosIniciales.objects.all().values())
#     if sum(DimensionMayor['DimensionMayor'])>0:
#         F3=list(pd.to_numeric(list(servicio['fuerza3'])))
#         M1=pd.to_numeric(servicio["momento1"])
#         M2=pd.to_numeric(servicio["momento2"])
#         lado_neto=list(DimensionMayor['DimensionMayor'])

#         Ex=[abs(M1[i]/F3[i]) for i in range(len(F3))]
#         Ey=[abs(M2[i]/F3[i]) for i in range(len(F3))]
#         Bz=[2*(lado_neto[i]/2+abs(Ex[i])) for i in range(len(lado_neto))]
#         Lz=[2*(lado_neto[i]/2+abs(Ey[i])) for i in range(len(lado_neto))]
#         for j in range(len(F3)):
#             while Ex[j]>(1/6)*Bz[j]:
#                 Bz[j]=Bz[j]+pd.to_numeric(datosI['aumentoB'])[0]

#         for k in range(len(F3)):
#             while Ey[k]>(1/6)*Lz[k]:
#                 Lz[k]=Lz[k]+pd.to_numeric(datosI['aumentoB'])[0]
#         B=Bz
#         L=Lz
#         BL=Asentamiento1(B,L,prof=prof,s1=True)

#         data=pd.DataFrame({'joint':servicio['joints'],'B_Excentricidad':Bz,'L_Excentricidad':Lz,'AsentamientoElastico':BL['AsentamientoInmediatos'],'AsentamientoPorConsolidacion':BL['AsentamientoporConsolidacion'],'Asentamientototal':BL['Asentamientototal']})
#         if s==True:
#             return data
#         return JsonResponse(data.to_dict('records'),safe=False)
#     else:
#         if s==True:
#             return pd.DataFrame({'B_Excentricidad':[0],'L_Excentricidad':[0]})
#         return JsonResponse({})




# def AsenD2(prof=1,consola=False):
#     diferencial= pd.DataFrame(diferenciales.objects.all().values())
#     datosI=pd.DataFrame(datosIniciales.objects.all().values())
#     dim=Excentricidades2(prof=prof,s=True)

#     if sum(dim['B_Excentricidad'])>0 and len(diferencial.index)>0 and len(dim['B_Excentricidad'])>1:
#         B=list(dim['B_Excentricidad'])
#         L=list(dim['L_Excentricidad'])
#         distancias=pd.to_numeric(diferencial["distancias"])
#         joint2=pd.to_numeric(diferencial["joints"])
#         Vecinos=pd.to_numeric(diferencial["vecinos"])
#         joint=pd.to_numeric(servicio["joints"])
#         Asen_total=Asentamiento1(B,L,prof=prof,aSt=True,v=True)
#         criterio=list(pd.to_numeric(diferencial['criterioDiferencial']))

#         DH_DIF_Adm=[distancias[x]/criterio[x] for x in range(len(distancias))]
#         DH_DIF_Cal=np.repeat([float(0)],len(joint2), axis=0)
#         for i in range(len(joint2)):
#             DH_DIF_Cal[i]=float(abs((Asen_total[int(np.where([joint[x]==joint2[i] for x in range(len(joint))])[0])]-Asen_total[int(np.where([joint[x]==Vecinos[i] for x in range(len(joint))])[0])])*1000))


#         for i in range(len(DH_DIF_Adm)):
#             while  DH_DIF_Adm[i]<DH_DIF_Cal[i]:
#                 Joi1=joint[int(np.where([joint[x]==joint2[i] for x in range(len(joint))])[0])]
#                 Joi2=joint[int(np.where([joint[x]==Vecinos[i] for x in range(len(joint))])[0])]
#                 A1=Asen_total[int(np.where([joint[x]==joint2[i] for x in range(len(joint))])[0])]
#                 A2=Asen_total[int(np.where([joint[x]==Vecinos[i] for x in range(len(joint))])[0])]
#                 if A1>A2:
#                     B[int(np.where([joint[x]==Joi1 for x in range(len(joint))])[0])]=B[int(np.where([joint[x]==Joi1 for x in range(len(joint))])[0])]+pd.to_numeric(datosI['aumentoB'])[0]
#                     L[int(np.where([joint[x]==Joi1 for x in range(len(joint))])[0])]=L[int(np.where([joint[x]==Joi1 for x in range(len(joint))])[0])]+pd.to_numeric(datosI['aumentoB'])[0]

#                 elif A2>A1:
#                     B[int(np.where([joint[x]==Joi2 for x in range(len(joint))])[0])]=B[int(np.where([joint[x]==Joi2 for x in range(len(joint))])[0])]+pd.to_numeric(datosI['aumentoB'])[0]
#                     L[int(np.where([joint[x]==Joi2 for x in range(len(joint))])[0])]=L[int(np.where([joint[x]==Joi2 for x in range(len(joint))])[0])]+pd.to_numeric(datosI['aumentoB'])[0]

#                 elif A1==A2:
#                     B[int(np.where([joint[x]==Joi1 for x in range(len(joint))])[0])]=B[int(np.where([joint[x]==Joi1 for x in range(len(joint))])[0])]+pd.to_numeric(datosI['aumentoB'])[0]
#                     B[int(np.where([joint[x]==Joi2 for x in range(len(joint))])[0])]=B[int(np.where([joint[x]==Joi2 for x in range(len(joint))])[0])]+pd.to_numeric(datosI['aumentoB'])[0]
#                     L[int(np.where([joint[x]==Joi1 for x in range(len(joint))])[0])]=L[int(np.where([joint[x]==Joi1 for x in range(len(joint))])[0])]+pd.to_numeric(datosI['aumentoB'])[0]
#                     L[int(np.where([joint[x]==Joi2 for x in range(len(joint))])[0])]=L[int(np.where([joint[x]==Joi2 for x in range(len(joint))])[0])]+pd.to_numeric(datosI['aumentoB'])[0]


#                 Asen_total=Asentamiento1(B,L,prof=prof,aSt=True,v=True)
#                 DH_DIF_Cal[i]=abs(A1-A2)*1000

#         ASI=Asentamiento1(B,L,prof=prof,aSi=True,v=True)
#         ASC=Asentamiento1(B,L,prof=prof,aSc=True,v=True)
#         AST=Asentamiento1(B,L,prof=prof,aSt=True,v=True)
#         data= pd.DataFrame({'B':B,'L':L,'A_Elastico':ASI,'A_consolidacion':ASC,'A_Total':AST})
#         if consola==True:
#             return  data

#         return JsonResponse(data.to_dict('records'), safe=False)

#     else:
#         if consola==True:
#             return  pd.DataFrame({'B':[0],'L':[0]})

#         return JsonResponse({})




# def dimensionesConstruccion2(prof=1,s=True):
#     datosI=pd.DataFrame(datosIniciales.objects.all().values())
#     Personalizado=pd.DataFrame(dimensionesPersonalizadas.objects.all().values())
#     BL=AsenD2(prof=prof,consola=True)
#     dim=Excentricidades2(prof=prof,s=True)
#     Be=dim['B_Excentricidad']
#     Le=dim['L_Excentricidad']
#     Bd=list(BL['B'])
#     Ld=list(BL['L'])
#     if sum(Bd)>0 or sum(Be)>0:
#         if sum(Be)>0 and len(Be)==1:
#             B=Be
#             L=Le
#             B_Const=[round(B[i],int(datosI['cifrasDecimales'][0])) for i in range(len(B))]
#             L_Const=[round(L[i],int(datosI['cifrasDecimales'][0])) for i in range(len(L))]
#         elif sum(Bd)>0 and len(Bd)>1:
#             B=Bd
#             L=Ld
#             B_Const=[round(B[i],int(datosI['cifrasDecimales'][0])) for i in range(len(B))]
#             L_Const=[round(L[i],int(datosI['cifrasDecimales'][0])) for i in range(len(L))]

#         else:
#             dimBL=Asentamiento3(prof=prof,s=True)
#             B=list(dimBL['B_Asentamiento'])
#             L=list(dimBL['L_Asentamiento'])
#             B_Const=[round(B[i],int(datosI['cifrasDecimales'][0])) for i in range(len(B))]
#             L_Const=[round(L[i],int(datosI['cifrasDecimales'][0])) for i in range(len(L))]





#         for i in range(len(B_Const)):
#             if B_Const[i]<1:
#                 B_Const[i]=1
#             if L_Const[i]<1:
#                 L_Const[i]=1
#             if B_Const[i]<B[i]:
#                 B_Const[i]=B_Const[i]+pd.to_numeric(datosI['salto'])[0]
#             if L_Const[i]<L[i]:
#                 L_Const[i]=L_Const[i]+pd.to_numeric(datosI['salto'])[0]


#         if len(Personalizado.index)>0 and datosI['personalizado'][0]=='si':
#             B_Const=list(pd.to_numeric(Personalizado['bpersonalizado']))
#             L_Const=list(pd.to_numeric(Personalizado['lpersonalizado']))

#         ASI=Asentamiento1(B_Const,L_Const,prof=prof,aSi=True,v=True)
#         ASC=Asentamiento1(B_Const,L_Const,prof=prof,aSc=True,v=True)
#         AST=Asentamiento1(B_Const,L_Const,prof=prof,aSt=True,v=True)

#         data=pd.DataFrame({'B_construcion':B_Const,'L_construcion':L_Const,'Asen_Elastico':ASI,'Asen_consolidacion':ASC,'Asen_Total':AST})
#         if s==True:
#             return data

#         return JsonResponse(data.to_dict('records'), safe=False)
#     else:
#         if s==True:
#             return pd.DataFrame({'B_construcion':[0],'L_construcion':[0]})
#         return JsonResponse({})




# def cant_ObraPres2(prof=1,R=False):
#     ValoresUnitarios=pd.DataFrame(preciosUnitarios.objects.all().values())
#     Personalizado=pd.DataFrame(dimensionesPersonalizadas.objects.all().values())
#     datosI=pd.DataFrame(datosIniciales.objects.all().values())
#     datosII=pd.DataFrame(datosPrimary.objects.all().values())

#     BL=dimensionesConstruccion2(prof=prof,s=True)

#     if len(ValoresUnitarios.index)>0 and len(datosI.index)>0 and len(datosII.index)>0:
#         if sum(BL['B_construcion'])>0 and datosI['personalizado'][0]=='no':
#             B=BL['B_construcion']
#             L=BL['L_construcion']
#         elif sum(BL['B_construcion'])>=0 and  datosI['personalizado'][0]=='si' and len(Personalizado.index)>0:
#             B=list(pd.to_numeric(Personalizado['bpersonalizado']))
#             L=list(pd.to_numeric(Personalizado['lpersonalizado']))
#         else:
#             return JsonResponse({})


#         #prof=pd.to_numeric(datosI['profundidadCimentacion'])[0]
#         EspesorSolado=pd.to_numeric(datosII['espesorSolado'])[0]

#         #Excavación
#         Area=list(np.multiply(list(B),list(L)))
#         Exc=[(prof+EspesorSolado)*i for i in Area]

#         #Solado
#         solado=[EspesorSolado*x for x in Area]

#         #Concreto Zapatas
#         MayorBL=np.repeat([float(0)],len(B), axis=0)
#         MenorBL=np.repeat([float(0)],len(B), axis=0)
#         for i in range(len(B)):
#             if  B[i]>=L[i]:
#                 MayorBL[i]=B[i]
#                 MenorBL[i]=L[i]
#             if L[i]>B[i]:
#                 MayorBL[i]=L[i]
#                 MenorBL[i]=B[i]

#         if datosII['condicion'][0]=='mayorBL':
#             ConcZ=np.multiply([pd.to_numeric(datosII['espesorZapata'])[0]*x for x in MayorBL], Area)
#             ConcP=[prof*pow(pd.to_numeric(datosII['espesorPedestal'])[0]*MayorBL[i],2) for i in range(len(MayorBL))]

#         elif datosII['condicion'][0]=='menorBL':
#             ConcZ=np.multiply([pd.to_numeric(datosII['espesorZapata'])[0]*x for x in MenorBL], Area)
#             ConcP=[prof*pow(pd.to_numeric(datosII['espesorPedestal'])[0]*MenorBL[i],2) for i in range(len(MenorBL))]
#         else:
#             ConcZ=np.multiply([pd.to_numeric(datosII['espesorZapata'])[0]*x for x in MenorBL], Area)
#             ConcP=[prof*pow(pd.to_numeric(datosII['espesorPedestal'])[0]*MenorBL[i],2) for i in range(len(MenorBL))]


#         Relleno=[Exc[i]-solado[i]-ConcP[i]-ConcZ[i] for i in range(len(B))]
#         for i in range(len(Relleno)):
#             if Relleno[i]<=0:
#                 Relleno[i]=0

#         #Presupuesto

#         PrecioExc=pd.to_numeric(ValoresUnitarios['precioExc'])[0]/1000000
#         VPExc=[i*PrecioExc for i in Exc]

#         PrecioConcZ=pd.to_numeric(ValoresUnitarios['precioConcZ'])[0]/1000000
#         VPConcZ=[i*PrecioConcZ for i in ConcZ]

#         PrecioConcP=pd.to_numeric(ValoresUnitarios['precioConcP'])[0]/1000000

#         VPConcP=[i*PrecioConcP for i in list(ConcP)]

#         PrecioRelleno=pd.to_numeric(ValoresUnitarios['precioRelleno'])[0]/1000000

#         VPRelleno=[i*PrecioRelleno for i in Relleno]

#         Preciosolado=pd.to_numeric(ValoresUnitarios['preciosolado'])[0]/1000000
#         VPsolado=[i*Preciosolado for i in solado]
#         AceroZapata=[pd.to_numeric(datosII['cuantiaAceroZapata'])[0]*i for i in ConcZ]
#         AceroPedestal=[pd.to_numeric(datosII['cuantiaAceroPedestal'])[0]*i for i in ConcP]
#         PrecioAceroZapata=pd.to_numeric(ValoresUnitarios['precioAceroZapata'])[0]/1000000
#         PrecioAceroPedestal=pd.to_numeric(ValoresUnitarios['precioAceroPedestal'])[0]/1000000
#         VpAceroZapata=[PrecioAceroZapata*i for i in AceroZapata]
#         VpAceroPedestal=[PrecioAceroPedestal*i for i in AceroPedestal]
#         VPZapata=[VPExc[i]+VPConcZ[i] +VPConcP[i]+VPRelleno[i]+VPsolado[i]+VpAceroZapata[i]+VpAceroPedestal[i] for i in range(len(B))]
#         SubTotal=sum(VPZapata)
#         data=pd.DataFrame({'Profundidad':prof,'B':[round(i,1) for i in B],'L':[round(i,1) for i in L],'Excavacion':[round(i,1) for i in Exc],'solado':[round(i,2) for i in solado],'ConcretoZapata':[round(i,2) for i in ConcZ],'ConcretoPedestal':[round(i,2) for i in ConcP],'Relleno':[round(i,2) for i in Relleno],'ValorParcialExcavacion':[round(i,2) for i in VPExc],'ValorParcialSolado':[round(i,2) for i in VPsolado],'ValorParcialConcretoZapata':[round(i,2) for i in VPConcZ],'ValorParcialConcretoPedestal':[round(i,2) for i in VPConcP],'VPRelleno':[round(i,2) for i in VPRelleno],'AceroZapata':[round(i,2) for i in AceroZapata],'AceroPedestal':[round(i,2) for i in AceroPedestal],'VpAceroZapata':[round(i,2) for i in VpAceroZapata],'VpAceroPedestal':[round(i,2) for i in VpAceroPedestal],'VPZapata':[round(i,2) for i in VPZapata],'SubTotal':round(SubTotal,1)})

#         if R==True:
#             return round(SubTotal,3)

#         return JsonResponse(data.to_dict('records'), safe=False)

#     else:
#         if R==True:
#             return  pd.DataFrame({'B':[0],'L':[0]})
#         return JsonResponse({})




# def prVScosto(r=False):
#     profundidad=pd.DataFrame(profundidades.objects.all().values())
#     if len(profundidad.index)>0 and len(B)>0:
#         w= list(pd.to_numeric(profundidad['profundidades']))
#         costo=np.repeat([float(0)],len(w), axis=0)
#         for k in range(len(w)):
#             costo[k]=cant_ObraPres2(prof=w[k],R=True)
        

#         base=pd.DataFrame({'prof':[-i for i in w],'costo':costo})

#         return JsonResponse(base.to_dict('records'), safe=False)
#     else:
#         return JsonResponse()

    

# # x = costo
# # y =[-i for i in w]

# # plt.plot(x,y)
# # plt.xlabel('costo')
# # plt.ylabel('profundidad')
# # plt.title('profundidad vs coto')
# # plt.savefig("plot.jpg")



























# ########################################################################################################################################

# # #Capacidad portante de Cimentación Profunda

# def alfa(cohesion):
#         x=[0,7.5,20,100]
#         y=[1.1,0.8,0.5,0.5]
#         if any([x[i]>=cohesion for i in range(len(x))]):
#             i=1
#         else:
#             i=len(x)-1
#         x1=x[i-1]
#         x2=x[i]
#         y1=y[i-1]
#         y2=y[i]
#         alfa=((y2-y1)/(x2-x1))*(cohesion-x2)+y2
#         return alfa


# def Io(L_d ,db_d):
#     x=[0,1.25,2.5,5,10,15,20,25,30,35,40,45,50,100]
#     y=[1,2,3]
#     ii=L_d       
#     jj = db_d
    
#     xy=np.zeros((14, 3))
#     xy[0,0]=0.7
#     xy[1,0]=0.4
#     xy[2,0]=0.3
#     xy[3,0]=0.21
#     xy[4,0]=0.15
#     xy[5,0]=0.11
#     xy[6,0]=0.09
#     xy[7,0]=0.075
#     xy[8,0]=0.065
#     xy[9,0]=0.059
#     xy[10,0]=0.052
#     xy[11,0]=0.048
#     xy[12,0]=0.045
#     xy[13,0]=0.0254

#     xy[0,1]=0.3
#     xy[1,1]=0.28
#     xy[2,1]=0.28
#     xy[3,1]=0.18
#     xy[4,1]=0.13
#     xy[5,1]=0.1
#     xy[6,1]=0.084
#     xy[7,1]=0.07
#     xy[8,1]=0.062
#     xy[9,1]=0.056
#     xy[10,1]=0.051
#     xy[11,1]=0.0465
#     xy[12,1]=0.0435
#     xy[13,1]=0.0254
   

#     xy[0,2]=0.25
#     xy[1,2]=0.24
#     xy[2,2]=0.2
#     xy[3,2]=0.16
#     xy[4,2]=0.12
#     xy[5,2]=0.09
#     xy[6,2]=0.076
#     xy[7,2]=0.066
#     xy[8,2]=0.06
#     xy[9,2]=0.052
#     xy[10,2]=0.05
#     xy[11,2]=0.045
#     xy[12,2]=0.042
#     xy[13,2]=0.0254

    
#     for s in range(len(x)):
#         if x[s]>ii:
#             i=s+1
#             break
#         else:
#             i=len(x)-1
    
#     if i>=len(x):
#         i=i-1
    
#     for s in range(len(y)):
#         if y[s]>jj:
#             j=s+1
#             break
#         else:            
#             j=len(y)-1
    
#     if j>=len(y):
#         j=j-1

    
#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i - 1, j - 1]
#     y2 = xy[i - 1, j]
#     y3 = (y2 - y1)/(x2 - x1)*(jj - x2) + y2   
    
#     y1 = xy[i, j - 1]
#     y2 = xy[i, j]
#     y4 = (y2 - y1)/(x2 - x1)*(jj - x2) + y2
#     Io = (y4 - y3)/(x[i] - x[i - 1])*(ii - x[i]) + y4
#     if Io>1:
#         Io = 1
#     elif Io < 0.0254:
#         Io = 0.0254
#     return Io


# def Rk(K , L_d):
    
#     ii = K
#     x=[10,30,50,100,300,500,1000,3000,5000,10000]
    
#     jj = L_d
#     y=[1,2,5,10,25,50,100]
    
#     xy=np.zeros((10, 7))

#     xy[0, 0] = 1.1
#     xy[1, 0] = 1.05
#     xy[2, 0] = 1.025
#     xy[3, 0] = 1
#     xy[4, 0] = 1
#     xy[5, 0] = 1
#     xy[6, 0] = 1
#     xy[7, 0] = 1
#     xy[8, 0] = 1
#     xy[9, 0] = 1
#     xy[0, 1] = 1.2
#     xy[1, 1] = 1.1
#     xy[2, 1] = 1.05
#     xy[3, 1] = 1.025
#     xy[4, 1] = 1
#     xy[5, 1] = 1
#     xy[6, 1] = 1
#     xy[7, 1] = 1
#     xy[8, 1] = 1
#     xy[9, 1] = 1
#     xy[0, 2] = 1.55
#     xy[1, 2] = 1.25
#     xy[2, 2] = 1.15
#     xy[3, 2] = 1.1
#     xy[4, 2] = 1.05
#     xy[5, 2] = 1.025
#     xy[6, 2] = 1
#     xy[7, 2] = 1
#     xy[8, 2] = 1
#     xy[9, 2] = 1
#     xy[0, 3] = 2.25
#     xy[1, 3] = 1.6
#     xy[2, 3] = 1.4
#     xy[3, 3] = 1.3
#     xy[4, 3] = 1.1
#     xy[5, 3] = 1.05
#     xy[6, 3] = 1.025
#     xy[7, 3] = 1
#     xy[8, 3] = 1
#     xy[9, 3] = 1
#     xy[0, 4] = -10000
#     xy[1, 4] = 2.8
#     xy[2, 4] = 2.2
#     xy[3, 4] = 1.9
#     xy[4, 4] = 1.3
#     xy[5, 4] = 1.2
#     xy[6, 4] = 1.12
#     xy[7, 4] = 1.05
#     xy[8, 4] = 1.025
#     xy[9, 4] = 1
#     xy[0, 5] = -10000
#     xy[1, 5] = -10000
#     xy[2, 5] = 4
#     xy[3, 5] = 2.85
#     xy[4, 5] = 2
#     xy[5, 5] = 1.5
#     xy[6, 5] = 1.38
#     xy[7, 5] = 1.1
#     xy[8, 5] = 1.05
#     xy[9, 5] = 1.025
#     xy[0, 6] = -10000
#     xy[1, 6] = -10000
#     xy[2, 6] = -10000
#     xy[3, 6] = -10000
#     xy[4, 6] = 3
#     xy[5, 6] = 2.4
#     xy[6, 6] = 2
#     xy[7, 6] = 1.37
#     xy[8, 6] = 1.18
#     xy[9, 6] = 1.16

#     for s in range(len(x)):
#         if x[s]>ii:
#             i=s+1
#             break
#         else:
#             i=len(x)-1
    
#     if i>=len(x):
#         i=i-1
    
#     for s in range(len(y)):
#         if y[s]>jj:
#             j=s+1
#             break
#         else:            
#             j=len(y)-1
    
#     if j>=len(y):
#         j=j-1

#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i - 1, j - 1]
#     y2 = xy[i - 1, j]
#     y3 = (y2 - y1)/(x2 - x1)*(jj - x2) + y2
#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i, j - 1]
#     y2 = xy[i, j]
#     y4 = (y2 - y1)/(x2 - x1)*(jj - x2) + y2
#     Rk = (y4 - y3)/(x[i] - x[i - 1])*(ii - x[i]) + y4
#     if Rk < 1:
#         Rk = 1
#     return Rk





# ####################################

# def Rh(H_L, L_d ):
    
#     ii = H_L
#     x=[1,1.2,1.4,1.6,1.8,2,2.2,2.4,2.6,28,3]

#     jj = L_d
#     y=[1,2,5,10,25,50]
#     xy=np.zeros((11, 6))
#     xy[0, 0] = 0
#     xy[1, 0] = 0.05
#     xy[2, 0] = 0.18
#     xy[3, 0] = 0.28
#     xy[4, 0] = 0.38
#     xy[5, 0] = 0.45
#     xy[6, 0] = 0.55
#     xy[7, 0] = 0.65
#     xy[8, 0] = 0.78
#     xy[9, 0] = 0.88
#     xy[10, 0] = 1
#     xy[0, 1] = 0.12
#     xy[1, 1] = 0.15
#     xy[2, 2] = 0.35
#     xy[3, 1] = 0.45
#     xy[4, 1] = 0.55
#     xy[5, 1] = 0.6
#     xy[6, 1]= 0.7
#     xy[7, 1] = 0.75
#     xy[8, 1] = 0.82
#     xy[9, 1] = 0.9
#     xy[10, 1] = 1
#     xy[0, 2] = 0.05
#     xy[1, 2] = 0.4
#     xy[2, 2] = 0.55
#     xy[3, 2] = 0.65
#     xy[4, 2] = 0.68
#     xy[5, 2] = 0.75
#     xy[6, 2] = 0.78
#     xy[7, 2] = 0.85
#     xy[8, 2] = 0.86
#     xy[9, 2] = 0.92
#     xy[10, 2] = 1
#     xy[0, 3] = 0.1
#     xy[1, 3] = 0.5
#     xy[2, 3] = 0.65
#     xy[3, 3] = 0.7
#     xy[4, 3] = 0.75
#     xy[5, 3] = 0.79
#     xy[6, 3] = 0.83
#     xy[7, 3] = 0.865
#     xy[8, 3] = 0.9
#     xy[9, 3] = 0.93
#     xy[10, 3] = 1
#     xy[0, 4] = 0.3
#     xy[1, 4] = 0.65
#     xy[2, 4] = 0.72
#     xy[3, 4] = 0.75
#     xy[4, 4] = 0.81
#     xy[5, 4] = 0.84
#     xy[6, 4] = 0.85
#     xy[7, 4] = 0.88
#     xy[8, 4] = 0.915
#     xy[9, 4] = 0.94
#     xy[10, 4] = 1
#     xy[0, 5] = 0.4
#     xy[1, 5] = 0.7
#     xy[2, 5] = 0.78
#     xy[3, 5] = 0.82
#     xy[4, 5] = 0.85
#     xy[5, 5] = 0.86
#     xy[6, 5] = 0.88
#     xy[7, 5] = 0.9
#     xy[8, 5] = 0.92
#     xy[9, 5] = 0.95
#     xy[10, 5] = 1
    
#     for s in range(len(x)):
#         if x[s]>ii:
#             i=s+1
#             break
#         else:
#             i=len(x)-1
    
#     if i>=len(x):
#         i=i-1
    
#     for s in range(len(y)):
#         if y[s]>jj:
#             j=s+1
#             break
#         else:            
#             j=len(y)-1
    
#     if j>=len(y):
#         j=j-1
    
   
        
#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i - 1, j - 1]
#     y2 = xy[i - 1, j]
#     y3 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i, j - 1]
#     y2 = xy[i, j]
#     y4 = (y2 - y1)/(x2 - x1)*(jj - x2) + y2
#     Rh = (y4-y3)/(x[i]-x[i-1]) * (ii-x[i]) + y4
#     if Rh > 1:
#         Rh = 1
#     return Rh



# def Rv(vs , K ):
#     ii = vs
#     x =[ 0,0.1,0.2,0.3,0.4,0.5]

#     jj = K
#     y =[ 100,500,1000,2000]

#     xy=np.zeros((6, 4))

#     xy[0, 0] = 0.875
#     xy[1, 0] = 0.9
#     xy[2, 0] = 0.925
#     xy[3, 0] = 0.95
#     xy[4, 0] = 0.975
#     xy[5, 0] = 1
#     xy[0, 1] = 0.84
#     xy[1, 1] = 0.872
#     xy[2, 1] = 0.904
#     xy[3, 1] = 0.936
#     xy[4, 1] = 0.968
#     xy[5, 1] = 1
#     xy[0, 2] = 0.83
#     xy[1, 2] = 0.864
#     xy[2, 2] = 0.898
#     xy[3, 2] = 0.932
#     xy[4, 2] = 0.966
#     xy[5, 2] = 1
#     xy[0, 3] = 0.825
#     xy[1, 3] = 0.86
#     xy[2, 3] = 0.895
#     xy[3, 3] = 0.93
#     xy[4, 3] = 0.965
#     xy[5, 3] = 1

    
#     for s in range(len(x)):
#         if x[s]>ii:
#             i=s+1
#             break
#         else:
#             i=len(x)-1
    
#     if i>=len(x):
#         i=i-1
    
#     for s in range(len(y)):
#         if y[s]>jj:
#             j=s+1
#             break
#         else:            
#             j=len(y)-1
    
#     if j>=len(y):
#         j=j-1

#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i - 1, j - 1]
#     y2 = xy[i - 1, j]
#     y3 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i, j - 1]
#     y2 = xy[i, j]
#     y4 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     Rv = (y4 - y3)/(x[i] - x[i - 1])*(ii - x[i]) + y4
#     if Rv > 1:
#         Rv = 1
#     return Rv
        




# # ##################





# def Rb75(Eb_Es,k):
#     ii = Eb_Es
#     x =[1,10,100,1000]
#     jj = k
#     y =[100,500,1000,5000,20000]
    
#     xy=np.zeros((4, 5))

#     xy[0, 0] = 1
#     xy[1, 0] = 0.985
#     xy[2, 0] = 0.975
#     xy[3, 0] = 0.965

#     xy[0, 1] = 1
#     xy[1, 1] = 0.95
#     xy[2, 1] = 0.89
#     xy[3, 1] = 0.88

#     xy[0, 2] = 1
#     xy[1, 2] = 0.90
#     xy[2, 2] = 0.80
#     xy[3, 2] = 0.78

#     xy[0, 3] = 1
#     xy[1, 3] = 0.78
#     xy[2, 3] = 0.46
#     xy[3, 3] = 0.38

#     xy[0, 4] = 1
#     xy[1, 4] = 0.72
#     xy[2, 4] = 0.25
#     xy[3, 4] = 0.12

#     for s in range(len(x)):
#         if x[s]>ii:
#             i=s+1
#             break
#         else:
#             i=len(x)-1
    
#     if i>=len(x):
#         i=i-1
    
#     for s in range(len(y)):
#         if y[s]>jj:
#             j=s+1
#             break
#         else:            
#             j=len(y)-1
    
#     if j>=len(y):
#         j=j-1

#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i - 1, j - 1]
#     y2 = xy[i - 1, j]
#     y3 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i, j - 1]
#     y2 = xy[i, j]
#     y4 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     Rb = (y4 - y3)/(x[i] - x[i - 1])*(ii - x[i]) + y4
#     if Rb > 1:
#         Rb = 1
#     return Rb


# def Rb50(Eb_Es,k):
#     ii = Eb_Es
#     x =[1,10,100,1000]
#     jj = k
#     y =[100,500,1000,5000,20000]
    
#     xy=np.zeros((4, 5))

#     xy[0, 0] = 1
#     xy[1, 0] = 0.98
#     xy[2, 0] = 0.96
#     xy[3, 0] = 0.95

#     xy[0, 1] = 1
#     xy[1, 1] = 0.90
#     xy[2, 1] = 0.78
#     xy[3, 1] = 0.75

#     xy[0, 2] = 1
#     xy[1, 2] = 0.82
#     xy[2, 2] = 0.64
#     xy[3, 2] = 0.60

#     xy[0, 3] = 1
#     xy[1, 3] = 0.70
#     xy[2, 3] = 0.30
#     xy[3, 3] = 0.20

#     xy[0, 4] = 1
#     xy[1, 4] = 0.62
#     xy[2, 4] = 0.18
#     xy[3, 4] = 0.08

#     for s in range(len(x)):
#         if x[s]>ii:
#             i=s+1
#             break
#         else:
#             i=len(x)-1
    
#     if i>=len(x):
#         i=i-1
    
#     for s in range(len(y)):
#         if y[s]>jj:
#             j=s+1
#             break
#         else:            
#             j=len(y)-1
    
#     if j>=len(y):
#         j=j-1

#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i - 1, j - 1]
#     y2 = xy[i - 1, j]
#     y3 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i, j - 1]
#     y2 = xy[i, j]
#     y4 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     Rb = (y4 - y3)/(x[i] - x[i - 1])*(ii - x[i]) + y4
#     if Rb > 1:
#         Rb = 1
#     return Rb
   
    
# def Rb25(Eb_Es,k):
#     ii = Eb_Es
#     x =[1,10,100,1000]
#     jj = k
#     y =[100,500,1000,2000]
    
#     xy=np.zeros((4, 4))

#     xy[0, 0] = 1
#     xy[1, 0] = 0.92
#     xy[2, 0] = 0.83
#     xy[3, 0] = 0.82

#     xy[0, 1] = 1
#     xy[1, 1] = 0.75
#     xy[2, 1] = 0.52
#     xy[3, 1] = 0.49

#     xy[0, 2] = 1
#     xy[1, 2] = 0.62
#     xy[2, 2] = 0.37
#     xy[3, 2] = 0.32

#     xy[0, 3] = 1
#     xy[1, 3] = 0.50
#     xy[2, 3] = 0.10
#     xy[3, 3] = 0.02

    

#     for s in range(len(x)):
#         if x[s]>ii:
#             i=s+1
#             break
#         else:
#             i=len(x)-1
    
#     if i>=len(x):
#         i=i-1
    
#     for s in range(len(y)):
#         if y[s]>jj:
#             j=s+1
#             break
#         else:            
#             j=len(y)-1
    
#     if j>=len(y):
#         j=j-1

#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i - 1, j - 1]
#     y2 = xy[i - 1, j]
#     y3 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i, j - 1]
#     y2 = xy[i, j]
#     y4 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     Rb = (y4 - y3)/(x[i] - x[i - 1])*(ii - x[i]) + y4
#     if Rb > 1:
#         Rb = 1
#     return Rb


# def Rb10(Eb_Es,k):
#     ii = Eb_Es
#     x =[1,10,100,1000]
#     jj = k
#     y =[100,500,1000,10000]
    
#     xy=np.zeros((4, 4))

#     xy[0, 0] = 1
#     xy[1, 0] = 0.60
#     xy[2, 0] = 0.46
#     xy[3, 0] = 0.43

#     xy[0, 1] = 1
#     xy[1, 1] = 0.45
#     xy[2, 1] = 0.18
#     xy[3, 1] = 0.15

#     xy[0, 2] = 1
#     xy[1, 2] = 0.40
#     xy[2, 2] = 0.11
#     xy[3, 2] = 0.09

#     xy[0, 3] = 1
#     xy[1, 3] = 0.37
#     xy[2, 3] = 0.08
#     xy[3, 3] = 0.001

    

#     for s in range(len(x)):
#         if x[s]>ii:
#             i=s+1
#             break
#         else:
#             i=len(x)-1
    
#     if i>=len(x):
#         i=i-1
    
#     for s in range(len(y)):
#         if y[s]>jj:
#             j=s+1
#             break
#         else:            
#             j=len(y)-1
    
#     if j>=len(y):
#         j=j-1

#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i - 1, j - 1]
#     y2 = xy[i - 1, j]
#     y3 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i, j - 1]
#     y2 = xy[i, j]
#     y4 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     Rb = (y4 - y3)/(x[i] - x[i - 1])*(ii - x[i]) + y4
#     if Rb > 1:
#         Rb = 1
#     return Rb


# def Rb5(Eb_Es,k):
#     ii = Eb_Es
#     x =[1,10,100,1000]
#     jj = k
#     y =[100,500,1000,5000,20000]
    
#     xy=np.zeros((4, 5))

#     xy[0, 0] = 1
#     xy[1, 0] = 0.50
#     xy[2, 0] = 0.30
#     xy[3, 0] = 0.28

#     xy[0, 1] = 1
#     xy[1, 1] = 0.38
#     xy[2, 1] = 0.10
#     xy[3, 1] = 0.08

#     xy[0, 2] = 1
#     xy[1, 2] = 0.35
#     xy[2, 2] = 0.08
#     xy[3, 2] = 0.05

#     xy[0, 3] = 1
#     xy[1, 3] = 0.34
#     xy[2, 3] = 0.05
#     xy[3, 3] = 0.02

#     xy[0, 4] = 1
#     xy[1, 4] = 0.33
#     xy[2, 4] = 0.04
#     xy[3, 4] = 0.01

    

#     for s in range(len(x)):
#         if x[s]>ii:
#             i=s+1
#             break
#         else:
#             i=len(x)-1
    
#     if i>=len(x):
#         i=i-1
    
#     for s in range(len(y)):
#         if y[s]>jj:
#             j=s+1
#             break
#         else:            
#             j=len(y)-1
    
#     if j>=len(y):
#         j=j-1

#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i - 1, j - 1]
#     y2 = xy[i - 1, j]
#     y3 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     x1 = y[j - 1]
#     x2 = y[j]
#     y1 = xy[i, j - 1]
#     y2 = xy[i, j]
#     y4 = (y2 - y1) / (x2 - x1) * (jj - x2) + y2
#     Rb = (y4 - y3)/(x[i] - x[i - 1])*(ii - x[i]) + y4
#     if Rb > 1:
#         Rb = 1
#     return Rb




# def Capp(r=False,P=False,Diam=False):
#     estratos=pd.DataFrame(perfilGeotecnico.objects.all().values())
#     Geo=pd.DataFrame(geometriaCimentacionProfunda.objects.all().values())
#     datosI=pd.DataFrame(datosIniciales.objects.all().values())

#     if len(datosI.index)>0 and len(Geo.index)>0 and len(estratos.index)>0:

#         estratos=estratos.sort_values('idEstrato')

#         prof=pd.to_numeric(Geo['prof'])[0]
#         A=[0,-0.1]



#         NF=pd.to_numeric(datosI['nivelFeatico'])[0]
#         FS=pd.to_numeric(datosI['factorResistencia'])[0]
#         RC=pd.to_numeric(Geo['resistenciaConcreto'])[0]
        
        
#         hj=pd.to_numeric(estratos['espesorEstrato'])
#         G1= pd.to_numeric(list(estratos['pesoEspecifico']),errors='coerce')
#         FI1=pd.to_numeric(list(estratos['friccionSuelo']))
#         C1=pd.to_numeric(list(estratos['cohesionSuelo']))

#         C=np.repeat([float(-1)],len(A), axis=0)
#         FI=np.repeat([float(-1)],len(A), axis=0)
#         G=np.repeat([float(-1)],len(A), axis=0)
        
        
#         h=np.repeat([float(0)],len(hj), axis=0)
#         h[0]=hj[0]
#         for i in range(1,len(hj)):
#             h[i]=h[i-1]+hj[i]

#         s=0
#         ZI=[abs(i) for i in A]
#         for i in range(len(ZI)):
#             if ZI[i]<=h[s]:
#                 C[i]=C1[s]
#                 FI[i]=FI1[s]
#                 G[i]=G1[s]
                    
#             else:
#                 s=s+1
#                 if s<len(hj):
#                     C[i]=C1[s]
#                     FI[i]=FI1[s]
#                     G[i]=G1[s]

            
#         for i in range(len(FI)):
#             if FI[i]==-1:
#                 C[i]=C1[len(hj)-1]
#                 FI[i]=FI1[len(hj)-1]
#                 G[i]=G1[len(hj)-1]

      
        
#         c0=0
        
#         N=0

        
        
#         dia=pd.to_numeric(Geo['diametroI'])[0]
#         diaf=pd.to_numeric(Geo['diametrof'])[0]

#         te=list(Geo['tipoElemento'])[0]

#         if te=='Barretes':
#             diam=1
#         else:
#             diam=dia
        
       
#         if Geo['transCarga'][0]=='Punta' and te!='Barretes':
#             diam=diaf      



            
#         Qmax=((diam**2)*pi/4)*0.2*(RC)



#         if NF==0:
#             BB=0.5
#         else:
#             BB=1
#         t1=(2*(N**2)*diam*BB+(2*(100+(N**2)))*diam*BB)*3.281*0.004482/FS
#         t2=(1440*(N-3)*(((diam*3.281+1)/(diam*6.562))**2)*BB  )*0.004882
#         t3=(pi*(diam**2)*t1/4)
#         t4=(pi*(diam**2)*t2/4)

#         B=pd.to_numeric(Geo['B'])[0]
#         R=pd.to_numeric(Geo['R'])[0]

#         if Geo['transCarga'][0]=='Friccion':
#             fr=1
#             p=0
#             if te=='Barretes':
#                 fr=(0.9*2*(B+R)/(diam*pi))*fr
#                 p=((B*R)/((diam**2)*pi/4))*p

#         elif Geo['transCarga'][0]=='Punta':
#             p=1
#             fr=0
#             if te=='Barretes':
#                 fr=(0.9*2*(B+R)/(diam*pi))*fr
#                 p=((B*R)/((diam**2)*pi/4))*p
#         else:
#             p=1
#             fr=1
#             if te=='Barretes':
#                 fr=(0.9*2*(B+R)/(diam*pi))*fr
#                 p=((B*R)/((diam**2)*pi/4))*p


#         svp=np.repeat([float(0)],len(A), axis=0)
#         sw=np.repeat([float(0)],len(A), axis=0)
#         svf=np.repeat([float(0)],len(A), axis=0)
#         kp=np.repeat([float(0)],len(A), axis=0)
#         kp1=1
#         sh=np.repeat([float(0)],len(A), axis=0)
#         Nq=np.repeat([float(0)],len(A), axis=0)
#         Nc=np.repeat([float(0)],len(A), axis=0)
#         friccion=np.repeat([float(0)],len(A), axis=0)
#         punta=np.repeat([float(0)],len(A), axis=0)
#         Peso=np.repeat([float(0)],len(A), axis=0)
#         Total=np.repeat([float(0)],len(A), axis=0)
       
        
#         for i in range(1,len(A)):
#             svp[i]=svp[i-1]+(A[i-1]-A[i])*G[i]
#             if -A[i]-NF<0:
#                 sw[i]=0
#             else:
#                 sw[i]=-A[i]-NF
#             svf[i]=svp[i]-sw[i]

#             if FI[i]==0:
#                 kp[i]=1
#             else:
#                 kp[i]=((1+math.sin(FI[i]*(pi/180)))/(1-math.sin(FI[i]*(pi/180))))*kp1

#             sh[i]=svf[i]*kp[i]+ 2*C[i]*c0*pow(kp[i],0.5)

#             Nq[i]=math.exp(pi*math.tan(FI[i]*(pi/180)))*pow(math.tan(pi/4+ (FI[i]*pi/360)),2)
#             if FI[i]==0:
#                 Nc[i]=9
#             else:
#                 Nc[i]=(Nq[i]-1)/(math.tan(FI[i]*pi/180))

#             friccion[i]=(alfa(C[i])*C[i]*pi*diam*((A[i-1]-A[i])/FS)+((sh[i]+sh[i-1])/2)*(A[i-1]-A[i])*math.tan(FI[i]*pi/180)*(pi*diam)/FS)*fr+friccion[i-1]

#             if N==0 and Nq[i]==1:
#                 punta[i]=((1.3*C[i]*Nc[i]/FS+svp[i]*Nq[i]/(1))*pi*(diam**2)/4)*p
#             elif N==0:
#                 punta[i]=((1.3*C[i]*Nc[i]/FS+svp[i]*Nq[i]/(FS))*pi*(diam**2)/4)*p
#             else:
#                 punta[i]=min([t3,t4])*p

#             Peso[i]=-pi*(diam**2)/4*A[i]*pd.to_numeric(Geo['peso'])[0]

#             si=friccion[i]+punta[i]-Peso[i]


#             if si<0:
#                 Total[i]=0
#             else:
#                 Total[i]=si

#         k=1

#         #Total[k]< Qmax:
#         while abs(min(A))<=sum(hj):
#             A.append(A[k]-0.1)


#             k=k+1
            
            
#             svp=np.repeat([float(0)],len(A), axis=0)
#             sw=np.repeat([float(0)],len(A), axis=0)
#             svf=np.repeat([float(0)],len(A), axis=0)
#             kp=np.repeat([float(0)],len(A), axis=0)
#             kp1=1
#             sh=np.repeat([float(0)],len(A), axis=0)
#             Nq=np.repeat([float(0)],len(A), axis=0)
#             Nc=np.repeat([float(0)],len(A), axis=0)
#             friccion=np.repeat([float(0)],len(A), axis=0)
#             punta=np.repeat([float(0)],len(A), axis=0)
#             Peso=np.repeat([float(0)],len(A), axis=0)
#             Total=np.repeat([float(0)],len(A), axis=0)

            
#             C=np.repeat([float(-1)],len(A), axis=0)
#             FI=np.repeat([float(-1)],len(A), axis=0)
#             G=np.repeat([float(-1)],len(A), axis=0)

            
            
#             h=np.repeat([float(0)],len(hj), axis=0)
#             h[0]=hj[0]
#             for i in range(1,len(hj)):
#                 h[i]=h[i-1]+hj[i]


#             s=0
#             ZI=[abs(i) for i in A]
#             for i in range(len(ZI)):
#                 if s<len(h) and ZI[i]<=h[s]:
#                     C[i]=C1[s]
#                     FI[i]=FI1[s]
#                     G[i]=G1[s]
                    
#                 else:
#                     s=s+1
#                     if s<len(hj):
#                         C[i]=C1[s]
#                         FI[i]=FI1[s]
#                         G[i]=G1[s]

            
#             for i in range(len(FI)):
#                 if FI[i]==-1:
#                     C[i]=C1[len(hj)-1]
#                     FI[i]=FI1[len(hj)-1]
#                     G[i]=G1[len(hj)-1]

                
                
#             for i in range(1,len(A)):
#                 svp[i]=svp[i-1]+(A[i-1]-A[i])*G[i]
#                 if -A[i]-NF<0:
#                     sw[i]=0
#                 else:
#                     sw[i]=-A[i]-NF
#                 svf[i]=svp[i]-sw[i]

#                 if FI[i]==0:
#                     kp[i]=1
#                 else:
#                     kp[i]=((1+math.sin(FI[i]*(pi/180)))/(1-math.sin(FI[i]*(pi/180))))*kp1

#                 sh[i]=svf[i]*kp[i]+ 2*C[i]*c0*pow(kp[i],0.5)

#                 Nq[i]=math.exp(pi*math.tan(FI[i]*(pi/180)))*pow(math.tan(pi/4+ (FI[i]*pi/360)),2)
#                 if FI[i]==0:
#                     Nc[i]=9
#                 else:
#                     Nc[i]=(Nq[i]-1)/(math.tan(FI[i]*pi/180))

#                 friccion[i]=(alfa(C[i])*C[i]*pi*diam*((A[i-1]-A[i])/FS)+((sh[i]+sh[i-1])/2)*(A[i-1]-A[i])*math.tan(FI[i]*pi/180)*(pi*diam)/FS)*fr+friccion[i-1]

#                 if N==0 and Nq[i]==1:
#                     punta[i]=((1.3*C[i]*Nc[i]/FS+svp[i]*Nq[i]/(1))*pi*(diam**2)/4)*p
#                 elif N==0:
#                     punta[i]=((1.3*C[i]*Nc[i]/FS+svp[i]*Nq[i]/(FS))*pi*(diam**2)/4)*p
#                 else:
#                     punta[i]=min([t3,t4])*p

#                 Peso[i]=-pi*(diam**2)/4*A[i]*pd.to_numeric(Geo['peso'])[0]

#                 si=friccion[i]+punta[i]-Peso[i]


#                 if si<0:
#                     Total[i]=0
#                 else:
#                     Total[i]=si
        
#         data=pd.DataFrame({'Fi':FI, 'C':C,'G':G,'Longitud':A,'svp':svp, 'Kp':kp, 'sh':sh, 'friccion':friccion,'punta':punta,'Peso':Peso,'Total':Total})
#         data=data.drop([0],axis=0)
        
       
#         if P==True:
#             return A
        
#         if Diam==True:
#             return diam

#         if r==True:
#             return data
#         return JsonResponse(data.to_dict('records'), safe=False)
#     else:
#         if r==True:
#             return  pd.DataFrame({ 'Longitud':[0],'Total':[0]})
#         return JsonResponse({})




# pd.set_option('display.max_rows',600)




# #print(Capp(r=True))




# def AsentProf(r=False):
#     Geo=pd.DataFrame(geometriaCimentacionProfunda.objects.all().values())
#     estratos=pd.DataFrame(perfilGeotecnico.objects.all().values())
#     datosI=pd.DataFrame(datosIniciales.objects.all().values())
#     datos=pd.DataFrame(datosConsProfunda.objects.all().values())


#     if len(datos.index)>0 and len(Geo.index)>0 and len(estratos.index)>0 and len(datosI.index)>0:
#         ES=pd.to_numeric(list(Geo['ModuloMaterial']),errors='coerce')[0]
#         Bdado=pd.to_numeric(datos['Bdado'])[0]
#         Ldado=pd.to_numeric(datos['Ldado'])[0]        
#         AseMax=pd.to_numeric(datos['Amax'])[0]
#         CargaMax=pd.to_numeric(datos['CargaMax'])[0]

#         estratos=estratos.sort_values('idEstrato')
#         prof=pd.to_numeric(Geo['prof'])[0]
#         h1=pd.to_numeric(datos['H'])[0]/100
#         L=[prof+(h1/2)]

#         hj=pd.to_numeric(estratos['espesorEstrato'])        
              
#         U1=pd.to_numeric(list(estratos['relacionPoisson']))
#         CC1=pd.to_numeric(list(estratos['indiceDeComprension']))
#         e01=pd.to_numeric(list(estratos['relacionDeVacioInicial']))
                

#         h=np.repeat([float(0)],len(hj), axis=0)
#         h[0]=hj[0]
#         for i in range(1,len(hj)):
#             h[i]=h[i-1]+hj[i]
#         U=np.repeat([float(-1)],len(L), axis=0)
#         CC=np.repeat([float(-1)],len(L), axis=0)
#         e0=np.repeat([float(-1)],len(L), axis=0)

#         s=0        
#         for i in range(len(L)):
#             if s<len(h) and L[i]<=h[s]:
#                 U[i]=U1[s]
#                 CC[i]=CC1[s]
#                 e0[i]=e01[s]
                    
#             else:
#                 s=s+1
#                 if s<len(hj):
#                     U[i]=U1[s]
#                     CC[i]=CC1[s]
#                     e0[i]=e01[s]
            
#         for i in range(len(U)):
#             if U[i]==-1:
#                 U[i]=U1[len(hj)-1]
#                 CC[i]=CC1[len(hj)-1]
#                 e0[i]=e01[len(hj)-1]

#         dia=pd.to_numeric(Geo['diametroI'])[0]
#         diaf=pd.to_numeric(Geo['diametrof'])[0]

       
        
#         carga=pd.to_numeric(Geo['Carga'])[0]

#         Ep=pd.to_numeric(Geo['Ep'])[0]
#         Eb=pd.to_numeric(Geo['Eb'])[0]

#         H=np.repeat([float(0)],len(L), axis=0)
#         Rld=np.repeat([float(0)],len(L), axis=0)
#         Rhl=np.repeat([float(0)],len(L), axis=0)
#         k=np.repeat([float(0)],len(L), axis=0)
#         io=np.repeat([float(0)],len(L), axis=0)
#         rk=np.repeat([float(0)],len(L), axis=0)
#         rh=np.repeat([float(0)],len(L), axis=0)
#         rv=np.repeat([float(0)],len(L), axis=0)
#         Rb=np.repeat([float(0)],len(L), axis=0)
#         asent=np.repeat([float(0)],len(L), axis=0)
#         AsenT=np.repeat([float(0)],len(L), axis=0)
       


#         for i in range(len(L)):
#             H[i]=4*L[i]

#             Rld[i]=L[i]/dia
#             Rhl[i]=H[i]/L[i]
#             k[i]=Ep/ES

#             io[i]=Io(L_d=Rld[i],db_d=1)
#             rk[i]=Rk(K=k[i],L_d=Rld[i])

#             rh[i]=Rh(H_L=Rhl[i], L_d=Rld[i])
#             rv[i]=Rv(vs=U[i], K=k[i])

#             if Rld[i]<=5:
#                 Rb[i]=Rb5(Eb/ES,k[i])
#             elif Rld[i]>5 and Rld[i]<10:
#                 y0=Rb5(Eb/ES,k[i])
#                 x0=5
#                 y1=Rb10(Eb/ES,k[i])
#                 x1=10
#                 Rb[i]=y0+((y1-y0)/(x1-x0))*(Rld[i]-x0)
#             elif Rld[i]==10:
#                 Rb[i]=Rb10(Eb/ES,k[i])
#             elif Rld[i]>10 and Rld[i]<25:
#                 y0=Rb10(Eb/ES,k[i])
#                 x0=10
#                 y1=Rb25(Eb/ES,k[i])
#                 x1=25
#                 Rb[i]=y0+((y1-y0)/(x1-x0))*(Rld[i]-x0)
#             elif Rld[i]==25:
#                 Rb[i]=Rb25(Eb/ES,k[i])
            
#             elif Rld[i]>25 and Rld[i]<50:
#                 y0=Rb25(Eb/ES,k[i])
#                 x0=25
#                 y1=Rb50(Eb/ES,k[i])
#                 x1=50
#                 Rb[i]=y0+((y1-y0)/(x1-x0))*(Rld[i]-x0)
#             elif Rld[i]==50:
#                 Rb[i]=Rb50(Eb/ES,k[i])
            
#             elif Rld[i]>50 and Rld[i]<75:
#                 y0=Rb50(Eb/ES,k[i])
#                 x0=50
#                 y1=Rb75(Eb/ES,k[i])
#                 x1=75
#                 Rb[i]=y0+((y1-y0)/(x1-x0))*(Rld[i]-x0)
            
#             elif Rld[i]>=75:
#                 Rb[i]=Rb75(Eb/ES,k[i])
            
#             else:
#                 return JsonResponse({})   

            
#             if Geo['transCarga'][0]=='Punta':
#                 I=(io[i]*rk[i]*rv[i]*Rb[i])
#                 asent[i]=(carga*I/ES)/diaf
#             elif Geo['transCarga'][0]=='Friccion':
#                 I=(io[i]*rk[i]*rh[i]*rv[i])
#                 asent[i]=(carga*I/ES)/dia
#             elif Geo['transCarga'][0]=='Minimo':
#                 I1=(io[i]*rk[i]*rv[i]*Rb[i])
#                 I2=(io[i]*rk[i]*rh[i]*rv[i])
#                 asent[i]=min([((carga*I1/ES)/diaf),((carga*I2/ES)/dia)])
            
#             elif Geo['transCarga'][0]=='Maximo':
#                 I1=(io[i]*rk[i]*rv[i]*Rb[i])
#                 I2=(io[i]*rk[i]*rh[i]*rv[i])
#                 asent[i]=max([((carga*I1/ES)/diaf),((carga*I2/ES)/dia)])
            
#             else:
                
#                 I1=(io[i]*rk[i]*rv[i]*Rb[i])
#                 I2=(io[i]*rk[i]*rh[i]*rv[i])
#                 asent[i]=mean([((carga*I1/ES)/diaf),((carga*I2/ES)/dia)])
            
#             AsenT[i]=asent[i]

        
            

            



        
#         while AsenT[len(AsenT)-1]>AseMax:
#             L.append(L[len(L)-1]+(h1/2))

#             U=np.repeat([float(-1)],len(L), axis=0)
#             CC=np.repeat([float(-1)],len(L), axis=0)
#             e0=np.repeat([float(-1)],len(L), axis=0)

#             s=0        
#             for i in range(len(L)):
#                 if s<len(h) and L[i]<=h[s]:
#                     U[i]=U1[s]
#                     CC[i]=CC1[s]
#                     e0[i]=e01[s]
                        
#                 else:
#                     s=s+1
#                     if s<len(hj):
#                         U[i]=U1[s]
#                         CC[i]=CC1[s]
#                         e0[i]=e01[s]
                
#             for i in range(len(U)):
#                 if U[i]==-1:
#                     U[i]=U1[len(hj)-1]
#                     CC[i]=CC1[len(hj)-1]
#                     e0[i]=e01[len(hj)-1]
                




#             H=np.repeat([float(0)],len(L), axis=0)
#             Rld=np.repeat([float(0)],len(L), axis=0)
#             Rhl=np.repeat([float(0)],len(L), axis=0)
#             k=np.repeat([float(0)],len(L), axis=0)
#             io=np.repeat([float(0)],len(L), axis=0)
#             rk=np.repeat([float(0)],len(L), axis=0)
#             rh=np.repeat([float(0)],len(L), axis=0)
#             rv=np.repeat([float(0)],len(L), axis=0)
#             Rb=np.repeat([float(0)],len(L), axis=0)
#             asent=np.repeat([float(0)],len(L), axis=0)
            
#             AsenT=np.repeat([float(0)],len(L), axis=0)
#             AsentC=np.repeat([float(0)],len(L), axis=0)


#             for i in range(len(L)):
#                 H[i]=4*L[i]

#                 Rld[i]=L[i]/dia
#                 Rhl[i]=H[i]/L[i]
#                 k[i]=Ep/ES

#                 io[i]=Io(L_d=Rld[i],db_d=1)
#                 rk[i]=Rk(K=k[i],L_d=Rld[i])

#                 rh[i]=Rh(H_L=Rhl[i], L_d=Rld[i])
#                 rv[i]=Rv(vs=U[i], K=k[i])

#                 if Rld[i]<=5:
#                     Rb[i]=Rb5(Eb/ES,k[i])
#                 elif Rld[i]>5 and Rld[i]<10:
#                     y0=Rb5(Eb/ES,k[i])
#                     x0=5
#                     y1=Rb10(Eb/ES,k[i])
#                     x1=10
#                     Rb[i]=y0+((y1-y0)/(x1-x0))*(Rld[i]-x0)
#                 elif Rld[i]==10:
#                     Rb[i]=Rb10(Eb/ES,k[i])
#                 elif Rld[i]>10 and Rld[i]<25:
#                     y0=Rb10(Eb/ES,k[i])
#                     x0=10
#                     y1=Rb25(Eb/ES,k[i])
#                     x1=25
#                     Rb[i]=y0+((y1-y0)/(x1-x0))*(Rld[i]-x0)
#                 elif Rld[i]==25:
#                     Rb[i]=Rb25(Eb/ES,k[i])
                
#                 elif Rld[i]>25 and Rld[i]<50:
#                     y0=Rb25(Eb/ES,k[i])
#                     x0=25
#                     y1=Rb50(Eb/ES,k[i])
#                     x1=50
#                     Rb[i]=y0+((y1-y0)/(x1-x0))*(Rld[i]-x0)
#                 elif Rld[i]==50:
#                     Rb[i]=Rb50(Eb/ES,k[i])
                
#                 elif Rld[i]>50 and Rld[i]<75:
#                     y0=Rb50(Eb/ES,k[i])
#                     x0=50
#                     y1=Rb75(Eb/ES,k[i])
#                     x1=75
#                     Rb[i]=y0+((y1-y0)/(x1-x0))*(Rld[i]-x0)
                
#                 elif Rld[i]>=75:
#                     Rb[i]=Rb75(Eb/ES,k[i])
                
#                 else:
#                     return JsonResponse({})   

                
#                 if Geo['transCarga'][0]=='Punta':
#                     I=(io[i]*rk[i]*rv[i]*Rb[i])
                    
#                     asent[i]=(carga*I/ES)/diaf
#                 elif Geo['transCarga'][0]=='Friccion':
#                     I=(io[i]*rk[i]*rh[i]*rv[i])
#                     asent[i]=(carga*I/ES)/dia
                   
#                 elif Geo['transCarga'][0]=='Minimo':
#                     I1=(io[i]*rk[i]*rv[i]*Rb[i])
#                     I2=(io[i]*rk[i]*rh[i]*rv[i])
                    
#                     asent[i]=min([((carga*I1/ES)/diaf),((carga*I2/ES)/dia)])
                
#                 elif Geo['transCarga'][0]=='Maximo':
#                     I1=(io[i]*rk[i]*rv[i]*Rb[i])
#                     I2=(io[i]*rk[i]*rh[i]*rv[i])
#                     asent[i]=max([((carga*I1/ES)/diaf),((carga*I2/ES)/dia)])
                    
                
#                 else:
                    
#                     I1=(io[i]*rk[i]*rv[i]*Rb[i])
#                     I2=(io[i]*rk[i]*rh[i]*rv[i])
#                     asent[i]=mean([((carga*I1/ES)/diaf),((carga*I2/ES)/dia)])
                
#                 AsenT[i]=asent[i]
                    

#             LL=17#L[len(L)-1]
#             pf=4

#             zz=(LL/3)+(h1/2)
#             z=np.arange(zz,80,h1)
#             ni=np.repeat([float(0)],len(z), axis=0)
#             ni[0]=-pf-0.5
#             for i in range(len(ni)):
#                 if i>0:
#                     ni[i]=ni[i-1]-1
           
#             NF=3            
#             GAMA=[1.8 for i in z]
                           
#             freatico=[NF+i for i in ni]

#             Po1=6*1.5+(LL+(h1/2)-6)*1.4-(LL+(h1/2)-14)
#             Po=np.repeat([float(0)],len(z), axis=0)
#             Po[0]=Po1

#             for i in range(len(z)):
#                 if i>0:
#                     Po[i]=Po[i-1]+0.5*(GAMA[i-1]+GAMA[i])+freatico[i]-freatico[i-1]

                    
#             AsenC=np.repeat([float(0)],len(z), axis=0)
               
#             for j in range(len(z)):
#                 div=0.3/(1+1)         
#                 fact=(1/(z[j]+Bdado))/(z[j]+Ldado)   
#                 DP=fact*CargaMax
#                 AsenC[j]=float(div*(100*h1)*log10((DP+Po[j])/Po[j]))
                   
#             AsentC=sum(AsenC)
        
        
#         print(Po)
#         print(AsentC)
        

       
#         data=pd.DataFrame({'Longitud':L,'k':k,'Rb':Rb,'io':io,'rk':rk,'rv':rv,'Rld':Rld ,'Rhl':Rhl,'AsI': asent,'AseC':AsentC,'AsentamientoTotal':AsenT})
        
#         return  
#     else:
#         return JsonResponse({})






# #print(AsentProf(r=False))






# def Eficiencia(r=False):
#     EF=pd.DataFrame(eficiencia.objects.all().values())
#     cp=Capp(r=True)
#     datos=pd.DataFrame(datosConsProfunda.objects.all().values())
    
#     if len(cp['Total'])>0  and len(EF.index)>0:
        
#         Bdado=pd.to_numeric(datos['Bdado'])[0]
#         Ldado=pd.to_numeric(datos['Ldado'])[0]
#         D= Capp(Diam=True)
#         sepx=pd.to_numeric(EF['sepx'])[0]*D
#         sepy=pd.to_numeric(EF['sepy'])[0]*D

#         offsetMinX=pd.to_numeric(EF['offsetX'])[0]
#         offsetMinY=pd.to_numeric(EF['offsetY'])[0]

#         v=(Ldado-(2*offsetMinY))/sepy
#         offsetdisY=(v-int(v))/2+ offsetMinY
#         n2=int(v)+1


#         h=(Bdado-(2*offsetMinX))/sepx
#         offsetdisX=(h-int(h))/2+ offsetMinX
#         n1=int(h)+1

#         p=pi*D
#         d=(sepx+sepy)/2

#         capp=Capp(r=True)
#         capp=max(capp['Total'])
#         Q0=atan(D/d)*(360/(2*pi))
#         autor=EF['autor'][0]

#         efi1= 1-((((n1-1)*n2+(n2-1)*n1)/(90*n1*n2))*Q0)

#         efi2=round(1-D/(pi*d*n1*n2)*(n1*(n2-1)+n2*(n1-1)+sqrt(2)*(n1-1)*(n2-1)),2)
#         efi3=round((1-(11*(d*3.28083)/(7*(((d*3.28083)**2) -1)))*((n1+n2-2)/(n1+n2-1)))+0.3/(n1+n2),2)

#         if autor=='CL':
#             efi=efi1
#         elif autor=='GA':
#             efi=efi2

#         elif autor=='SK':
#             efi=efi3
#         elif autor=='Min':
#             efi=round(min([efi1,efi2,efi3]),2)
#         elif autor=='Max':
#             efi=round(max([efi1,efi2,efi3]),2)
        
#         elif autor=='Med':
#             efi=round(statistics.median([efi1,efi2,efi3]),2)
#         else:
#             efi= round(mean([efi1,efi2,efi3]),2)
        
#         efi=float(efi)

#         capcarga= round(n1*n2*efi*capp,2)
#         long=abs(min(cp['Longitud']))
#         longpilotes= round(long*(n1*n2),2)

#         data=pd.DataFrame({'NPVerticales':[n2],'NPHorizontales':[n1],'Eficiencia': [efi],'Capacidaddecarga':[capcarga],'Cantidadpilotes':[n1*n2],'Longitudpilotes':[longpilotes],'ofsetMinX':[offsetMinX],'offsetMinY':[offsetMinY],'ofsetDisX':[round(offsetdisX,1)],'offsetDisY':[round(offsetdisY,1)]})
#         if r==True:
#             return data
#         return #JsonResponse(data.to_dict('records'), safe=False)
#     else:
#         return JsonResponse({})



# #print(Eficiencia(r=True))





    
# # Abacoco simentacion superficial

# def CappAbaco(B,Rbl):

#     estratos = pd.DataFrame(perfilGeotecnico.objects.all().values())
#     datosI=pd.DataFrame(datosIniciales.objects.all().values())

#     if  len(datosI.index)>0 and len(estratos.index)>0:


        
#         hj=pd.to_numeric(estratos['espesorEstrato'])
        

#         prof=pd.to_numeric(datosI['profundidadCimentacion'])[0]
#         NF=pd.to_numeric(datosI['nivelFeatico'])[0]
#         modelo=datosI['modelo'][0]
#         FS=pd.to_numeric(datosI['factorResistencia'])[0]
#         theta=0#pd.to_numeric(datosI['theta'])[0]
        


#         j=0
#         q=np.repeat(float(0), [len(hj)], axis=0)
#         hji=[]
#         while j<len(hj):
            
            
#             hji.append(hj[j])
#             S=sum(hji)            

#             if prof<=S:
#                 fi=pd.to_numeric(list(estratos['friccionSuelo']))[j]
#                 C=pd.to_numeric(list(estratos['cohesionSuelo']))[j]
#                 Gama=pd.to_numeric(estratos['pesoEspecifico'])[j]
                
#                 if NF<prof:
#                     q[j]=NF*Gama+(prof-NF)*1.13*(Gama-0.981)
#                 else:
#                     q[j]=Gama*prof
#             j=j+1 
        
#         q1=q
#         q=max(q)
#         Gama=(q/prof)
        
#         ref= "fi" in locals()
#         if ref==False:
#             fi=pd.to_numeric(list(estratos['friccionSuelo']))[len(hj)-1]
#             C=pd.to_numeric(list(estratos['cohesionSuelo']))[len(hj)-1] 
#             Gama=pd.to_numeric(estratos['pesoEspecifico'])[len(hj)-1]
#             if NF<prof:
#                 q=NF*Gama+(prof-NF)*1.13*(Gama-0.981)
#             else:
#                 q=Gama*prof

        
#         Nq=math.exp(math.pi*math.tan(fi*(math.pi/180)))*pow(math.tan(math.pi/4+(fi/2)*(math.pi/180)),2)
#         Nc=(Nq-1)/math.tan(fi*(math.pi/180))
#         if modelo=='hansen':
#             Nr=1.5*(Nq-1)*math.tan(fi*(math.pi/180))
#         elif modelo=='Vesic':
#             Nr=2*(Nq+1)*math.tan(fi*(math.pi/180))
        
        
#         qu=[]
#         qa=[]
        
#         for i in range(len(B)):
#             if NF<prof:
#                 Gp =1.13*Gama-1
            
#             elif NF-prof < B[i]:
#                 Gp=1.33*Gama-1 +(NF-prof)/(B[i]*(Gama-(1.33*Gama-1)))
                
#             else:
#                 Gp=Gama
            

#             if prof/B[i]<=1:
#                 ter=prof/B[i]
#             else:
#                 ter=atan(prof/B[i])
            
#             if (1-0.4*Rbl)<=0.6:
#                 ter2=0.6
#             else:
#                 ter2=(1-0.4*Rbl)

#             Nccorr=Nc*(1+Nq/Nc*Rbl)*(1+ 0.4*ter)*(1-theta/147)   
#             Nqcorr=Nq*(1+Rbl*math.sin(fi*(pi/180))  ) *(1+2*math.tan(fi*(pi/180))*(1-math.sin(fi*(pi/180) ) )**2*ter)*((1-0.5*math.tan(theta*(pi/180)))**5)
#             Nrcorr=Nr*ter2*((1-0.5*math.tan(theta*(pi/180))  )**5)

#             qu.append(C*Nccorr+q*Nqcorr+Gp*B[i]*Nrcorr/2)
#             qa.append(qu[i]/FS)




#         return  qa
       
#     else:        
#         return [0]



# #print(CappAbaco([1,2],0.5))



# def AsenAbaco(Bmin,Bmax,Rbl,F3,each=0.01,x=False,y=False):
#     B=np.arange(Bmin,Bmax+1,each)

#     estratos=pd.DataFrame(perfilGeotecnico.objects.all().values())
#     datosI=pd.DataFrame(datosIniciales.objects.all().values())

#     if len(datosI.index)>0 and len(estratos.index)>0:

#         prof=pd.to_numeric(datosI['profundidadCimentacion'])[0]
#         NF=pd.to_numeric(datosI['nivelFeatico'])[0]
#         estratos=estratos.sort_values('idEstrato')
#         L=[]
#         for i in range(len(B)):
#             L.append(B[i]/Rbl)


#         Lx=[L[i]/2 for i in range(len(L))]
#         Bx=[B[i]/2 for i in range(len(B))]
#         product = [x*y for x,y in zip(B,L)]
#         q=[F3/product[x] for x in range(len(product))]

#         u=pd.to_numeric(list(estratos['relacionPoisson']))
#         Es=pd.to_numeric(list(estratos['moduloElasticidad']))
#         Cc=pd.to_numeric(list(estratos['indiceDeComprension']))
#         Cr=pd.to_numeric(list(estratos['indiceDeExpansibilidad']))
#         Sp=pd.to_numeric(list(estratos['presionDepreconsolidacion']))
#         e0=pd.to_numeric(list(estratos['relacionDeVacioInicial']))
#         hj=pd.to_numeric(list(estratos['espesorEstrato']))
#         Gama=pd.to_numeric(list(estratos['pesoEspecifico']))

#         ZI=np.arange(pd.to_numeric(datosI['h'])[0],sum(hj),pd.to_numeric(datosI['h'])[0])
#         hi=np.repeat([float(0)],len(ZI), axis=0)
#         hi[0]=ZI[0]
#         for i in range(1,len(ZI)):
#             hi[i]=pd.to_numeric(datosI['h'])[0]

#         Zcarg=[ZI[i]-prof for i in range(len(ZI))]
#         for i in range(len(Zcarg)):
#             if Zcarg[i]<0:
#                 Zcarg[i]=0


#         Crr=np.repeat([float(0)],len(ZI), axis=0)
#         Ccc=np.repeat([float(0)],len(ZI), axis=0)
#         SP=np.repeat([float(0)],len(ZI), axis=0)
#         E0=np.repeat([float(0)],len(ZI), axis=0)
#         Hj=np.repeat([float(0)],len(ZI), axis=0)
#         GAMA=np.repeat([float(0)],len(ZI), axis=0)
#         ES=np.repeat([float(0)],len(ZI), axis=0)
#         uu=np.repeat([float(0)],len(ZI), axis=0)

#         h=np.repeat([float(0)],len(hj), axis=0)
#         h[0]=hj[0]
#         for i in range(1,len(hj)):
#             h[i]=h[i-1]+hj[i]


#         s=0
#         for i in range(len(ZI)):

#             if ZI[i]<=h[s]:
#                 Crr[i]=Cr[s]
#                 Ccc[i]=Cc[s]
#                 E0[i]=e0[s]
#                 GAMA[i]=Gama[s]
#                 SP[i]=Sp[s]
#                 Hj[i]=hj[s]
#                 ES[i]=Es[s]
#                 uu[i]=u[s]
#             else:
#                 s=s+1
#                 Crr[i]=Cr[s]
#                 Ccc[i]=Cc[s]
#                 E0[i]=e0[s]
#                 GAMA[i]=Gama[s]
#                 SP[i]=Sp[s]
#                 Hj[i]=hj[s]
#                 ES[i]=Es[s]
#                 uu[i]=u[s]


#         for i in range(len(ZI)):
#             if ZI[i]<=prof:
#                 Ccc[i]=0
#                 Crr[i]=0

#         iSz=[hi[i]*GAMA[i] for i in range(len(hi))]
#         Sz=np.repeat([float(0)],len(iSz), axis=0)
#         Sz[0]=iSz[0]
#         for i in range(1,len(Sz)):
#             Sz[i]=Sz[i-1]+iSz[i]

#         gw=9.81
#         hw=[ZI[i]-NF for i in range(len(ZI))]
#         for i in range(len(hw)):
#             if hw[i]<0:
#                 hw[i]=0
#         U=[gw*x for x in hw]


#         #esfuerzos efectivos

#         Szp=[Sz[i]-U[i] for i in range(len(U))]
#         R1=np.repeat([float(0)],len(Zcarg), axis=0)
#         R2=np.repeat([float(0)],len(Zcarg), axis=0)
#         R3=np.repeat([float(0)],len(Zcarg), axis=0)
#         dsz=np.repeat([float(0)],len(Zcarg), axis=0)
#         dsx=np.repeat([float(0)],len(Zcarg), axis=0)
#         dsy=np.repeat([float(0)],len(Zcarg), axis=0)
#         DU=np.repeat([float(0)],len(Zcarg), axis=0)
#         dszp=np.repeat([float(0)],len(Zcarg), axis=0)
#         dsxp=np.repeat([float(0)],len(Zcarg), axis=0)
#         dsyp=np.repeat([float(0)],len(Zcarg), axis=0)
#         Dz=np.repeat([float(0)],len(Zcarg), axis=0)

#         ASI=np.repeat([float(0)],len(B), axis=0)
#         ASC=np.repeat([float(0)],len(B), axis=0)
#         AST=np.repeat([float(0)],len(B), axis=0)
#         for j in range(len(B)):
#             for k in range(len(Zcarg)):
#                 R1[k]=math.sqrt(Lx[j]**2+Zcarg[k]**2)
#                 R2[k]=math.sqrt(Bx[j]**2+Zcarg[k]**2)
#                 R3[k]=math.sqrt(Lx[j]**2+Bx[j]**2+Zcarg[k]**2)
#                 if Zcarg[k]==0:
#                     dsz[k]=0
#                     dsx[k]=0
#                     dsy[k]=0
#                 else:

#                     dsz[k]=4*(q[j]/(2*math.pi))*(math.atan(((Lx[j])*(Bx[j]))/(Zcarg[k]*R3[k]))+(((Lx[j])*(Bx[j])*Zcarg[k])/R3[k])*((1/(R1[k]**2))+(1/(R2[k]**2))))
#                     dsx[k]=4*(q[j]/(2*math.pi))*(math.atan((((Lx[j]*Bx[j])/(Zcarg[k]*R3[k]))))- (Lx[j]*Bx[j]*Zcarg[k])/((R1[k]**2)*R3[k]))
#                     dsy[k]=4*(q[j]/(2*math.pi))*(math.atan((((Lx[j]*Bx[j])/(Zcarg[k]*R3[k]))))- (Lx[j]*Bx[j]*Zcarg[k])/((R2[k]**2)*R3[k]))



#                 DU[k]=(dsz[k]+dsy[k]+dsx[k])/3
#                 Dz[k]=((dsz[k]/ES[k])-(uu[k]/ES[k])*(dsx[k]+dsy[k]))*hi[k]

#                 dszp[k]=dsz[k]-DU[k]
#                 dsxp[k]=dsx[k]-DU[k]
#                 dsyp[k]=dsy[k]-DU[k]



#             Szfp=[Szp[i]+dszp[i] for i in range(len(dszp))]



#             Sc=np.repeat([float(0)],len(Szfp), axis=0)
#             for k in range(len(Szfp)):
#                 if datosI['OCR'][0]=="Si":
#                    C1=hi[k]/(1+E0[k])
#                    term1=Ccc[k]*C1
#                    log=math.log10(Szfp[k]/Szp[k])
#                    Sc[k]=term1*log
#                 else:
#                     if SP[k]>Szfp[k] and Szfp[k]/Szp[k]>0:
#                        C1=hi[k]/(1+E0[k])
#                        term1=Crr[k]*C1
#                        log=math.log10(Szfp[k]/Szp[k])
#                        Sc[k]=term1*log
#                     elif SP[k]>Szp[k] and SP[k]<Szfp[k]:
#                        C1=hi[k]/(1+E0[k])
#                        Sc[k]=C1*(Crr[k]*math.log10(SP[k]/Szp[k]) + Ccc[k]*math.log10(Szfp[k]/SP[k]))
#                     elif Szfp[k]/Szp[k]>0:
#                         C1=hi[k]/(1+E0[k])
#                         term1=Ccc[k]*C1
#                         log=math.log10(Szfp[k]/Szp[k])
#                         Sc[k]=term1*log
#                     else:
#                         Sc[k]=0


#             ASI[j]=sum(Dz)
#             ASC[j]=sum(Sc)
#             AST[j]=sum(Dz)+sum(Sc)

        
#         data=pd.DataFrame({'B':B,'Asentamiento':AST})
#         if x==True:
#             return AST
#         if y==True:
#             return B

#     else:
       
#         return [-1]
    


# # R=pd.DataFrame(rangoDimensiones.objects.all().values())

# # RC=pd.DataFrame(relacionCarga.objects.all().values())
# # RC=RC.sort_values('rbl')

# # rbl=pd.to_numeric(list(RC['rbl']))
# # F3=pd.to_numeric(list(RC['carga']))


# # bmin=pd.to_numeric(list(R['Bmin']))[0]
# # bmax=pd.to_numeric(list(R['Bmax']))[0]
# # cada=pd.to_numeric(list(R['each']))[0]


# # X=[]
# # Y=[]

# # for i in range(len(rbl)):
# #     x=AsenAbaco(Bmin=bmin,Bmax=bmax,Rbl=rbl[i],F3=F3[i],each=cada,x=True)
# #     y=AsenAbaco(Bmin=bmin,Bmax=bmax,Rbl=rbl[i],F3=F3[i],each=cada,y=True)
# #     rb=list(np.repeat([float(rbl[i])],len(x), axis=0))
    
    
# #     X.append(x)
# #     Y.append(y)

# # Rb=np.repeat(rbl, len(x))
# # Y=np.repeat(y, len(rbl))



# # data=pd.DataFrame({'B':y,'Asentamiento':x,'RBL':rbl})

# # myplot=p.ggplot(data=data,
# #         mapping=p.aes(x='Asentamiento', y='B', color='RBL'))   + p.geom_line() +p.ylab("Dimension")  + p.xlab("Asentamiento Total") + p.scale_x_log10() + p.theme_bw()+ p.theme(text=p.element_text(size=16))

# # myplot.save("myplot.png", dpi=600)
