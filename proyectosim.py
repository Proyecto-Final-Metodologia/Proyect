#declaracion de librerias
import time
import csv
import math
import datetime
from math import isnan
import random

#Declaramos las variables
tem = 0
hum = 0
poten = 0
lum = 0
tiempo_muestreo = 0
fechaActual = ""
fechaActual2 = ""

datos_actualizados = []  # Lista para almacenar los datos actualizados


def variables(tem, hum, poten, lum, tiempo_muestreo, fechaActual2):
    tem = random.randint(1, 50)
    hum = random.randint(1, 100)
    poten = random.randint(0,1023)
    lum = int(random.uniform(100,600))
    tiempo_muestreo = random.randrange(1,5,1)
    fechaActual = datetime.datetime.now()
    fechaActual2 = datetime.datetime.strftime(fechaActual, '%d/%m/%Y %H:%M:%S')#Formato: Día/Mes/Año hora/minuto/segundo
    
    return tem, hum, poten, lum, tiempo_muestreo, fechaActual2
    
def mostrar_LCD(tem, hum, lum, tiempo_muestreo, fechaActual2):
    datos = "Fecha:{}  Temperatura:{}C   Humedad:{}%    Int.Lumínica:{} Lx    Tiempo de muestreo:{}s".format(fechaActual2, tem, hum, lum, tiempo_muestreo)
    datos_actualizados.append(datos)  # Agregar datos a la lista (Se ve raro pero es pa la prubea, con un print(datos) se ve mejor xd)
    print("Datos actualizados:")
    
    #Ciclo para que actualice los datos de la tabla
    for datos in datos_actualizados:
        print(datos_actualizados)
    print()
            
def tiempo(tiempo_muestreo):
    if tiempo_muestreo == 1:
        0 <= poten <= 205
        time.sleep(1)
        return poten
        
    elif tiempo_muestreo == 2 :  
        205 < poten <= 410
        time.sleep(2)
        return poten
        
    elif tiempo_muestreo == 3 :
        410 < poten <= 615
        time.sleep(3)
        return poten
        
    elif tiempo_muestreo == 4 :  
        615 < poten <= 820 
        time.sleep(4)
        return poten

    elif tiempo_muestreo == 5 :  
        820 < poten <= 1023
        time.sleep(5)
        return poten
         
while True:
    # Asignamos los nuevos valores devueltos por la función a las variables externas
    tem, hum, poten, lum, tiempo_muestreo, fechaActual2 = variables(tem, hum, poten, lum, tiempo_muestreo, fechaActual2)
    
    try:
        variables(tem, hum, poten, lum, tiempo_muestreo, fechaActual2)#Imita a los sensores tirando daticos random
        mostrar_LCD(tem, hum, lum, tiempo_muestreo, fechaActual2)#Imprime en pantalla pues
        tiempo(tiempo_muestreo)#Simula el tiempito de muestreo del potenciometro patico
        
  
        

    except IOError:
       print("Error")