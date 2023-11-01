import requests
import pytpu
tarjeta_personal = {}


while True:
    elegir_que_hacer = int(input("Que desea hacer? 1- Crear datos nuevos, 2- Modificar datos , 3 - Eliminar datos"))
    
    if elegir_que_hacer == 1:
        clave = input("Ingrese el dato: ")
        valor = input("Ingrese el valor: ")
        tarjeta_personal[clave] = valor
        print(tarjeta_personal)
    
    elif elegir_que_hacer == 2:
        clave = input("Ingrese el dato que desea modificar: ")
        valor = input("Ingrese el valor que desea modificar: ")
        tarjeta_personal[clave] = valor
        print(tarjeta_personal)
    
    elif elegir_que_hacer == 3:
            clave = input("Ingrese el dato que desea eliminar: ")
            del tarjeta_personal[clave]
            print(tarjeta_personal)
    else:
        print("La opcion ingresada no es valida")
        break
         

import RPi.GPIO # Libreria para manejo de pines 
import time
#Los pines de conexionGPIO16, GPIO 20, GPIO 21
LED_Amarillo = 16
LED_Rojo = 20
LED_Verde = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup()

