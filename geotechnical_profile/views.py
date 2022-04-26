from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, response
# Create your views here.
from .models import perfilGeotecnico,parametroSuelo,correlaciones,Observaciones
from rest_framework import viewsets
from .serializers import perfilSerializer,correlaciones_Serializer,Observaciones_Serializer,parametroSuelo_Serializer
import pandas as pd
import numpy as np
import json
from math import sqrt
from rdp import rdp
from numpy.core.fromnumeric import alltrue, mean
from rdp import rdp
import plotnine as p
from plotnine import *
import matplotlib.pyplot as plt
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from perforation_register.models import Sondeo, registroDePerforacion
from laboratories.models import laboratory
from pandas_datareader import data as wb



# Create your views here.

class correlacionesViewSet(viewsets.ModelViewSet):
    serializer_class = correlaciones_Serializer
    queryset = correlaciones.objects.all()
    def perform_create(self, serializer):
        serializer.save() 
    def get_queryset(self):
        return self.queryset.filter()
    


class perfilViewSet(viewsets.ModelViewSet):
    serializer_class = perfilSerializer
    queryset = perfilGeotecnico.objects.all()
    def perform_create(self, serializer):
        serializer.save() 
    def get_queryset(self):
        return self.queryset.filter()
    

class parametrosViewSet(viewsets.ModelViewSet):
    serializer_class = parametroSuelo_Serializer
    queryset = parametroSuelo.objects.all()
    def perform_create(self, serializer):
        serializer.save() 
    def get_queryset(self):
        return self.queryset.filter()
    
class observacionesViewSet(viewsets.ModelViewSet):
    serializer_class = Observaciones_Serializer
    queryset = Observaciones.objects.all()
    def perform_create(self, serializer):
        serializer.save() 
    def get_queryset(self):
        return self.queryset.filter()
    


# ############################################################################################

# def Perfil(Plot=False,sig=False):
#     data1 = pd.DataFrame(registroDePerforacion.objects.all().values())
#     data2 = pd.DataFrame(laboratory.objects.all().values())

#     if len(data2.index)>0 and len(data1.index)>0:
#         data1 =data1 .sort_values('id')
#         data2 =data2 .sort_values('id')
#         data=pd.concat([data1, data2], axis=1)
#         data.rename(columns={'usc':'USC'},inplace=True)
    
#     elif len(data2.index)>0:
#         data2 =data2 .sort_values('id')
#         data=data2
    
#     elif len(data1.index)>0:
#         data1 =data1 .sort_values('id')
#         data=data1        
#         data['USC']=data['clasificacionesPrimarias']

#     else:
#         return JsonResponse({})
    

#     data3=pd.DataFrame()
#     if len(data1.index)>0:        
#         data1.rename(columns={'profundidadInicial':'PROF1','profundidadFinal':'PROF2','spt6': 'SPT1','spt12': 'SPT2', 'spt18': 'SPT3','clasificacionesPrimarias':'class1'},inplace=True)
#         data3["SPT1"] = pd.to_numeric(data1["SPT1"],errors='coerce')        
#         data3["SPT2"] = pd.to_numeric(data1["SPT2"],errors='coerce')
#         data3["SPT3"] = pd.to_numeric(data1["SPT3"],errors='coerce')
#         data3["PROF1"] = pd.to_numeric(data1["PROF1"],errors='coerce')        
#         data3["PROF2"] = pd.to_numeric(data1["PROF2"],errors='coerce')

#         Suma=[list(data3['SPT2'])[y]+list(data3['SPT3'])[y] for y in range(len(data3['SPT2']))]
#         Res4=list(np.repeat([' '],len(Suma), axis=0))
#         for i in range(len(Suma)):
#             if Suma[i]<=20:
#                 Res4[i]="Blando"
#             elif Suma[i]>20 and Suma[i]<=30:
#                 Res4[i]='Media'
#             else:
#                 Res4[i]='Duro'
        
#     if len(data2.index)>0:
#         data2.rename(columns={'wPercentage':'W','waterLimit':'wL','wp': 'wP','plasticityIndex': 'IP', 'usc': 'USC','volumen':'vol'},inplace=True)
#         data2.rename(columns={'percentageGravas':'Gravas','percentageArenas':'Arenas','percentageFinos': 'Finos'},inplace=True)
#         data3["W"] = pd.to_numeric(data2["W"],errors='coerce')               
#         data3['wL'] =pd.to_numeric(list(data2["wL"]),errors='coerce')        
#         data3["wP"] = pd.to_numeric(data2["wP"],errors='coerce')          
#         data3["IP"] = pd.to_numeric(data2["IP"],errors='coerce')       
#         data3["Gravas"] = pd.to_numeric(data2["Gravas"],errors='coerce')        
#         data3["Arenas"] = pd.to_numeric(data2["Arenas"],errors='coerce')         
#         data3["Finos"] = pd.to_numeric(data2["Finos"],errors='coerce')        
#         data3["vol"] = pd.to_numeric(data2["vol"],errors='coerce')
#         data3['USC']=data2['USC']

