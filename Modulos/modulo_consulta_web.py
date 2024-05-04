
#Modulos necesarios
import requests #Modulo para consumir la API
import pandas as pd #dataframes
import os #limpiar consola

#Declaración de métodos

def clear_console():#Método para limpiar la consola
    os.system('cls' if os.name == 'nt' else 'clear')

def consultar_global():
    """
    Devuelve la información en una lista de los casos totales de COVID-19 en todos los paises. 
    """
    clear_console()
    print("Casos COVID-19 totales para todos los paises")
    #Solicitud con GET de los casos totales de todos los paises
    url = "https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)

    #Validad respuesta
    if response.status_code == 200:
        print("La solicitud fue exitosa!")
    else:
        print("Hubo un problema con la solicitud: Código de estado", response.status_code)
    
    #Recolectar los datos en un json
    data = response.json() 
    return data
    
    


def consultar_pais():
    #print("Casos COVID-19 para un país en específico")
    pass

def consultar_conjunto_paises():
    pass



def iniciar():
    """submenu principal
    """
    #Mostrar submenu principal
    print("\n\nSubmenú consultas web\n")
    print("1- Casos COVID-19 globales\n2- Casos dos\n3- Casos dos\n4- Casos dos\n5- Casos dos\n")
    opcion_web = input("Selecciona una opcion: ")

    if opcion_web == "1": #Consultar casos para todos los países
        data = consultar_global()

        df_data = pd.DataFrame(data) #Guardar datos obtenidos en un dataframe
        print(df_data.head(5))
        
        
    elif opcion_web == "2":
        #consultar_pais()  
        pass    
    elif opcion_web== "3":
        pass
    elif opcion_web=="4":
        pass

