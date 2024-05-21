#Modulos
from math import e
from os import write #
import sys 
sys.path.append('Modulos') #Agrega los directorios de los modulos al PATH de python
import pandas as pd #
#import numpy as pd
import datetime #modulo para mostrar la fecha y hora
import modulo_consulta_web as mcw
import modulo_consulta_registros as mcr
#import modulo_estadisticas as mstats
#import modulo_graficas as mplots
#Variables globales


# Mostrar menu prinicipal
def mostrar_menu_principal():
    """
    Muestra las opciones del menú principal.
    """ 
    print("\n--- Menú Principal ---")
    print("1. Consultar casos del COVID-19")
    print("2. Consultar registros")
    print("3. Estadísticas")
    print("4. Gráficas")
    print("5. Eliminar registros")
    print("6. Salir del programa")

def menu_principal():
    """
    Invoca las opciones del menu principal que el usuario elije.
    """ 
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == '1': #consultar casos
            submenu_consulta_web()
        elif opcion == '2': #consultar registros
            submenu_consulta_registros()
            pass
        elif opcion == '3': #estadisticas
            pass
        elif opcion == '4': #graficas
            pass
        elif opcion == '5':#borrar datos
            pass
        elif opcion == '6': #Salir del programa
            print("Has salido del programa.")
            break
        else: 
            print("Opción no válida. Elije una opción del 1 al 6.")


# Opciones del menu principal---

def mostrar_submenu(names_list:list):
    """ Muestra las subopciones para cada opcion del menú principal
    """
    print("\n--- Submenú {} ---\n".format(names_list[0]["submenu_name"]))
    print("Selecciona una opción a consultar")
    
    #Muestra las opciones para cada submenú
    for opcion in range(1,len(names_list)):
        print("{}. {}".format(opcion,names_list[opcion]))
    print("R. Regresar al Menú Principal")
