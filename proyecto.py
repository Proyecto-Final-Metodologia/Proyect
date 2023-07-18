#declaracion de librerias
import time
import csv
from grovepi import *  
import math
from grove_rgb_lcd import *
import datetime
from math import isnan

#declaramos donde estan conectados todos los sensores
light_sensor = 1
potentiometer = 2
dht_sensor_port = 7
dht_sensor_type = 0
pinMode(light_sensor,"INPUT")

#while principal        
while True:
    try:
        
        #guardamos en variables los datos tomados por los sensores          
        [temp,hum] = dht(dht_sensor_port,dht_sensor_type)       
        sl= analogRead(light_sensor)
        poten = analogRead(potentiometer)
        fechaActual = datetime.datetime.now()
        fechaActual2 = datetime.datetime.strftime(fechaActual, '%d/%m/%Y %H:%M:%S')

        #condicionales dependientes de los datos del potenciometro, para configurar el tiempo
        #muestreo
        if 0 <= poten <= 205 :
        
            t = str(temp)
            h = str(hum)
            slm = str(sl)
        
            print("Fecha: " + fechaActual2 + "temp =", temp, "C\thumidity =", hum,"%", "lum =", sl)
            setText_norefresh("T:" + t + "C" + " TM:1s" + "   H:" + h + "%" + " lum:" + slm)
            
            time.sleep(1)
        
        elif 205 < poten <= 410 :   
        
            t = str(temp)
            h = str(hum)
            slm = str(sl)
        
            print("Fecha: " + fechaActual2 + "temp =", temp, "C\thumidity =", hum,"%", "lum =", sl)
            setText_norefresh("T:" + t + "C" + " TM:2s" + "   H:" + h + "%" + " lum:" + slm)
            time.sleep(2)
        
        elif 410 < poten <= 615 :
        
            t = str(temp)
            h = str(hum)
            slm = str(sl)
        
            print("Fecha: " + fechaActual2 + "temp =", temp, "C\thumidity =", hum,"%", "lum =", sl)
            setText_norefresh("T:" + t + "C" + " TM:3s" + "   H:" + h + "%" + " lum:" + slm)
            time.sleep(3)
        
        elif 615 < poten <= 820 :
        
            t = str(temp)
            h = str(hum)
            slm = str(sl)
        
            print("Fecha: " + fechaActual2 + "temp =", temp, "C\thumidity =", hum,"%", "lum =", sl )
            setText_norefresh("T:" + t + "C" + " TM:4s" + "   H:" + h + "%" + " lum:" + slm)           
            time.sleep(4)
        
        elif 820 < poten <= 1023 :
        
            t = str(temp)
            h = str(hum)
            slm = str(sl)
        
            print("Fecha: " + fechaActual2 + "temp =", temp, "C\thumidity =", hum,"%", "lum =", sl)
            setText_norefresh("T:" + t + "C" + " TM:5s" + "   H:" + h + "%" + " lum:" + slm)            
            time.sleep(5)
        
        
        
        else:
            setText_norefresh("error")

    except IOError:
       print("Error")