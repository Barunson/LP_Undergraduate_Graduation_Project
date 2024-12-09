#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 00:07:18 2022

@author: daisuke
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import shutil
import sys
import os.path
from pyomo.environ import *


#Productos por linea y su cantidad de productos
V1 = pd.read_excel(r'inputs.xlsx', sheet_name = 'Vitaline01')
V1 = dict([(i,[a,b]) for i,a,b in zip(V1.Codigo, V1.Eficiencia, V1.Velocidad)])
V1Lista = list(V1.keys())
V1largo = len(V1Lista)

V3 = pd.read_excel(r'inputs.xlsx', sheet_name = 'Vitaline03')
V3 = dict([(i,[a,b]) for i,a,b in zip(V3.Codigo, V3.Eficiencia, V3.Velocidad)])
V3Lista = list(V3.keys())
V3largo = len(V3Lista)

P08 = pd.read_excel(r'inputs.xlsx', sheet_name = 'Polo08') 
P08 = dict([(i,[a,b]) for i,a,b in zip(P08.Codigo, P08.Eficiencia, P08.Velocidad)])
P08Lista = list(P08.keys())
P08largo = len(P08Lista)

P12 = pd.read_excel(r'inputs.xlsx', sheet_name = 'Polo12') 
P12 = dict([(i,[a,b]) for i,a,b in zip(P12.Codigo, P12.Eficiencia, P12.Velocidad)])
P12Lista = list(P12.keys())
P12largo = len(P12Lista)

H2 = pd.read_excel(r'inputs.xlsx', sheet_name = 'Hinzet02')
H2 = dict([(i,[a,b]) for i,a,b in zip(H2.Codigo, H2.Eficiencia, H2.Velocidad)]) 
H2Lista = list(H2.keys())
H2largo = len(H2Lista)

FL = pd.read_excel(r'inputs.xlsx', sheet_name = 'Flexline')
FL = dict([(i,[a,b]) for i,a,b in zip(FL.Codigo, FL.Eficiencia, FL.Velocidad)]) 
FLLista = list(FL.keys())
FLlargo = len(FLLista)

L05 = pd.read_excel(r'inputs.xlsx', sheet_name = 'Linea05')
L05 = dict([(i,[a,b]) for i,a,b in zip(L05.Codigo, L05.Eficiencia, L05.Velocidad)]) 
L05Lista = list(L05.keys())
L05largo = len(L05Lista)

L06 = pd.read_excel(r'inputs.xlsx', sheet_name = 'Linea06')
L06 = dict([(i,[a,b]) for i,a,b in zip(L06.Codigo, L06.Eficiencia, L06.Velocidad)]) 
L06Lista = list(L06.keys())
L06largo = len(L06Lista)

L07 = pd.read_excel(r'inputs.xlsx', sheet_name = 'Linea07')
L07 = dict([(i,[a,b]) for i,a,b in zip(L07.Codigo, L07.Eficiencia, L07.Velocidad)]) 
L07Lista = list(L07.keys())
L07largo = len(L07Lista)

L09 = pd.read_excel(r'inputs.xlsx', sheet_name = 'Linea09')
L09 = dict([(i,[a,b]) for i,a,b in zip(L09.Codigo, L09.Eficiencia, L09.Velocidad)]) 
L09Lista = list(L09.keys())
L09largo = len(L09Lista)

L10 = pd.read_excel(r'inputs.xlsx', sheet_name = 'Linea10')
L10 = dict([(i,[a,b]) for i,a,b in zip(L10.Codigo, L10.Eficiencia, L10.Velocidad)]) 
L10Lista = list(L10.keys())
L10largo = len(L10Lista)

NumeroProductos = {'V1': V1largo , 'V3': V3largo, 'P08': P08largo, 'P12':P12largo, 
                   'H2': H2largo, 'FL': FLlargo, 'L05': L05largo, 'L06': L06largo,
                   'L07': L07largo, 'L09': L09largo, 'L10': L10largo}


#Demanda de productos
Demanda = pd.read_excel(r'inputs.xlsx', sheet_name = 'Demanda')
Demanda = Demanda[['Codigo', 'Cantidad']]
Demanda = dict([(i,a) for i, a in zip(Demanda.Codigo, Demanda.Cantidad) ])



#rendimiento produccion (cj/hr) (i,k) y eficiencia (%) (i, k)
RendimientoV1dic = {}
EficienciaV1dic = {}
for producto in V1Lista:
    RendimientoV1dic[(producto ,'V1')] = V1[producto][1]
    EficienciaV1dic[(producto, 'V1')] = V1[producto][0]

RendimientoV3dic = {}
EficienciaV3dic = {}
for producto in V3Lista:
    RendimientoV3dic[(producto ,'V3')] = V3[producto][1]
    EficienciaV3dic[(producto, 'V3')] = V3[producto][0]
    
RendimientoP08dic = {}
EficienciaP08dic = {}
for producto in P08Lista:
    RendimientoP08dic[(producto ,'P08')] = P08[producto][1]
    EficienciaP08dic[(producto ,'P08')] = P08[producto][0]

RendimientoP12dic = {}
EficienciaP12dic = {}
for producto in P12Lista:
    RendimientoP12dic[(producto ,'P12')] = P12[producto][1]
    EficienciaP12dic[(producto ,'P12')] = P12[producto][0]
    
RendimientoH2dic = {}
EficienciaH2dic = {}
for producto in H2Lista:
    RendimientoH2dic[(producto ,'H2')] = H2[producto][1]
    EficienciaH2dic[(producto ,'H2')] = H2[producto][0]
    
RendimientoFLdic = {}
EficienciaFLdic = {}
for producto in FLLista:
    RendimientoFLdic[(producto ,'FL')] = FL[producto][1]
    EficienciaFLdic[(producto ,'FL')] = FL[producto][0]

RendimientoL05dic = {}
EficienciaL05dic = {}
for producto in L05Lista:
    RendimientoL05dic[(producto ,'L05')] = L05[producto][1]
    EficienciaL05dic[(producto ,'L05')] = L05[producto][0]