#         CC=[0.009*(list(data3['wL'])[i]-10) for i in range(len(data3['wL']))]
#         data3['Cc']=[round(i,3) for i in CC]

#         data3['eo']=[2.4*(data3['W'][i]/100) for i in range(len(data3['W']))]
        
#         Res3=list(data3['wL'])
#         for i in range(len(Res3)):
#             if Res3[i]<=50:
#                 Res3[i]='LL<50'
#             else:
#                 Res3[i]='LL>50'
        
#         base=pd.DataFrame({'Arena':data3["Arenas"],'Fino':data3["Finos"], 'Grava':data3["Gravas"]})
            

#         Res2=list(np.repeat([' '],len(base.index), axis=0))
#         for i in range(len(base.index)):
#             pos=np.array(np.where([base.iloc[i][x]==max(base.iloc[i]) for x in range(len(base.iloc[i]))])).flatten().tolist()
            
#             if len(pos)>0 and len(pos)<2:       
        
#                 a=list(base.iloc[i])
#                 a.pop(pos[0])
            
#                 seg=np.array(np.where([base.iloc[i][x]==max(a) for x in range(len(base.iloc[i]))])).flatten().tolist()
                
#                 if pos[0]==1 and seg[0]==2:
#                     Res2[i]='FG'
#                 elif pos[0]==0 and seg[0]==2:
#                     Res2[i]='AG'
#                 elif pos[0]==0 and seg[0]==1:
#                     Res2[i]='AF'
#                 elif pos[0]==1 and seg[0]==0:
#                     Res2[i]='FA'
#                 elif pos[0]==2 and seg[0]==1:
#                     Res2[i]='GF'
#                 elif pos[0]==2 and seg[0]==0:
#                     Res2[i]='GA'
#             elif len(pos)==2:
#                 if pos[0]==1 and pos[1]==2:
#                     Res2[i]='FG'
#                 elif pos[0]==0 and pos[1]==2:
#                     Res2[i]='AG'
#                 elif pos[0]==0 and pos[1]==1:
#                     Res2[i]='AF'
#                 elif pos[0]==1 and pos[1]==0:
#                     Res2[i]='FA'
#                 elif pos[0]==2 and pos[1]==1:
#                     Res2[i]='GF'
#                 elif pos[0]==2 and pos[1]==0:
#                     Res2[i]='GA'

                
#             else:
#                 Res2[i]=Res2[i]
               
    
#     r2='Res2' in locals()
#     r3='Res3' in locals()
#     r4='Res4' in locals()

    
   
#     if r2==r3==r4==True:
#         Res=[data['USC'][x]+Res2[x] + Res3[x] + Res4[x] for x in range(len(Res2))]
#     elif r2==r3==True:
#         Res=[data['USC'][x]+Res2[x] + Res3[x] for x in range(len(Res2))]
    
#     elif r2==r4==True:
#         Res=[data['USC'][x]+Res2[x] + Res4[x] for x in range(len(Res2))]
    
#     elif r3==r4==True:
#         Res=[data['USC'][x]+Res3[x] + Res4[x] for x in range(len(Res3))]
#     elif r4==True:
#         Res=[data['USC'][x]+Res4[x] for x in range(len(Res4))]
    
#     else:

#         return JsonResponse({})


#     data3['Res']=Res
#     tipo_S=data3['Res'].value_counts()
#     tipo_S=tipo_S.index.values
#     data3.index = list(range(len(list(data3['Res']))))
        
#     data3['res']=data3['Res']
        
#     RES=np.repeat([float(0)],len(list(data3['Res'])), axis=0)
#     for i in range(len(list(data3['Res']))):
#         k=0
#         while list(data3['Res'])[i]!=tipo_S[k]:
#             k=k+1
                
#         RES[i]=k
    

#     data3['Res']=RES

#     D_M=[0.5*(data3['PROF1'][i]+data3['PROF2'][i]) for i in range(len(data3['PROF2']))]

#     D=[i for i, x in enumerate(D_M) if D_M.count(x) > 1]

    
#     while len(D)>0:
#         D_M[max(D)]=D_M[max(D)]+0.001
#         D=[i for i, x in enumerate(D_M) if D_M.count(x) > 1]
   
