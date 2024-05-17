
#Modulos necesarios
import requests #Modulo para consumir la API

"""
import os #limpiar consola
def clear_console():#Método para limpiar la consola
os.system('cls' if os.name == 'nt' else 'clear')
clear_console()
"""
#opciones del menu consulta web

def consultar_totales_pais(pais = 'Mexico'):
    """
    Devuelve la información en un JSON de los casos totales de COVID-19 de algun pais en especifico. Por default
    devuelve los datos para Mexico.
    """
    #Solicitud con GET de los casos
    url = f'https://disease.sh/v3/covid-19/countries/{pais}?strict=false'
    response = requests.get(url)
    if response.status_code == 200:
        print("La solicitud fue exitosa!")
    else:
        print("Hubo un problema con la solicitud: Código de estado", response.status_code)
        
    #Se almacenan los datos json recibidos
    data = response.json() 
    return data
    
def consultar_historicos(pais = 'Mexico'):
    """
    Devuelve la información en un JSON de los datos historicos registrados de COVID-19 para pais 
    en especifico del 22/1/20 al 9/3/23. Por default devuelve la información para Mexico.
    """
    #Solicitud con GET de los casos históricos para pais en espec.
    url = f'https://disease.sh/v3/covid-19/historical/{pais}?lastdays=all'
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
    Devuelve la información en un JSON de los casos totales del COVID-19 
    para todos los paises.
    """
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

def consultar_globales_historicos(num_dias = 'all'):
    """
    Devuelve la información de los casos globales acumulados historicos del 22/1/20
    a 9/3/23.
    """
    #Solicitud con GET de los casos globales historicos
    url = f'https://disease.sh/v3/covid-19/historical/all?lastdays={num_dias}'
    response = requests.get(url)

    #Validar respuesta
    if response.status_code == 200:
        print("La solicitud fue exitosa!")
    else:
        print("Hubo un problema con la solicitud: Código de estado", response.status_code)
    
    #Se almacenan los datos json recibidos
    data = response.json() 
    return data

def consultar_vacunas(pais = 'Mexico'):
    """
    Devuelve la información de las dosis totales de vacunas administradas para pais en especifico
    del 1/12/20 al presente reportadas por el gobierno. Por default devuelve la información para Mexico.
    """
    #Solicitud con GET de las vacunas
    url = f'https://disease.sh/v3/covid-19/vaccine/coverage/countries/{pais}?lastdays=all&fullData=false'
    response = requests.get(url)

    #Validar respuesta
    if response.status_code == 200:
        print("La solicitud fue exitosa!")
    else:
        print("Hubo un problema con la solicitud: Código de estado", response.status_code)
    
    #Se almacenan los datos json recibidos
    data = response.json() 
    return data
 
 