RendimientoL06dic = {}
EficienciaL06dic = {}
for producto in L06Lista:
    RendimientoL06dic[(producto ,'L06')] = L06[producto][1]
    EficienciaL06dic[(producto ,'L06')] = L06[producto][0]

RendimientoL07dic = {}
EficienciaL07dic = {}
for producto in L07Lista:
    RendimientoL07dic[(producto ,'L07')] = L07[producto][1]
    EficienciaL07dic[(producto ,'L07')] = L07[producto][0]

RendimientoL09dic = {}
EficienciaL09dic = {}
for producto in L09Lista:
    RendimientoL09dic[(producto ,'L09')] = L09[producto][1]
    EficienciaL09dic[(producto ,'L09')] = L09[producto][0]

RendimientoL10dic = {}
EficienciaL10dic = {}
for producto in L10Lista:
    RendimientoL10dic[(producto ,'L10')] = L10[producto][1]
    EficienciaL10dic[(producto ,'L10')] = L10[producto][0]


Rendimiento = {**RendimientoV1dic, **RendimientoV3dic, **RendimientoP08dic,
               **RendimientoP12dic, **RendimientoH2dic, **RendimientoFLdic,
               **RendimientoL05dic, **RendimientoL06dic, **RendimientoL07dic,
               **RendimientoL09dic, **RendimientoL10dic}

Eficiencia = {**EficienciaV1dic, **EficienciaV3dic, **EficienciaP08dic,
              **EficienciaP12dic, **EficienciaH2dic, **EficienciaFLdic,
              **EficienciaL05dic, **EficienciaL06dic, **EficienciaL07dic,
              **EficienciaL09dic, **EficienciaL10dic}


#Capacidad de produccion efectiva Rendimiento*Eficiencia
RendimientoEfectivo={}
RendimientoEfectivo2={}
for producto in Rendimiento:
    RendimientoEfectivo[producto] = Rendimiento[producto] * Eficiencia[producto]
    RendimientoEfectivo2[producto] = Rendimiento[producto] * (Eficiencia[producto]**2)

#Paros planeados (i,k)
#Calculo tiempos paros planeados Apertura la variable S (min)
MatrizParosPlaneados = pd.read_excel(r'inputs.xlsx', sheet_name = 'ParosPlaneados')

PPV1S={}
for producto in V1Lista:
    PPV1S[(producto,'V1')] = (MatrizParosPlaneados.iloc[0,1])/60

PPV3S={}
for producto in V3Lista:
    PPV3S[(producto,'V3')] = (MatrizParosPlaneados.iloc[1,1])/60
    
PPP08S={}
for producto in P08Lista:
    PPP08S[(producto,'P08')] = (MatrizParosPlaneados.iloc[2,1])/60

PPP12S={}
for producto in P12Lista:
    PPP12S[(producto,'P12')] = (MatrizParosPlaneados.iloc[3,1])/60

PPH2S={}
for producto in H2Lista:
    PPH2S[(producto,'H2')] = (MatrizParosPlaneados.iloc[4,1])/60

PPL05S={}
for producto in L05Lista:
    PPL05S[(producto,'L05')] = (MatrizParosPlaneados.iloc[5,1])/60

PPL06S={}
for producto in L06Lista:
    PPL06S[(producto,'L06')] = (MatrizParosPlaneados.iloc[6,1])/60

PPL07S={}
for producto in L07Lista:
    PPL07S[(producto,'L07')] = (MatrizParosPlaneados.iloc[7,1])/60

PPL09S={}
for producto in L09Lista:
    PPL09S[(producto,'L09')] = (MatrizParosPlaneados.iloc[8,1])/60

PPL10S={}
for producto in L10Lista:
    PPL10S[(producto,'L10')] = (MatrizParosPlaneados.iloc[9,1])/60

PPFLS={}
for producto in FLLista:
    PPFLS[(producto,'FL')] = (MatrizParosPlaneados.iloc[10,1])/60


ParoPlaneadoS = {**PPV1S, **PPV3S, **PPP08S, **PPP12S, **PPH2S, **PPL05S, 
                 **PPL06S, **PPL07S, **PPL09S, **PPL10S, **PPFLS}


#Paros planeados (i,k)
#Calculo tiempos paros planeados Cierre para la variable F (min)
PPV1F={}
for producto in V1Lista:
    PPV1F[(producto,'V1')] = (MatrizParosPlaneados.iloc[0,4])/60

PPV3F={}
for producto in V3Lista:
    PPV3F[(producto,'V3')] = (MatrizParosPlaneados.iloc[1,4])/60

PPP08F={}
for producto in P08Lista:
    PPP08F[(producto,'P08')] = (MatrizParosPlaneados.iloc[2,4])/60

PPP12F={}
for producto in P12Lista:
    PPP12F[(producto,'P12')] = (MatrizParosPlaneados.iloc[3,4])/60

PPH2F={}
for producto in H2Lista:
    PPH2F[(producto,'H2')] = (MatrizParosPlaneados.iloc[4,4])/60

PPL05F={}
for producto in L05Lista:
    PPL05F[(producto,'L05')] = (MatrizParosPlaneados.iloc[5,4])/60

PPL06F={}
for producto in L06Lista:
    PPL06F[(producto,'L06')] = (MatrizParosPlaneados.iloc[6,4])/60

PPL07F={}
for producto in L07Lista:
    PPL07F[(producto,'L07')] = (MatrizParosPlaneados.iloc[7,4])/60

PPL09F={}
for producto in L09Lista:
    PPL09F[(producto,'L09')] = (MatrizParosPlaneados.iloc[8,4])/60

PPL10F={}
for producto in L10Lista:
    PPL10F[(producto,'L10')] = (MatrizParosPlaneados.iloc[9,4])/60

PPFLF={}
for producto in FLLista:
    PPFLF[(producto,'FL')] = (MatrizParosPlaneados.iloc[10,4])/60
    

ParoPlaneadoF = {**PPV1F, **PPV3F, **PPP08F, **PPP12F, **PPH2F, **PPL05F, 
                 **PPL06F, **PPL07F, **PPL09F, **PPL10F, **PPFLF}



