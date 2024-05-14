
#Modulos necesarios
import requests #Modulo para consumir la API

#Declaración de métodos
"""
import os #limpiar consola
def clear_console():#Método para limpiar la consola
os.system('cls' if os.name == 'nt' else 'clear')
clear_console()
"""

def consultar_totales_paises(pais):  # noqa: F821
    """
    Devuelve la información de los casos totales de COVID-19 de algun pais en especifico. 
    """
  
    print("Casos totales del COVID-19 en México")
    #Solicitud con GET de los casos totales para Mexico
    url = f'https://disease.sh/v3/covid-19/countries/{pais}?strict=false'
    response = requests.get(url)
    if response.status_code == 200:
        print("La solicitud fue exitosa!")
    else:
        print("Hubo un problema con la solicitud: Código de estado", response.status_code)
    
    #Se almacenan los datos json recibidos
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

def consultar_globales():
    """
    Devuelve la información de los casos totales para todos los paises.
    """
    print("Casos globales de COVID-19")
    #Solicitud con GET de los casos totales globales
    url = "https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)

    #***Pendiente validar ***
    if response.status_code == 200:
        print("La solicitud fue exitosa!")
    else:
        print("Hubo un problema con la solicitud: Código de estado", response.status_code)

    #Recolectar los datos en un json
    data = response.json()
    return data

def consultar_globales_historicos():
    """
    Devuelve la información de los casos globales acumulados historicos.
    """
    print("Casos globales históricos de COVID-19 en todos los paises")
    #Solicitud con GET de los casos globales historicos
    url = "https://disease.sh/v3/covid-19/historical/all?lastdays=all"
    response = requests.get(url)

    #Validar respuesta
    if response.status_code == 200:
        print("La solicitud fue exitosa!")
    else:
        print("Hubo un problema con la solicitud: Código de estado", response.status_code)
    
    #Se almacenan los datos json recibidos
    data = response.json() 
    return data

def consultar_vacunas():
    """
    Devuelve la información de las dosis totales de vacunas administradas en Mexico de 1/12/20-presente,
    reportadas por el gobierno.
    """
    print("Dosis totales de vacunas administradas en Mexico")
    #Solicitud con GET de las vacunas
    url = "https://disease.sh/v3/covid-19/vaccine/coverage/countries/Mexico?lastdays=all&fullData=false"
    response = requests.get(url)

    #Validar respuesta
    if response.status_code == 200:
        print("La solicitud fue exitosa!")
    else:
        print("Hubo un problema con la solicitud: Código de estado", response.status_code)
    
    #Se almacenan los datos json recibidos
    data = response.json() 
    return data
 
#

