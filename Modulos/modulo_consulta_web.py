#Modulo para el consumo de la API
import requests

def consultar_global():
    print("Casos COVID-19 totales para todos los paises")
    #Solicitud con GET de los casos totales de todos los paises
    url = "https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)

    #Validad respuesta
    if response.status_code == 200:
        print("La solicitud fue exitosa!")
    else:
        print("Hubo un problema con la solicitud: Código de estado", response.status_code)
    
    #recolectar los datos en un json
    data = response.json() 

    print(type(data))



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

    if opcion_web == "1": #Consultar casos para país en especifico
        consultar_global()
    elif opcion_web == "2":
        consultar_pais()     
    else:
        pass