#Paro planeado Linea limpieza (min) y frecuencia de paro. Se dejara en Hrs
ParoPlaneadoV1XLinea = {}
FreqV1={}
for producto in V1Lista:
    ParoPlaneadoV1XLinea[(producto, 'V1')] = MatrizParosPlaneados.iloc[0,2]/60
    FreqV1[(producto,'V1')] = MatrizParosPlaneados.iloc[0,3]
    
ParoPlaneadoV3XLinea = {}
FreqV3={}
for producto in V3Lista:
    ParoPlaneadoV3XLinea[(producto, 'V3')] = MatrizParosPlaneados.iloc[1,2]/60
    FreqV3[(producto,'V3')] = MatrizParosPlaneados.iloc[1,3]

ParoPlaneadoP08XLinea = {}
FreqP08={}
for producto in P08Lista:
    ParoPlaneadoP08XLinea[(producto, 'P08')] = MatrizParosPlaneados.iloc[2,2]/60
    FreqP08[(producto, 'P08')] = MatrizParosPlaneados.iloc[2,3]

ParoPlaneadoP12XLinea = {}
FreqP12={}
for producto in P12Lista:
    ParoPlaneadoP12XLinea[(producto, 'P12')] = MatrizParosPlaneados.iloc[3,2]/60
    FreqP12[(producto,'P12')] = MatrizParosPlaneados.iloc[3,3]

ParoPlaneadoH2XLinea = {}
FreqH2={}
for producto in H2Lista:
    ParoPlaneadoH2XLinea[(producto, 'H2')] = MatrizParosPlaneados.iloc[4,2]/60
    FreqH2[(producto,'H2')] = MatrizParosPlaneados.iloc[4,3]
    
ParoPlaneadoL05XLinea = {}
FreqL05={}
for producto in L05Lista:
    ParoPlaneadoL05XLinea[(producto, 'L05')] = MatrizParosPlaneados.iloc[5,2]/60
    FreqL05[(producto,'L05')]= MatrizParosPlaneados.iloc[5,3]
    
ParoPlaneadoL06XLinea = {}
FreqL06={}
for producto in L06Lista:
    ParoPlaneadoL06XLinea[(producto, 'L06')] = MatrizParosPlaneados.iloc[6,2]/60
    FreqL06[(producto,'L06')]= MatrizParosPlaneados.iloc[6,3]

ParoPlaneadoL07XLinea = {}
FreqL07={}
for producto in L07Lista:
    ParoPlaneadoL07XLinea[(producto, 'L07')] = MatrizParosPlaneados.iloc[7,2]/60
    FreqL07[(producto,'L07')] = MatrizParosPlaneados.iloc[7,3]

ParoPlaneadoL09XLinea = {}
FreqL09={}
for producto in L09Lista:
    ParoPlaneadoL09XLinea[(producto, 'L09')] = MatrizParosPlaneados.iloc[8,2]/60
    FreqL09[(producto,'L09')] = MatrizParosPlaneados.iloc[8,3]

ParoPlaneadoL10XLinea = {}
FreqL10={}
for producto in L10Lista:
    ParoPlaneadoL10XLinea[(producto, 'L10')] = MatrizParosPlaneados.iloc[9,2]/60
    FreqL10[(producto,'L10')] = MatrizParosPlaneados.iloc[9,3]

ParoPlaneadoFLXLinea = {}
FreqFL={}
for producto in FLLista:
    ParoPlaneadoFLXLinea[(producto, 'FL')] = MatrizParosPlaneados.iloc[10,2]/60
    FreqFL[(producto,'FL')] = MatrizParosPlaneados.iloc[10,3]


ParoPlaneadoXLinea = {**ParoPlaneadoV1XLinea, **ParoPlaneadoV3XLinea, **ParoPlaneadoP08XLinea, **ParoPlaneadoP12XLinea,
                          **ParoPlaneadoH2XLinea, **ParoPlaneadoL05XLinea, **ParoPlaneadoL06XLinea, **ParoPlaneadoL07XLinea,
                          **ParoPlaneadoL09XLinea, **ParoPlaneadoL10XLinea, **ParoPlaneadoFLXLinea}


FreqPPXLinea = {**FreqV1, **FreqV3, **FreqP08, **FreqP12, **FreqH2, **FreqL05, **FreqL06,
                **FreqL07, **FreqL09, **FreqL10, **FreqFL}


#Indices
ListaLineas = list(NumeroProductos.keys())
ListaProductos = {'V1': V1Lista, 'V3': V3Lista, 'P08': P08Lista, 'P12': P12Lista, 'H2': H2Lista,
                  'FL': FLLista, 'L05': L05Lista, 'L06': L06Lista, 'L07':L07Lista, 'L09': L09Lista,
                  'L10':L10Lista
                  }



#Lista de indices 
ListaK= [k for k in ListaLineas] #Lista de lineas


#Creacion de diccionario conjunto de lineas que producen un producto determinado
##con esto, quedan pareadas las lineas con cada producto que elaboran            
ProductoLinea ={}
for k in ListaK:
    for i in ListaProductos[k]:
        if i not in ProductoLinea.keys():
            ProductoLinea[i] = [k]
        else:
            ProductoLinea[i].append(k)


indice= [(i,k) for i in list(ProductoLinea.keys()) for k in ProductoLinea[i]] #Todas las combinaciones existentes de lineas y productos 


#Paro planeado de arranque para cada linea
ParoPlaneadoS2 = {}
for k in ListaK:
    for i in ListaProductos[k]:
        ParoPlaneadoS2[k] = ParoPlaneadoS[(i,k)]
        break

#Paro planeado de cierre para cada linea 
ParoPlaneadoF2 = {}
for k in ListaK:
    for i in ListaProductos[k]:
        ParoPlaneadoF2[k] = ParoPlaneadoF[(i,k)]
        break




#----------------------------------Creacion instancia modelo----------------------------------------------
modelo = pyomo.environ.ConcreteModel()