#     data3['D_M']=D_M      
#     data3=data3.sort_values('D_M')
#     data3['Res']=pd.to_numeric(data3['Res'],errors='coerce')
#     R1 = pd.DataFrame(data['USC']).value_counts()
#     if len(data2.index)>0:           
#         R2 = pd.DataFrame(Res2).value_counts()
#         R3 = pd.DataFrame(Res3).value_counts()
        
        
#     D_Inter=np.repeat([float(0)],len(data3.index), axis=0)
#     D_Acu=np.repeat([float(0)],len(data3.index), axis=0)
#     Pred_M=np.repeat([float(0)],len(data3.index), axis=0)
#     A_Inter=np.repeat([float(0)],len(data3.index), axis=0)
#     A_Acu=np.repeat([float(0)],len(data3.index), axis=0)        
       

#     for i in range(1,len(data3.index)):
#         D_Inter[0]=0
#         D_Acu[0]=D_Inter[0]
#         Pred_M[0]=data3['Res'][0]
#         A_Inter[0]=0
#         A_Acu[0]=A_Inter[0]
            
#         D_Inter[i]=data3['PROF2'][i]-data3['PROF1'][i]
#         D_Acu[i]=D_Inter[i]+D_Acu[i-1]
#         Pred_M[i]=0.5*(data3['Res'][i]+data3['Res'][i-1])
#         A_Inter[i]=D_Inter[i]*Pred_M[i]
#         A_Acu[i]=A_Inter[i]+A_Acu[i-1]
    
    
#     Zx=np.repeat([float(0)],len(data3.index), axis=0)
#     for i in range(len(data3.index)):
#         Zx[i]=A_Acu[i]-((max(A_Acu)/max(D_Acu))*D_Acu[i])

   
#     data['D_Inter']=D_Inter
#     data['D_Acu']=D_Acu
#     data['Pred_M']=Pred_M
#     data['A_Inter']=A_Inter
#     data['A_Acu']=A_Acu

#     data3['Zx']= [round(abs(Zx)[i],5) for i in range(len(Zx))]
        
#     ZZ=[abs(Zx)[i] for i in range(len(Zx))]

#     point= np.column_stack((data3['D_M'],ZZ))
    
#     J=np.arange(0,2,0.01)
        
#     DPE=[]
#     for i in range(len(J)):
#         if len(point)>3:
#            DPE.append(rdp(point,J[i]))
#         else:
#             DPE.append(rdp(point,0))
    

#     d=np.repeat([float(0)],len(J), axis=0)
#     for i in range(len(J)):
#         d[i]=len(DPE[i])
#     d = pd.DataFrame(d)
#     frecuencia=d.value_counts()
#     f1=list(frecuencia)
    
#     pos= np.array(np.where([max(f1)==list(frecuencia)[i] for i in range(len(list(frecuencia))) ])).flatten().tolist()
    
#     dim=list(frecuencia.index.values[min(pos)])[0]
    
#     B = pd.DataFrame()
#     B['J']=J
#     B['d']=d
#     B=B[B['d']==dim]

#     if len(point)>3:
#        Epsilon=min(B['J'])
#     else:
#        Epsilon=0

#     DPE=rdp(point, Epsilon)
    
#     DPE=np.array(DPE)
    
#     data4=pd.DataFrame({'D_M':list(DPE[:,0]),'Zx': list(DPE[:,1])})
    

#     DPE=list(DPE[:,0])
   
#     Group=np.repeat([float(0)],len(data3['D_M']), axis=0)
#     j=1
#     for i in range(1,len(DPE)):   
#         b=[data3['D_M'][x]>=DPE[i-1] and data3['D_M'][x]<=DPE[i] for x in range(len(data3['D_M']))]
#         Group[np.array(np.where(b)).flatten().tolist()]=j
#         j=j+1
        
    
#     Grupos = pd.Series(Group, name='Estratos')
#     USC = pd.Series(data['USC'], name='Suelo')
#     table = pd.crosstab(Grupos,USC )
#     inter=list(DPE)
#     Inicio=np.repeat([float(0)],len(table.index), axis=0)
#     Fin=np.repeat([float(0)],len(table.index), axis=0)

#     for i in range(len(table.index)):
#         Inicio[i]=round(inter[i],2)
#         Fin[i]=round(inter[i+1],2)

#     dataf=pd.DataFrame({'ProfundidadInicial':Inicio,'ProfundidadFinal':Fin})
        
#     data3['Group']=[round(i,3) for i in Group]
        
#     v1='R2' in locals()

#     if v1==True and len(R2)>=len(R1) and len(R1)>=len(R3):
#         sig='La variable que más aportó en la definición de los estratos fue Arenas, gravas y finos, seguido de USC'
#     elif v1==True and len(R2)>=len(R1) and len(R1)<len(R3):
#        sig='La variable que más aportó en la definición de los estratos fue Arenas, Gravas y finos, seguido del limite liquido'
            