# Consultas a la API
def submenu_consulta_web():
    """Invoca las opciones que se pueden consultar ala API"""
    while True:
        #Se manda la lista de los nombres de las subopciones del menu
        subopciones_names= [{"submenu_name":"Consulta Web"},
                            "Casos totales de COVID-19 para pais en específico",
                            "Casos historicos totales de COVID-19 para pais en especifico",
                            "Casos totales de COVID-19 para todos los paises",
                            "Casos globales acumulados historicos de COVID-19",
                            "Dosis de vacunas administradas para pais en especifico",
                            ]
        mostrar_submenu(subopciones_names) 
        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            print('\n')
            print(f'--------{subopciones_names[1]}--------')
            pais_totales = input('Selecciona un pais a buscar, iso2, iso3, o country ID code: ')
            data_totales = mcw.consultar_totales_pais(pais_totales) # 'dict' data de la api
            #se muestra la fecha y hora de la consulta
            current_datetime = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-6))) #GMT-6
            current_time = current_datetime.strftime("%H_%M_%S")
            current_date = current_datetime.strftime("%d_%m_%Y")
            print('\n')
            #Se cambian los nombres y eliminan los datos innecesarios del JSON recibido 
            data_totales = {
                "1":["pais",data_totales["country"]],
                "2":["poblacion",data_totales["population"]],
                "3":["casos totales",data_totales["cases"]],
                "4":["casos de hoy",data_totales["todayCases"]],
                "5":["muertes totales",data_totales["deaths"]],
                "6":["muertes de hoy",data_totales["todayDeaths"]],
                "7":["casos recuperados",data_totales["recovered"]],
                "8":["casos recuperados hoy", data_totales["todayRecovered"]],
                "9":["casos activos", data_totales["active"]],
                "10":["casos criticos", data_totales["critical"]],
                "11":["pruebas totales", data_totales["tests"]],
                "12":["pruebas por millon", data_totales["testsPerOneMillion"]],
                "13":["casos por millon", data_totales["casesPerOneMillion"]],
                "14":["muertes por millon", data_totales["deathsPerOneMillion"]]
            }   
            #Se construye un DataFrame con los datos recibidos para mostrar la info
            df_totales = pd.DataFrame.from_dict(data_totales, orient = 'Index', columns= ["Nombre", "Valor"])
            df_totales.index.name = None
            print(f'Casos totales de COVID-19 en {pais_totales} ({data_totales['1'][1]})')
            print('-------------------------------------')
            print(df_totales)
            print('-------------------------------------')
            print('(Datos de COVID-19 procedentes de Worldometers, actualizados cada 10 minutos)') 
            
            print('\nDesea guardar el registro de la consulta anterior?')
            print('1. Si')
            print('2. No. Regresar al menu anterior')
            respuesta = input('Seleccionar opcion: ')
            while True:
                if respuesta == '1':
                    #Escritura del archivo con el formato reporte_fecha_hora.txt
                    f = open(f'Reportes de consulta API/reporte_{current_date}_{current_time}.txt', mode = "w")
                    f.write(f'{data_totales}')
                    f.close()
                    
                    ruta_data_totales = f'reporte_{current_date}_{current_time}.txt'
                    #Guardar la ruta en el archivo de rutas
                    f = open('Reportes de consulta API/rutas_registros_totales_pais.txt', mode = 'a')
                    f.write(f'{ruta_data_totales}\n')
                    f.close()
                    #rutas["rutas_txt"].append(ruta_data_totales)
                    print('La consulta anterior se ha guardado correctamente...')
                    break
                elif respuesta == '2':
                    break
                else:
                    print('Ingresa una opción valida.\n')
            
        elif opcion == '2':
            print('\n')
            print(f'--------{subopciones_names[2]}--------')
            pais_historicos = input('Selecciona un pais a buscar, iso2, iso3, o country ID code: ')
            data_historicos = mcw.consultar_historicos(pais_historicos) # 'dict'
            print('\n')
            #Se guardan los datos de interes en un dataframe
            df_historicos = pd.DataFrame(data_historicos['timeline'])
            
            print(f'Casos historicos totales de COVID-19 en {pais_historicos} ({data_historicos['country']})')
            print('-------------------------------------')
            print(df_historicos)
            print('-------------------------------------')
            print('(Datos de COVID-19 procedentes de la Universidad Johns Hopkins, actualizados cada 10 minutos)')  
            
            
            
            f = open('Reportes de Consulta API/prueba.txt', mode = "w")
            f.write(f'{data_historicos['country']}\n')
            f.write(f'{data_historicos['timeline']}')
            f.close()
            print('La consulta se ha guardado...')
            
        elif opcion == '3':
            print('\n')
            print(f'----------------------------------{subopciones_names[3]}--------------------------------')
            data_globales = mcw.consultar_globales() #list
            print('\n')
            df_globales = pd.DataFrame(data_globales) # 'DataFrame'
            #Se eliminan las columnas que no se necesitan del dataframe
            df_globales.drop(labels =["updated", "countryInfo", "testsPerOneMillion", "oneCasePerPeople", "oneDeathPerPeople",
                                          "oneTestPerPeople", "activePerOneMillion", "recoveredPerOneMillion", "criticalPerOneMillion"],
                                 axis = 1, inplace = True )

            #Cambiamos los nombres de las columnas e imprimimos el dataframe
            df_globales.columns = ["País", "Casos", "CasosDeHoy", "Muertes", "MuertesDeHoy", "Recuperados","RecuperadosDeHoy", "Activos",
                                       "Críticos", "CasosPorMillon", "MuertesPorMillon","Pruebas", "Población", "Continente"]
            
            print('-'*113)
            print(df_globales)
            print('-'*113)
            print('(Datos de COVID-19 procedentes de Worldometers, actualizados cada 10 minutos)')  
            
        elif opcion == '4':
            print('\n')
            print(f'--------{subopciones_names[4]}--------')
            num_dias = input('Ingresa el numero de días a mostrar ("all" para mostrar todos los dias): ')
            data_globales_historicos = mcw.consultar_globales_historicos(num_dias)
            print('\n')
            
            df_globales_historicos = pd.DataFrame(data_globales_historicos)
            print('Casos globales acumulados historicos de COVID-19')
            print('-------------------------------------')
            print(df_globales_historicos)
            print('-------------------------------------')
            print('(Datos de COVID-19 procedentes de la Universidad Johns Hopkins, actualizados cada 10 minutos)')  
            
        elif opcion == '5':
            print('\n')
            print(f'--------{subopciones_names[5]}--------')
            pais_vacunas = input('Selecciona un pais a buscar, iso2, iso3, o country ID code: ')
            data_vacunas = mcw.consultar_vacunas(pais_vacunas)
            print('\n')
            df_vacunas = pd.DataFrame.from_dict(data_vacunas['timeline'], orient = 'index', columns= ['dosis administradas'])
            print(f'Dosis de vacunas administradas en {pais_vacunas} ({data_vacunas['country']})')
            
            print('-------------------------------------')
            print(df_vacunas)
            print('-------------------------------------')
            print('Dosis de vacuna COVID-19 administradas para paises que han notificado el despliegue de vacunacion.')
            print('Fuente de https://covid.ourworldindata.org/') 
            
        elif opcion == 'R':
            break
             
        else:
            print("Opción no valida. Por favor, elija una opción del 1 al 5.")
            