#Definicion de variables de decision
modelo.X = pyomo.environ.Var(indice , domain = NonNegativeReals, name= "X", initialize=0,  bounds=(0,136))
modelo.ZL = pyomo.environ.Var(indice , domain = NonNegativeIntegers, name="Zl" , initialize=0)
modelo.ZK = pyomo.environ.Var(indice, domain = NonNegativeIntegers, name="ZK", initialize=0)
modelo.Y = pyomo.environ.Var(ParoPlaneadoS2.keys() , domain = Binary, name="Y" , initialize=0)
modelo.W = pyomo.environ.Var(indice,domain = Binary, name="W", initialize=0)

BigM = 136

#Funcion Objetivo
modelo.UL=pyomo.environ.Objective(
    expr = sum(modelo.X[(i,k)] for i in list(ProductoLinea.keys()) for k in ProductoLinea[i] ) ,
    sense= maximize
    )


#Definicion de restricciones
modelo.Constraint = pyomo.environ.ConstraintList()


#(1) Restriccion que activa la variable W cuando se produce X
## Variable binaria para activar el PP de Arranque por cada producto
for e in indice:
    modelo.Constraint.add(expr= modelo.X[e] <= modelo.W[e] * BigM)


#(2) Restricción que activa la variable Y cuando se produce X
## Variable binaria para activar el PP de Cierre (Aplica una sola vez en la producción en la linea k)
for k in ListaK:
    for i in ListaProductos[k]:
        modelo.Constraint.add(expr = sum(modelo.X[(i,k)] for i in ListaProductos[k]) <= modelo.Y[(k)] * BigM)


#(3)Restricción tiempo disponible
for k in ListaK:
    modelo.Constraint.add(expr= sum((modelo.X[(i,k)] / Eficiencia[(i,k)]) for i in ListaProductos[k]) <= 136 - 
                          sum(ParoPlaneadoS2[k] * modelo.W[(i,k)] for i in ListaProductos[k]) - 
                          sum(ParoPlaneadoXLinea[(i,k)]*modelo.ZL[(i,k)] for i in ListaProductos[k]) - 
                          ParoPlaneadoF2[k] * modelo.Y[k])


#(4)Restriccion demanda
for i in list(ProductoLinea.keys()):
    modelo.Constraint.add(expr=sum(modelo.X[(i,k)] * RendimientoEfectivo[(i,k)] for k in ProductoLinea[i]) <= 
                          Demanda[i])


#(5)Restriccion Aproximación/Redondeo frecuencia paros planeados por linea
for e in indice:
    modelo.Constraint.add(expr= ((modelo.X[e] / Eficiencia[e]) + ParoPlaneadoS2[e[1]] * modelo.W[e] +  
                                 ParoPlaneadoXLinea[e] * modelo.ZL[e] + 
                                 ParoPlaneadoF2[e[1]] * modelo.Y[e[1]])/(8* FreqPPXLinea[e]) <= 
                                 modelo.ZL[e] + 1)


#Resultados
resultados = pyomo.environ.SolverFactory('SCIP').solve(modelo)


resultados.write()

print(pyomo.environ.value(modelo.UL))

for k in  ListaK:
    print('Y[%s]:%s'%(k,pyomo.environ.value(modelo.Y[k])))
    for i in ListaProductos[k]:
        if pyomo.environ.value(modelo.X[(i,k)]) > 0:
            print('W[%s,%s]:%s'%(i,k,pyomo.environ.value(modelo.W[(i,k)])))
            print('X[%s,%s]:%s'%(i,k,pyomo.environ.value(modelo.X[(i,k)])))
            print('ZL[%s,%s]:%s'%(i,k,pyomo.environ.value(modelo.ZL[(i,k)])))
            
            

#------------------------------ CARTA GANTT AUTOMATIZADA ------------------------------------------

#Definición funcion que calcula la barra segmentada y vectores para su ploteo
def FuncBarra(X, Barra, Acum, PPS, PPXF, Freq):
    global Position
    i=0
    if X==0:
        Acum+=0
        Position+=0

    if X > 0 and Position > 0:
        stop = True
        while Acum <= X and stop==True :
            if X <= 8 * Freq - PPS and i==0:
                Barra.append((Position + PPS, X))
                Acum+=X
                Position+= X + PPS
                #print("1 Acum(1)=", Acum, "Position=", Position, "i=", i)
                stop=False
                break
            
            if X > 8 * Freq - PPS and i==0:
                Barra.append((Position + PPS, 8*Freq - PPS))
                Acum+= 8*Freq - PPS
                Position+= Acum + PPS
                #print("1 Acum(2)=", Acum, "Position=", Position, "i=", i)
                i+=1
            
            if X - Acum > 8*Freq - PPXF:
                Barra.append((Position + PPXF, 8*Freq - PPXF))
                Acum+= 8*Freq - PPXF
                Position+= 8*Freq  
                #print("1 Acum(3)=", Acum, "Position=", Position, "i=", i)
                i+=1
                
        
            if X - Acum <= 8*Freq - PPXF:
                Barra.append((Position + PPXF, X - Acum))
                Position += X - Acum + PPXF
                Acum+= X - Acum
                #print("1 Acum(4)=", Acum, "Position=", Position, "i=", i)
                i+=1
                stop=False
                Position=Position
                break
    
            
    if X > 0 and Position==0:
        stop= True
        while Acum <= X and stop == True :
            if X <= 8*Freq - PPS and i==0:
                Barra.append((PPS, X))
                Acum+=X
                Position+=X + PPS
                #print("1 Acum(1)=", Acum, "Position=", Position, "i=", i)            
                stop = False
                break
            
            if X > 8*Freq - PPS and i==0:
                Barra.append((PPS, 8*Freq - PPS))
                Acum+= 8*Freq -PPS
                Position+= Acum + PPS
                #print("1 Acum(2)=", Acum, "Position=", Position, "i=", i)
                i+=1
            
            if X - Acum > 8*Freq - PPXF:
                Barra.append((Position  + PPXF, 8*Freq - PPXF))
                Acum+= 8*Freq - PPXF
                Position+= 8*Freq
                #print("1 Acum(3)=", Acum, "Position=", Position, "i=", i)
                i+=1
                
        
            if X - Acum <= 8*Freq - PPXF:
                Barra.append((Position + PPXF, X - Acum))
                Position += X - Acum + PPXF
                Acum+= X - Acum
                #print("1 Acum(4)=", Acum, "Position=", Position, "i=", i)
                i+=1
                stop= False
                break
    