#     elif v1==True and len(R1)>=len(R2) and len(R2)>=len(R3):
#         sig='La variable que más aportó en la definición de los estratos fue USC, seguido de  Arenas, Gravas y finos'
            
#     elif v1==True and len(R1)>=len(R2) and len(R2)<len(R3):
#         sig='La variable que más aportó en la definición de los estratos fue USC, seguido de limite liquido'

#     elif v1==True and len(R3)>=len(R2) and len(R2)>=len(R1):
#         sig='La variable que más aportó en la definición de los estratos fue Limite liquido, seguido de Arenas, gravas y finos'
            
#     else:
#         sig='Se utilizó la clasificación primaria y los SPT para definir los estratos'

    
#     if 'Cc' in data3.columns:      
#         ccM=data3.groupby("Group").agg({"Cc":"mean"}).rename(columns ={"Cc":"MediaCc"})
#         dataf['Cc'] = list(ccM.iloc[:,0])
        
        
#     if 'eo' in data3.columns:      
#         e0M=data3.groupby("Group").agg({"eo":"mean"}).rename(columns ={"eo":"Mediaeo"})
#         dataf['e0'] = list(e0M.iloc[:,0])
        

#     if 'W' in data3.columns:      
#         Wmin=list(pd.DataFrame(data3.groupby("Group").agg({"W":"min"}).rename(columns ={"W":"Minimo W"})).iloc[:,0])
#         Wmax=list(pd.DataFrame(data3.groupby("Group").agg({"W":"max"}).rename(columns ={"W":"Máximo W"})).iloc[:,0])
#         dataf['W_min'] = Wmin
#         dataf['W_max'] = Wmax

#     if 'wL' in data3.columns:      
#         WLmin=list(pd.DataFrame(data3.groupby("Group").agg({"wL":"min"}).rename(columns ={"wL":"Minimo WL"})).iloc[:,0])
#         WLmax=list(pd.DataFrame(data3.groupby("Group").agg({"wL":"max"}).rename(columns ={"wL":"Máximo WL"})).iloc[:,0])
#         dataf['WL_min'] = WLmin
#         dataf['WL_max'] = WLmax


#     if 'wP' in data3.columns:     
#         WPmin=list(pd.DataFrame(data3.groupby("Group").agg({"wP":"min"}).rename(columns ={"wP":"Minimo WL"})).iloc[:,0])
#         WPmax=list(pd.DataFrame(data3.groupby("Group").agg({"wP":"max"}).rename(columns ={"wP":"Máximo WL"})).iloc[:,0])
#         dataf['WP_min'] = WPmin
#         dataf['WP_max'] = WPmax

#     if 'IP' in data3.columns:
#         IPmin=list(pd.DataFrame(data3.groupby("Group").agg({"IP":"min"}).rename(columns ={"IP":"Minimo IP"})).iloc[:,0])
#         IPmax=list(pd.DataFrame(data3.groupby("Group").agg({"IP":"max"}).rename(columns ={"IP":"Máximo IP"})).iloc[:,0])
#         dataf['IP_min'] = IPmin
#         dataf['IP_max'] = IPmax
        
#     if 'vol' in data3.columns:
#         Vmin=list(pd.DataFrame(data3.groupby("Group").agg({"vol":"min"}).rename(columns ={"vol":"Minimo vol"})).iloc[:,0])
#         Vmax=list(pd.DataFrame(data3.groupby("Group").agg({"vol":"max"}).rename(columns ={"vol":"Máximo vol"})).iloc[:,0])
#         dataf['Vol_min'] = Vmin
#         dataf['VOl_max'] = Vmax
    
   
#     Usc=[pd.DataFrame(table).columns[np.where(pd.DataFrame(table).iloc[i]==  max(pd.DataFrame(table).iloc[0]))][0] for i in range(len(dataf.index))]

#     dataf['TipoSuelo']=Usc
    

#     y=list(data3['Zx'])+list(data4['Zx'])
    
#     x=list(data3['D_M'])+list(data4['D_M'])
#     es=list(np.repeat(['Muestra'],len(data3.index), axis=0))+list(np.repeat(['Estimado'],len(data4.index), axis=0))
#     base=pd.DataFrame({'X':x,'Y':y,'Estrato':es})

#     myplot=p.ggplot(data=base,
#         mapping=p.aes(x='X', y='Y', color='Estrato'))   + p.geom_line() +p.ylab("")  + p.xlab("Profundidad promedio") + p.scale_x_log10() + p.theme_bw()+ p.theme(text=p.element_text(size=16))


#     myPlot= myplot.draw()
#     plt.yticks([])

#     # myplot.save("myplot.png", dpi=600)   
#     # myPlot.savefig("myPlot.png",  dpi=800,) 
        
#     return JsonResponse(dataf.to_dict('records'), safe=False)
