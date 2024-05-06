
#Modulos necesarios
import requests #Modulo para consumir la API

#Declaración de métodos
"""
import os #limpiar consola
def clear_console():#Método para limpiar la consola
os.system('cls' if os.name == 'nt' else 'clear')
clear_console()
"""

def consultar_totales_mx():
    """
    Devuelve la información en una lista de los casos totales de COVID-19 en México. 
    """
  
    print("Casos totales del COVID-19 en México")
    #Solicitud con GET de los casos totales para Mexico
    url = "https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)

    #Validad respuesta
    if response.status_code == 200:
        print("La solicitud fue exitosa!")
    else:
        print("Hubo un problema con la solicitud: Código de estado", response.status_code)
    
    #Se almacenan los datos json en una lista y se devuelven 
    data = response.json() 
    return data
    
def consultar_historicos_mx():
    """
    Devuelve la información en una lista de los casos históricos de COVID-19 en México del 22/1/20
    a 9/3/23. 
    """
    print("Casos historicos del COVID-19 para México")
    #Solicitud con GET de los casos históricos para Mexico
    url = "https://disease.sh/v3/covid-19/historical/Mexico?lastdays=all"
    response = requests.get(url)

    #Validad respuesta
    if response.status_code == 200:
        print("La solicitud fue exitosa!")
    else:
        print("Hubo un problema con la solicitud: Código de estado", response.status_code)
    
    #Se almacenan los datos json en una lista y se devuelven 
    data = response.json() 
    return data

def consultar_casos_nl():
    """
    Devuelve la información en una lista de los casos históricos de COVID-19 en México del 22/1/20
    a 9/3/23 para el estado de Nuevo León.
    """
    pass

def consultar_vacunas():
    """
    Devuelve la información en una lista de los casos históricos de COVID-19 en México del 22/1/20
    a "9/3/23"  
    """
    pass
 