#Definicion funcion para producciones sin PPfreq (para linea L06 y L10)
def FuncBarraNofreq(X, Barra, Acum, PPS):
    global Position
    if X==0:
        Acum+=0
        Position+=0

    if X > 0 and Position > 0:
        Barra.append((Position + PPS, X))
        Position+= X + PPS
        #print("2 Acum(1)=", Acum, "Position=", Position, "i=", i)
        
    if X > 0 and Position == 0:
        Barra.append((PPS, X))
        Position= X + PPS
        #print("1 Acum(1)=", Acum, "Position=", Position, "i=", i)




indiceSorted = [
(12034915,'V1'),(12035120,'V1'),(12076018,'V1'),(12495503,'V1'),(12370207,'V1'),
(12034915,'V3'),(12035120,'V3'),(12076018,'V3'),(12370206,'V3'),(12023357,'V3'),(12219159,'V3'),
(12373369,'V3'),(12495503,'V3'),(12373400,'V3'),(12422018,'V3'),(12422050,'V3'),(12422068,'V3'),
(12499889,'V3'),(12499897,'V3'),(12499728,'V3'),(12422077,'V3'),
(12263770,'P08'),(12370209,'P08'),(12023357,'P08'),(12219159,'P08'),(12373369,'P08'),(12373400,'P08'),
(12383496,'P08'),
(12076018,'P12'),(12094971,'P12'),(12312462,'P12'),(12357636,'P12'),(12455336,'P12'),(12422019,'P12'),
(12422299,'P12'),(12422311,'P12'),(12422312,'P12'),(12380329,'P12'),
(12018322,'H2'),(12018358,'H2'),(12018359,'H2'),(12018364,'H2'),(12018422,'H2'),(12018423,'H2'),
(12018424,'H2'),(12018425,'H2'),(12329510,'H2'),(12018554,'H2'),(12465140,'H2'),(12465129,'H2'),
(12465131,'H2'),(12112705,'H2'),
(12018322,'FL'),(12018358,'FL'),(12018359,'FL'),(12018364,'FL'),(12112705,'FL'),(12018422,'FL'),
(12018423,'FL'),(12018424,'FL'),(12018425,'FL'),(12018554,'FL'),(12137923,'FL'),(12137924,'FL'),
(12137925,'FL'),(12138093,'FL'),(12385967,'FL'),(12385968,'FL'),(12100169,'FL'),(12100210,'FL'),
(12132728,'L05'),(12132730,'L05'),(12132731,'L05'),(12132734,'L05'),(12133126,'L05'),(12133127,'L05'),
(12133128,'L05'),(12133129,'L05'),(12133140,'L05'),(12161632,'L05'),(12192064,'L05'),(12304308,'L05'),
(12312257,'L05'),(12319020,'L05'),(12383494,'L05'),(12383495,'L05'),(12317444,'L05'),(12317902,'L05'),
(12393729,'L05'),(12453432,'L05'),(12373842,'L05'),(12373843,'L05'),(12373979,'L05'),(12374036,'L05'),
(12374037,'L05'),(12374038,'L05'),(12374150,'L05'),(12374151,'L05'),(12374152,'L05'),(12374153,'L05'),
(12374154,'L05'),(12416312,'L05'),(12418242,'L05'),(12422298,'L05'),(12453760,'L05'),(12100169,'L05'),
(12100210,'L05'),(12385968,'L05'),(12137923,'L05'),(12137924,'L05'),(12137925,'L05'),(12463663,'L05'),
(12502458,'L05'),(12502459,'L05'),(12463646,'L05'),(12463648,'L05'),(12138093,'L05'),(12018358,'L05'),
(12018359,'L05'),(12018423,'L05'),(12018364,'L05'),(12018424,'L05'),(12112705,'L05'),
(12114456,'L06'),(12114459,'L06'),(12114480,'L06'),(12114481,'L06'),(12114491,'L06'),(12182331,'L06'),
(12018358,'L06'),(12018359,'L06'),(12018364,'L06'),(12018423,'L06'),(12018554,'L06'),(12112705,'L06'),
(12100169,'L06'),(12100210,'L06'),(12385967,'L06'),(12385968,'L06'),(12137923,'L06'),
(12018358,'L07'),(12018359,'L07'),(12018364,'L07'),(12018423,'L07'),(12018424,'L07'),(12112705,'L07'),
(12100210,'L07'),(12385967,'L07'),(12385968,'L07'),(12298926,'L07'),(12299009,'L07'),(12497906,'L07'),
(12292621,'L07'),(12438596,'L07'),(12438597,'L07'),(12462606,'L07'),(12462857,'L07'),(12462856,'L07'),
(12319674,'L09'),(12319791,'L09'),(12345021,'L09'),(12415825,'L09'),(12416326,'L09'),(12417172,'L09'),
(12487665,'L09'),(12493875,'L09'),(12495499,'L09'),(12462115,'L09'),(12417974,'L09'),(12418229,'L09'),
(12316605,'L09'),(12316606,'L09'),(12422452,'L09'),(12450923,'L09'),(12487681,'L09'),(12462103,'L09'),
(12018358,'L09'),(12018359,'L09'),(12018364,'L09'),(12018423,'L09'),(12018424,'L09'),(12112705,'L09'),
(12100169,'L09'),(12100210,'L09'),(12385967,'L09'),(12385968,'L09'),
(12294153,'L10'),(12294154,'L10'),(12295105,'L10'),(12415993,'L10'),(12495428,'L10'),(12495279,'L10'),
(12462083,'L10'),(12462085,'L10'),(12316602,'L10'),(12316603,'L10'),(12418228,'L10'),(12132728,'L10'),
(12132730,'L10'),(12132731,'L10'),(12132734,'L10'),(12133126,'L10'),(12133127,'L10'),(12133128,'L10'),
(12133129,'L10'),(12133140,'L10'),(12161632,'L10'),(12192064,'L10'),(12304308,'L10'),(12312257,'L10'),
(12319020,'L10'),(12501513,'L10'),(12383494,'L10'),(12383495,'L10'),(12100169,'L10'),(12100210,'L10'),
(12385967,'L10'),(12385968,'L10'),(12137923,'L10'),(12137924,'L10'),(12137925,'L10'),(12463663,'L10'),
(12463646,'L10'),(12138093,'L10'),(12463648,'L10'),(12018423,'L10')
]