#submenú para consultar los registros hechos de la función .submenu_consulta_web()
def submenu_consulta_registros():
    """
    Muestra y busca las consultas que se han realizado y guardado de la API.
    """
    while True:
        subopciones_names= [{"submenu_name":"Consulta sin internet"},
                                "Registros Casos totales de COVID-19 para pais en específico",
                                "Registros Casos historicos totales de COVID-19 para pais en especifico",
                                "Registros Casos totales de COVID-19 para todos los paises",
                                "Registros Casos globales acumulados historicos de COVID-19",
                                "Registros Dosis de vacunas administradas para pais en especifico",
                                ]
        
        
        mostrar_submenu(subopciones_names) 
        opcion = input('Seleccione una opción: ')
    
        if opcion == '1': #Registros Casos totales de COVID-19 para pais en especifico
            print('\n')
            print(f'--------{subopciones_names[1]}--------')
            
            while True:
                print('-------------------')
                print('1. Buscar registro ')
                print('R. Regresa al menu anterior')
                eleccion = input('Selecciona una opcion: ')
                if eleccion == '1':
                    #Mostramos todas las rutas de las consultas disponibles
                    print('\nReportes disponibles: ')
                    with open('Reportes de consulta API/rutas_registros_totales_pais.txt') as f:
                        for ruta in f:
                            print(ruta)
                    respuesta = input('Ingresa el nombre del registro (formato reporte_fecha_hora) a buscar: ')
                    try:
                        with open(f'Reportes de consulta API/{respuesta}') as f:
                            print('\nRegistro encontrado:\n')
                            print(f.read())
                            
                    except FileNotFoundError:
                        print('No se ha encontrado archivo con ese nombre...\n')
                    except:  # noqa: E722
                        print('Ha ocurrido un error. Intentalo de nuevo\n')
                elif eleccion == 'R':
                    break
                else:
                    print('Elije una opcion valida.\n')  
        elif opcion == '2': #"Registros Casos historicos totales de COVID-19 para pais en especifico"
            pass
        elif opcion == '3': #"Registros Casos totales de COVID-19 para todos los paises"
            pass
        elif opcion == '4': #"Registros Casos globales acumulados historicos de COVID-19"
            pass
        elif opcion == '5': #"Registros Dosis de vacunas administradas para pais en especifico"
            pass
        elif opcion == 'R': #Regresar
            break
        else:
            print('Ingresa una opcion valida')
        
#submenú para consultar las estadísticas de las consultas a la API
def submenu_estadisticas():
    pass
    """
    while True:
        subopciones_names = [] #Agregar nombres de las opciones que tendrá el submenu
        mostrar_submenu_helper(subopciones_names) 
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            #print("Ha seleccionado {}".format(subopciones_names[1]))
            pass
        elif opcion == '2':
            #print("Ha seleccionado {}".format(subopciones_names[2]))
            pass
        elif opcion == '3':
            #print("Ha seleccionado {}".format(subopciones_names[3]))
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 3.")
    """
#submenú para consultar las graficas de las consultas a la API
def submenu_graficas():
    pass
    """
    while True:
        subopciones_names = [] #Agregar nombres de las opciones que tendrá el submenu
        mostrar_submenu_helper(subopciones_names) 
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            #print("Ha seleccionado {}".format(subopciones_names[1]))
            pass
        elif opcion == '2':
            #print("Ha seleccionado {}".format(subopciones_names[2]))
            pass
        elif opcion == '3':
            #print("Ha seleccionado {}".format(subopciones_names[3]))
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 3.")
    """

def submenu_borrar_registros():
    pass

#iniciar el programa
if __name__ == "__main__":
    menu_principal() 