fig, gnt = plt.subplots(figsize=(11,6))

        
#Lista de valores de produccion X en orden respectivo y nombres de producto+linea
Lista_Lineas=[]
lista_x =[]
lista_nombre_yplot=[]
lista_rendimiento_efectivo=[]
for e in indiceSorted:
    lista_x.append(pyomo.environ.value(modelo.X[(e)]) / Eficiencia[(e)]) #from here we use the real production time
    lista_nombre_yplot.append((e[1])+'_'+str(e[0]))
    Lista_Lineas.append(e[1])
    lista_rendimiento_efectivo.append(RendimientoEfectivo2[(e)]) #we have to multiply two times so we can get the real production

#Listas ordenada con valores de paros planeados tuples (PPS, PPF, PPXF)
lista_PP=[]
for e in indiceSorted:
    if e[1]=='V1':
        lista_PP.append(((MatrizParosPlaneados.iloc[0,1])/60,
                        (MatrizParosPlaneados.iloc[0,4])/60,
                          MatrizParosPlaneados.iloc[0,2]/60)) #tercer elemento del tuple corresponde a la freq de paro
        
    if e[1]=='V3':
        lista_PP.append(((MatrizParosPlaneados.iloc[1,1])/60,
                         (MatrizParosPlaneados.iloc[1,4])/60,
                          MatrizParosPlaneados.iloc[1,2]/60))

    if e[1]=='P08':
        lista_PP.append(((MatrizParosPlaneados.iloc[2,1])/60,
                         (MatrizParosPlaneados.iloc[2,4])/60,
                         MatrizParosPlaneados.iloc[2,2]/60))
        
    if e[1]=='P12':
        lista_PP.append(((MatrizParosPlaneados.iloc[3,1])/60,
                         (MatrizParosPlaneados.iloc[3,4])/60,
                         MatrizParosPlaneados.iloc[3,2]/60))
        
    if e[1]=='H2':
        lista_PP.append(((MatrizParosPlaneados.iloc[4,1])/60,
                         (MatrizParosPlaneados.iloc[4,4])/60,
                         MatrizParosPlaneados.iloc[4,2]/60))
        
    if e[1]=='L05':
        lista_PP.append(((MatrizParosPlaneados.iloc[5,1])/60,
                         (MatrizParosPlaneados.iloc[5,4])/60,
                         MatrizParosPlaneados.iloc[5,2]/60))
        
    if e[1]=='L06':
        lista_PP.append(((MatrizParosPlaneados.iloc[6,1])/60,
                         (MatrizParosPlaneados.iloc[6,4])/60,
                         MatrizParosPlaneados.iloc[6,2]/60))
        
    if e[1]=='L07':
        lista_PP.append(((MatrizParosPlaneados.iloc[7,1])/60,
                         (MatrizParosPlaneados.iloc[7,4])/60,
                         MatrizParosPlaneados.iloc[7,2]/60))
        
    if e[1]=='L09':
        lista_PP.append(((MatrizParosPlaneados.iloc[8,1])/60,
                         (MatrizParosPlaneados.iloc[8,4])/60,
                         MatrizParosPlaneados.iloc[8,2]/60))
        
    if e[1]=='L10':
        lista_PP.append(((MatrizParosPlaneados.iloc[9,1])/60,
                         (MatrizParosPlaneados.iloc[9,4])/60,
                         MatrizParosPlaneados.iloc[9,2]/60))
        
    if e[1]=='FL':
        lista_PP.append(((MatrizParosPlaneados.iloc[10,1])/60,
                         (MatrizParosPlaneados.iloc[10,4])/60,
                         (MatrizParosPlaneados.iloc[10,2])/60))


#Achicando lista_x, lista_nombre_yplot, lista_PP, Lista_Lineas para plotear solo los productos que 
#son fabricados efectivamente 
Lista_prod_Lineas=[]
lista_prod_x=[]
lista_prod_yplot=[]
lista_prod_PP=[]
lista_prod_rendimiento_efectivo=[]
for i in range(len(lista_x)):
    if lista_x[i]>0:
        lista_prod_x.append(lista_x[i])
        lista_prod_yplot.append(lista_nombre_yplot[i])
        lista_prod_PP.append(lista_PP[i])
        Lista_prod_Lineas.append(Lista_Lineas[i])
        lista_prod_rendimiento_efectivo.append(lista_rendimiento_efectivo[i])        

print(indiceSorted)
        
#Numero de barras para ploteo
numBar = len(lista_prod_x)

#Setting margin as a percentage of the total number of bars 
margin_percentage=10

# Calculate the y-axis limits
y_min = 0
y_max = (numBar*10) + 10

#Defining plot dimensions
gnt.set_ylim(y_min, y_max)
gnt.set_xlim(0,136)

#Setting labels for x,y axis
gnt.set_xlabel('Hrs.')  # X-axis label
gnt.set_ylabel('Line_prod')           # Y-axis label

#calculating bar title positions on Y axis
BarTitle_positions =[((i+1)*10)+5 for i in range(numBar)]

#Setting bar positions
BarPosition=[(i+1)*10 for i in range(numBar)]
BarPositionReversed = BarPosition[::-1]

#Position of every bar and product naming
gnt.set_yticks(BarTitle_positions)
gnt.set_yticklabels(lista_prod_yplot[::-1]) #reversing element order by slicing method

#Vectors of planned stops (starting, finishing) and stopping frequency
#Defining vectors to define bar segmentations
Barra=[]
count_V1=0 
count_V3=0
count_P08=0
count_P12=0
count_H2=0
count_L05=0
count_L06=0
count_L07=0
count_L09=0
count_L10=0
count_FL=0
for element in range(len(Lista_prod_Lineas)):
    if Lista_prod_Lineas[element]=='V1' and count_V1!=0:
        SubBar=[]
        Acum=0
        i=0
        FuncBarra(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0], lista_prod_PP[element][2], 3)
        Barra.append(SubBar)
        count_V1+=1
        
    if Lista_prod_Lineas[element]=='V1' and count_V1==0:
        SubBar=[]
        Position = 0
        Acum=0
        i=0
        FuncBarra(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0], lista_prod_PP[element][2], 3)
        Barra.append(SubBar)
        count_V1+=1
        
    if Lista_prod_Lineas[element]=='V3' and count_V3!=0:
        SubBar=[]
        Acum=0
        i=0
        FuncBarra(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0], lista_prod_PP[element][2], 3)
        Barra.append(SubBar)
        count_V3+=1    
        
    if Lista_prod_Lineas[element]=='V3' and count_V3==0:
        SubBar=[]
        Position = 0
        Acum=0
        i=0
        FuncBarra(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0], lista_prod_PP[element][2], 3)
        Barra.append(SubBar)
        count_V3+=1
        
    if Lista_prod_Lineas[element]=='P08' and count_P08!=0:
        SubBar=[]
        Acum=0
        i=0
        FuncBarra(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0], lista_prod_PP[element][2], 3)
        Barra.append(SubBar)
        count_P08+=1
    
    if Lista_prod_Lineas[element]=='P08' and count_P08==0:
        SubBar=[]
        Position = 0
        Acum=0
        i=0
        FuncBarra(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0], lista_prod_PP[element][2], 3)
        Barra.append(SubBar)
        count_P08+=1
        
    if Lista_prod_Lineas[element]=='P12' and count_P12!=0:
        SubBar=[]
        Acum=0
        i=0
        FuncBarra(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0], lista_prod_PP[element][2], 3)
        Barra.append(SubBar)
        count_P12+=1
    
    if Lista_prod_Lineas[element]=='P12' and count_P12==0:
        SubBar=[]
        Position = 0
        Acum=0
        i=0
        FuncBarra(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0], lista_prod_PP[element][2], 3)
        Barra.append(SubBar)
        count_P12+=1
        
    if Lista_prod_Lineas[element]=='H2' and count_H2!=0:
        SubBar=[]
        Acum=0
        i=0
        FuncBarra(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0], lista_prod_PP[element][2], 4)
        Barra.append(SubBar)
        count_H2+=1
    
    if Lista_prod_Lineas[element]=='H2' and count_H2==0:
        SubBar=[]
        Position = 0
        Acum=0
        i=0
        FuncBarra(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0], lista_prod_PP[element][2], 4)
        Barra.append(SubBar)
        count_H2+=1
        
    if Lista_prod_Lineas[element]=='L05' and count_L05!=0:
        SubBar=[]
        Acum=0
        i=0
        FuncBarra(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0], lista_prod_PP[element][2], 3)
        Barra.append(SubBar)
        count_L05+=1
    
    if Lista_prod_Lineas[element]=='L05' and count_L05==0:
        SubBar=[]
        Position = 0
        Acum=0
        i=0
        FuncBarra(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0], lista_prod_PP[element][2], 3)
        Barra.append(SubBar)
        count_L05+=1
        
    if Lista_prod_Lineas[element]=='L06' and count_L06!=0:
        SubBar=[]
        Acum=0
        i=0
        FuncBarraNofreq(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0])
        Barra.append(SubBar)
        count_L06+=1
        
    if Lista_prod_Lineas[element]=='L06' and count_L06==0: 
        SubBar=[]
        Position = 0
        Acum=0
        i=0
        FuncBarraNofreq(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0])
        Barra.append(SubBar)
        count_L06+=1
        
    if Lista_prod_Lineas[element]=='L07' and count_L07!=0:
        SubBar=[]
        Acum=0
        i=0
        FuncBarra(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0], lista_prod_PP[element][2], 3)
        Barra.append(SubBar)
        count_L07+=1
    
    if Lista_prod_Lineas[element]=='L07' and count_L07==0:
        SubBar=[]
        Position = 0
        Acum=0
        i=0
        FuncBarra(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0], lista_prod_PP[element][2], 3)
        Barra.append(SubBar)
        count_L07+=1
        
    if Lista_prod_Lineas[element]=='L09' and count_L09!=0:
        SubBar=[]
        Acum=0
        i=0
        FuncBarra(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0], lista_prod_PP[element][2], 3)
        Barra.append(SubBar)
        count_L09+=1
    
    if Lista_prod_Lineas[element]=='L09' and count_L09==0:
        SubBar=[]
        Position = 0
        Acum=0
        i=0
        FuncBarra(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0], lista_prod_PP[element][2], 3)
        Barra.append(SubBar)
        count_L09+=1
        
    if Lista_prod_Lineas[element]=='L10' and count_L10!=0: #####
        SubBar=[]
        Acum=0
        i=0
        FuncBarraNofreq(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0])
        Barra.append(SubBar)
        count_L10+=1
    
    if Lista_prod_Lineas[element]=='L10' and count_L10==0: #####
        SubBar=[]
        Position = 0
        Acum=0
        i=0
        FuncBarraNofreq(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0])
        Barra.append(SubBar)
        count_L10+=1
        
    if Lista_prod_Lineas[element]=='FL' and count_FL!=0:
        SubBar=[]
        Acum=0
        i=0
        FuncBarra(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0], lista_prod_PP[element][2], 3)
        Barra.append(SubBar)
        count_FL+=1
    
    if Lista_prod_Lineas[element]=='FL' and count_FL==0:
        SubBar=[]
        Position = 0
        Acum=0
        i=0
        FuncBarra(lista_prod_x[element],SubBar,Acum,lista_prod_PP[element][0], lista_prod_PP[element][2], 3)
        Barra.append(SubBar)
        count_FL+=1
        

#Calculating final position(total production + total PPXF) for each bar (OK)
Final_position=[]
for i in range(len(Barra)):
    Accum=0
    FinalPositionK=0
    for k in range(len(Barra[i])):
        Accum+=Barra[i][k][1]
        if k==len(Barra[i]) -1:
            FinalPositionK = Accum + (len(Barra[i]) - 1) * lista_prod_PP[i][2]
            Final_position.append(FinalPositionK)
            

#Bar plotting
for i in range(len(lista_prod_x)):
   #PP Start
   gnt.broken_barh([(Barra[i][0][0] - lista_prod_PP[i][0], lista_prod_PP[i][0])], (BarPositionReversed[i],9), facecolors = 'tab:green') 
   #PP by frequency
   gnt.broken_barh([(Barra[i][0][0], Final_position[i])], (BarPositionReversed[i],9), facecolors = 'tab:red') 
   #Actual working
   gnt.broken_barh(Barra[i], (BarPositionReversed[i],9), facecolors = 'tab:blue')
   
#Calculating amaount of products for each line 
V1_count=0
V3_count=0
P08_count=0
P12_count=0
H2_count=0
L05_count=0
L06_count=0
L07_count=0
L09_count=0
L10_count=0
FL_count=0
for i in range(len(Lista_prod_Lineas)):
    if Lista_prod_Lineas[i]=='V1':
        V1_count+=1
    if Lista_prod_Lineas[i]=='V3':
        V3_count+=1
    if Lista_prod_Lineas[i]=='P12':
        P12_count+=1
    if Lista_prod_Lineas[i]=='P08':
        P08_count+=1
    if Lista_prod_Lineas[i]=='H2':
        H2_count+=1
    if Lista_prod_Lineas[i]=='L05':
        L05_count+=1
    if Lista_prod_Lineas[i]=='L06':
        L06_count+=1
    if Lista_prod_Lineas[i]=='L07':
        L07_count+=1
    if Lista_prod_Lineas[i]=='L09':
        L09_count+=1
    if Lista_prod_Lineas[i]=='L10':
        L10_count+=1
    if Lista_prod_Lineas[i]=='FL':
        FL_count+=1
        
#Plotting the final PP on the last product of each line         
for i in range(len(Lista_prod_Lineas)):
    PositionPPF_count=0
    if Lista_prod_Lineas[i]=='V1' and i+1 == V1_count :
        gnt.broken_barh([(Barra[i][0][0] + Final_position[i], lista_prod_PP[i][1])], (BarPositionReversed[i],9), facecolors = 'tab:purple') 
        
    if Lista_prod_Lineas[i]=='V3' and i+1 == V1_count + V3_count :
        gnt.broken_barh([(Barra[i][0][0] + Final_position[i], lista_prod_PP[i][1])], (BarPositionReversed[i],9), facecolors = 'tab:purple') 
        
    if Lista_prod_Lineas[i]=='P08' and i+1 == V1_count + V3_count + P08_count:
        gnt.broken_barh([(Barra[i][0][0] + Final_position[i], lista_prod_PP[i][1])], (BarPositionReversed[i],9), facecolors = 'tab:purple')  
    
    if Lista_prod_Lineas[i]=='P12' and i+1 == V1_count + V3_count + P08_count + P12_count :
        gnt.broken_barh([(Barra[i][0][0] + Final_position[i], lista_prod_PP[i][1])], (BarPositionReversed[i],9), facecolors = 'tab:purple') 

    if Lista_prod_Lineas[i]=='H2' and i+1 == V1_count + V3_count + P08_count + P12_count + H2_count:
        gnt.broken_barh([(Barra[i][0][0] + Final_position[i], lista_prod_PP[i][1])], (BarPositionReversed[i],9), facecolors = 'tab:purple') 
        
    if Lista_prod_Lineas[i]=='FL' and i+1 == V1_count + V3_count + P08_count + P12_count + H2_count + FL_count :
        gnt.broken_barh([(Barra[i][0][0] + Final_position[i], lista_prod_PP[i][1])], (BarPositionReversed[i],9), facecolors = 'tab:purple') 

    if Lista_prod_Lineas[i]=='L05' and i+1 == V1_count + V3_count + P12_count + P08_count + H2_count + FL_count+ L05_count :
        gnt.broken_barh([(Barra[i][0][0] + Final_position[i], lista_prod_PP[i][1])], (BarPositionReversed[i],9), facecolors = 'tab:purple') 

    if Lista_prod_Lineas[i]=='L06' and i+1 == V1_count + V3_count + P12_count + P08_count + H2_count + FL_count+ L05_count + L06_count :
        gnt.broken_barh([(Barra[i][0][0] + Final_position[i], lista_prod_PP[i][1])], (BarPositionReversed[i],9), facecolors = 'tab:purple') 

    if Lista_prod_Lineas[i]=='L07' and i+1 == V1_count + V3_count + P12_count + P08_count + H2_count + FL_count+ L05_count + L06_count + L07_count :
        gnt.broken_barh([(Barra[i][0][0] + Final_position[i], lista_prod_PP[i][1])], (BarPositionReversed[i],9), facecolors = 'tab:purple') 

    if Lista_prod_Lineas[i]=='L09' and i+1 ==V1_count + V3_count + P12_count + P08_count + H2_count + FL_count+ L05_count + L06_count + L07_count + L09_count :
        gnt.broken_barh([(Barra[i][0][0] + Final_position[i], lista_prod_PP[i][1])], (BarPositionReversed[i],9), facecolors = 'tab:purple') 

    if Lista_prod_Lineas[i]=='L10' and i+1 == V1_count + V3_count + P12_count + P08_count + H2_count + FL_count+ L05_count + L06_count + L07_count + L09_count + L10_count :
        gnt.broken_barh([(Barra[i][0][0] + Final_position[i], lista_prod_PP[i][1])], (BarPositionReversed[i],9), facecolors = 'tab:purple') 



#printing results on txt
with open("Output.txt","w") as file:
    file.write("--------Production in hours---------- \n")
    
    for i in range(len(lista_prod_x)):
        file.write(str(lista_prod_yplot[i])+ ": "+ str(lista_prod_x[i]) + "\n")

    file.write("--------Production in units---------- \n")
    
    for i in range(len(lista_prod_x)):
        file.write(str(lista_prod_yplot[i])+ ": "+ str(lista_prod_x[i] * lista_prod_rendimiento_efectivo[i]) + "\n") # since production time was divided by its perfomance I had to multiply it **2
        
    
# Setting graph attribute and plotting
gnt.grid(True)
plt.savefig("gantt.png",dpi=380)




