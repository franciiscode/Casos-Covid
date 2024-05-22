#Modulos externos
import os #manejar los archivos
from sys import path #
path.append('Modulos') #Agrega los directorios de los modulos al PATH de python
import pandas as pd #DataFrames
from PIL import Image #Mostrar las gráficas
import datetime #modulo para mostrar la fecha (d-m-a) y hora (h-m-s) 
#import numpy as np
#Modulos propios
import modulo_consulta_web as mcw
import modulo_estadisticas as mstats
import modulo_graficas as mg


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
        elif opcion == '3': #estadisticas
            submenu_estadisticas()
        elif opcion == '4': #graficas
            submenu_graficas()
        elif opcion == '5':#borrar datos
            submenu_borrar_registros()
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
    print("Selecciona una opción")
    
    #Muestra las opciones para cada submenú
    for opcion in range(1,len(names_list)):
        print("{}. {}".format(opcion,names_list[opcion]))
    print("R. Regresar al Menú Principal")
# Consultas a la API
def submenu_consulta_web():
    """Invoca las opciones que se pueden consultar a la API"""
    while True:
        #Se manda la lista de los nombres de las subopciones del menu
        subopciones_names= [{"submenu_name":"Consulta Web"},
                            "Casos totales de COVID-19 para pais en especifico",
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
                "14":["muertes por millon", data_totales["deathsPerOneMillion"]],
                '15':["pruebas por million", data_totales["testsPerOneMillion"]],
                '16':["activos por millon", data_totales["activePerOneMillion"]],
                '17':["recuperados por millon", data_totales["recoveredPerOneMillion"]],
                '18':["Un caso por persona", data_totales["oneCasePerPeople"]],
                '19':["Una muerte por persona", data_totales["oneDeathPerPeople"]],
                '20':["Una prueba por persona", data_totales["oneTestPerPeople"]],
            }     
            #Se construye un DataFrame con los datos recibidos para mostrar la info
            df_totales = pd.DataFrame.from_dict(data_totales, orient = 'Index', columns= ["Nombre", "Valor"])
            df_totales.index.name = None
            
            print(f'Casos totales de COVID-19 en {pais_totales} ({data_totales['1'][1]})')
            print('-------------------------------------')
            print(df_totales.iloc[:14,])
            print('-------------------------------------')
            print('(Datos de COVID-19 procedentes de Worldometers, actualizados cada 10 minutos)') 
            #Enviar variable a menu de graficas
            #graficas['totales_pais'].append(df_totales)
  
            #Guardar el archivo
            while True:
                print('\nDesea guardar el registro de la consulta anterior?')
                print('1. Si')
                print('2. No.')
                respuesta = input('Seleccionar opcion: ')
                if respuesta == '1':
                    #Escritura del archivo con el formato reporte_fecha_hora.txt
                    f = open(f'Reportes de consulta API/reportes_totales_pais/reporte_{current_date}_{current_time}.txt', mode = "w")
                    f.write(f'{data_totales}')
                    f.close()
                    
                    ruta_data_totales = f'reporte_{current_date}_{current_time}.txt'
                    #Guardar la ruta en el archivo de rutas
                    f = open('Reportes de consulta API/rutas_registros_totales_pais.txt', mode = 'a')
                    f.write(f'{ruta_data_totales}\n')
                    f.close()
                    print('La consulta anterior se ha guardado correctamente')
                    print(f'con el nombre: reporte_{current_date}_{current_time}.txt')
                    break
                elif respuesta == '2': #Salir
                    break
                else:
                    print('Ingresa una opción valida.\n')
            while True:
                print('\nDesea guardar una gráfica para la consulta anterior?: ')
                print('1. Si')
                print('2. No. Regresar al menu anterior')
                generar = input('')
                if generar == '1':
                    mg.graficar_totales_pais(df_totales).savefig(f'Graficas/histograma_{current_date}_{current_time}.png')
                    
                    print(f'\nLa grafica se ha guardado como histograma_{current_date}_{current_time}.png')
                    print(f'Y su ubicación es: Graficas/histograma_{current_date}_{current_time}.png ')
                    print('\nLa(s) grafica(s) se puede(n) buscar en el menu Graficas')
                    break
                elif generar == '2':
                    break
                else:
                    print('Ingresa una opcion valida\n')
            
            #Guardar el dataframe de la consulta en un archivo excel
            # Carpeta específica del espacio de trabajo
             # Crear la carpeta si no existe
        
            ruta_carpeta = 'Reportes datos numericos/datos_totales_pais'
            #Si no existe la ruta, la crea
            if not os.path.exists(ruta_carpeta):
                os.makedirs(ruta_carpeta)
            
            nombre_archivo_xlsx = f'consulta_{current_date}_{current_time}.xlsx'
            #Verificar que el nombre del archivo tenga la extension correcta
            if not nombre_archivo_xlsx.endswith('.xlsx'):
                print("Error: El archivo debe tener la extensión '.xlsx'.")
                return
    
            mstats.crear_archivo_excel(dataframe = df_totales,ruta_carpeta=ruta_carpeta, nombre_archivo = nombre_archivo_xlsx)
           
            
        elif opcion == '2':
            print('\n')
            print(f'--------{subopciones_names[2]}--------')
            pais_historicos = input('Selecciona un pais a buscar, iso2, iso3, o country ID code: ')
            data_historicos = mcw.consultar_historicos(pais_historicos) # 'dict'
            current_datetime = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-6))) #GMT-6
            current_time = current_datetime.strftime("%H_%M_%S")
            current_date = current_datetime.strftime("%d_%m_%Y")
            print('\n')
            #Se guardan los datos de interes en un dataframe
            df_historicos = pd.DataFrame(data_historicos['timeline'])
            
            print(f'Casos historicos totales de COVID-19 en {pais_historicos} ({data_historicos['country']})')
            print('-------------------------------------')
            print(df_historicos)
            print('-------------------------------------')
            print('(Datos de COVID-19 procedentes de la Universidad Johns Hopkins, actualizados cada 10 minutos)')  
            
            while True:
                print('\nDesea guardar el registro de la consulta anterior?')
                print('1. Si')
                print('2. No. Regresar al menu anterior')
                respuesta = input('Seleccionar opcion: ')
                if respuesta == '1':
                    #Escritura del archivo con el formato reporte_fecha_hora.txt
                    try : 
                        f =  open(f'Reportes de consulta API/reportes_historicos_pais/reporte_{current_date}_{current_time}.txt', mode = "w")
                        f.write(f'{data_historicos}\n')
                        f.close()
                        
                        ruta_data_historicos = f'reporte_{current_date}_{current_time}.txt'
                        #Guardar la ruta en el archivo de rutas
                        with open('Reportes de consulta API/rutas_registros_historicos_pais.txt', mode = 'a') as f:
                            f.write(f'{ruta_data_historicos}\n')
                        print('La consulta anterior se ha guardado correctamente') 
                        print(f'con el nombre: reporte_{current_date}_{current_time}.txt')
                        break 
                    except:  # noqa: E722
                        print('Ha ocurrido un error. Intentalo de nuevo\n') 
                        break   
                    #Preguntar si guardar info
                    
                elif respuesta == '2':
                    break
                else:
                    print('Ingresa una opción valida.\n')
            while True:
                print('\nDesea generar y guardar gráfica para la consulta anterior?: ')
                print('1. Si')
                print('2. No. Regresar al menu anterior')
                generar = input('')
                if generar == '1':
                    mg.graficar_historicos_pais(df_historicos, current_date,current_time)
                    
                    print(f'\nLa grafica se ha guardado como casosVSrecuperadosVSmuertes_{current_date}_{current_time}.png')
                    
                    print('Ubicacion:\n')
                    print(f'Graficas/casosVSrecuperadosVSmuertes_{current_date}_{current_time}.png')
                    print('\nLa(s) grafica(s) se puede(n) buscar en el menu Graficas')
                    break
                elif generar == '2':
                    break
                else:
                    print('Ingresa una opcion valida\n')           
            
        elif opcion == '3':
            print('\n')
            print(f'----------------------------------{subopciones_names[3]}--------------------------------')
            data_globales = mcw.consultar_globales() #list
            current_datetime = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-6))) #GMT-6
            current_time = current_datetime.strftime("%H_%M_%S")
            current_date = current_datetime.strftime("%d_%m_%Y")
            
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
            
            while True:
                print('\nDesea guardar el registro de la consulta anterior?')
                print('1. Si')
                print('2. No. Regresar al menu anterior')
                respuesta = input('Seleccionar opcion: ')
                if respuesta == '1':
                    #Escritura del archivo con el formato reporte_fecha_hora.txt
                    try : 
                        f =  open(f'Reportes de consulta API/reportes_globales/reporte_{current_date}_{current_time}.txt', mode = "w")
                        f.write(f'{data_globales}\n')
                        f.close()
                        
                        ruta_data_globales = f'reporte_{current_date}_{current_time}.txt'
                        #Guardar la ruta en el archivo de rutas
                        with open('Reportes de consulta API/rutas_registros_globales.txt', mode = 'a') as f:
                            f.write(f'{ruta_data_globales}\n')
                        print('La consulta anterior se ha guardado correctamente') 
                        print(f'con el nombre: reporte_{current_date}_{current_time}.txt')
                        break   
                    except:  # noqa: E722
                        print('Ha ocurrido un error. Intentalo de nuevo\n') 
                        break 
                elif respuesta == '2':
                    break
                else:
                    print('Ingresa una opción valida.\n')
            while True:
                print('\nDesea generar y guardar algunas gráficas para la consulta anterior?: ')
                print('1. Si')
                print('2. No. Regresar al menu anterior')
                generar = input('')
                if generar == '1':
                    mg.graficar_globales(df_globales, current_date,current_time)
                    
                    print(f'\nLas graficas se han guardado como:\ncasos_activos_{current_date}_{current_time}.png')
                    print(f'continenteVSmuertes{current_date}_{current_time}.png')
                    print(f'continenteVScasos{current_date}_{current_time}.png')
                    
                    print('\nUbicaciones respectivas:')
                    print(f'Graficas/casos_activos_{current_date}_{current_time}.png')
                    print(f'Graficas/continenteVSmuertes{current_date}_{current_time}.png')
                    print(f'Graficas/continenteVScasos{current_date}_{current_time}.png')
                    
                    print('\nLa(s) grafica(s) se puede(n) observar en el menu Graficas')
                    break
                elif generar == '2':
                    break
                else:
                    print('Ingresa una opcion valida\n')
        elif opcion == '4':
            print('\n')
            print(f'--------{subopciones_names[4]}--------')
            num_dias = input('Ingresa el numero de días a mostrar ("all" para mostrar todos los dias): ')
            data_globales_historicos = mcw.consultar_globales_historicos(num_dias)
            current_datetime = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-6))) #GMT-6
            current_time = current_datetime.strftime("%H_%M_%S")
            current_date = current_datetime.strftime("%d_%m_%Y")
            print('\n')
            
            df_globales_historicos = pd.DataFrame(data_globales_historicos)
            print('Casos globales acumulados historicos de COVID-19')
            print('-------------------------------------')
            print(df_globales_historicos)
            print('-------------------------------------')
            print('(Datos de COVID-19 procedentes de la Universidad Johns Hopkins, actualizados cada 10 minutos)')  
            
            while True:
                print('\nDesea guardar el registro de la consulta anterior?')
                print('1. Si')
                print('2. No. Regresar al menu anterior')
                respuesta = input('Seleccionar opcion: ')
                if respuesta == '1':
                    #Escritura del archivo con el formato reporte_fecha_hora.txt
                    try : 
                        f =  open(f'Reportes de consulta API/reportes_globales_historicos/reporte_{current_date}_{current_time}.txt', mode = "w")
                        f.write(f'{data_globales_historicos}\n')
                        f.close()
                        
                        ruta_data_globales_historicos = f'reporte_{current_date}_{current_time}.txt'
                        #Guardar la ruta en el archivo de rutas
                        with open('Reportes de consulta API/rutas_registros_globales_historicos.txt', mode = 'a') as f:
                            f.write(f'{ruta_data_globales_historicos}\n')
                        print('La consulta anterior se ha guardado correctamente...') 
                        print(f'con el nombre: reporte_{current_date}_{current_time}.txt')
                        break
                    except:  # noqa: E722
                        print('Ha ocurrido un error. Intentalo de nuevo\n') 
                        break 
                elif respuesta == '2':
                    break
                else:
                    print('Ingresa una opción valida.\n')
            while True:
                print('\nDesea generar y guardar grafica para la consulta anterior?: ')
                print('1. Si')
                print('2. No. Regresar al menu anterior')
                generar = input('')
                if generar == '1':
                    mg.graficar_globales_historicos(df_globales_historicos, current_date,current_time)
                    
                    print('\nLa grafica se ha guardado como:')
                    print(f'casosVSrecuperadosVSmuertes_hist_{current_date}_{current_time}.png')
                    
                    print('\nUbicacion:')
                    print(f'Graficas/casosVSrecuperadosVSmuertes_hist_{current_date}_{current_time}.png')
                    print('\nLa(s) grafica(s) se puede(n) observar en el menu Graficas')
                    break
                elif generar == '2':
                    break
                else:
                    print('Ingresa una opcion valida\n')
        elif opcion == '5':
            print('\n')
            print(f'--------{subopciones_names[5]}--------')
            pais_vacunas = input('Selecciona un pais a buscar, iso2, iso3, o country ID code: ')
            data_vacunas = mcw.consultar_vacunas(pais_vacunas)
            current_datetime = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-6))) #GMT-6
            current_time = current_datetime.strftime("%H_%M_%S")
            current_date = current_datetime.strftime("%d_%m_%Y")
            print('\n')
            df_vacunas = pd.DataFrame.from_dict(data_vacunas['timeline'], orient = 'index', columns= ['dosis administradas'])
            print(f'Dosis de vacunas administradas en {pais_vacunas} ({data_vacunas['country']})')
            
            print('-------------------------------------')
            print(df_vacunas)
            print('-------------------------------------')
            print('Dosis de vacuna COVID-19 administradas para paises que han notificado el despliegue de vacunacion.')
            print('Fuente de https://covid.ourworldindata.org/') 
            
            while True:
                print('\nDesea guardar el registro de la consulta anterior?')
                print('1. Si')
                print('2. No. Regresar al menu anterior')
                respuesta = input('Seleccionar opcion: ')
                if respuesta == '1':
                    #Escritura del archivo con el formato reporte_fecha_hora.txt
                    try : 
                        f =  open(f'Reportes de consulta API/reportes_vacunas/reporte_{current_date}_{current_time}.txt', mode = "w")
                        f.write(f'{data_vacunas}\n')
                        f.close()
                        
                        ruta_data_vacunas = f'reporte_{current_date}_{current_time}.txt'
                        #Guardar la ruta en el archivo de rutas
                        with open('Reportes de consulta API/rutas_registros_vacunas.txt', mode = 'a') as f:
                            f.write(f'{ruta_data_vacunas}\n')
                        print('La consulta anterior se ha guardado correctamente...') 
                        break
                    except:  # noqa: E722
                        print('Ha ocurrido un error. Intentalo de nuevo\n') 
                        break 
                elif respuesta == '2':
                    break
                else:
                    print('Ingresa una opción valida.\n')
            while True:
                print('\nDesea generar y guardar grafica para la consulta anterior?: ')
                print('1. Si')
                print('2. No. Regresar al menu anterior')
                generar = input('')
                if generar == '1':
                    mg.graficar_vacunas(df_vacunas, current_date,current_time)
                    
                    print('\nLa grafica se ha guardado como:')
                    print(f'dosis_administradas_{current_date}_{current_time}.png')
                    
                    print('\nUbicacion:')
                    print(f'Graficas/dosis_administradas_{current_date}_{current_time}.png')
                    print('\nLa(s) grafica(s) se puede(n) observar en el menu Graficas')
                    break
                elif generar == '2':
                    break
                else:
                    print('Ingresa una opcion valida\n')
        elif opcion == 'R':
            break
             
        else:
            print("Opción no valida. Por favor, elija una opción valida.")
            
#submenú para consultar los registros hechos de la función .submenu_consulta_web()
def submenu_consulta_registros():
    """
    Muestra y busca las consultas que se han realizado y guardado de la API.
    """
    while True:
        subopciones_names= [{"submenu_name":"Consulta sin internet"},
                                "Registros Casos totales de COVID-19 para pais en especifico",
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
                        with open(f'Reportes de consulta API/reportes_totales_pais/{respuesta}') as f:
                            print('\nRegistro encontrado:\n')
                            print(f'Reportes de consulta API/reportes_totales_pais/{respuesta}') #print se imprime la ruta del archivo encontrado
                            
                    except FileNotFoundError:
                        print('No se ha encontrado archivo con ese nombre...\n')
                    except:  # noqa: E722
                        print('Ha ocurrido un error. Intentalo de nuevo\n')
                elif eleccion == 'R':
                    break
                else:
                    print('Elije una opcion valida.\n')  
        elif opcion == '2': #"Registros Casos historicos totales de COVID-19 para pais en especifico"
            print('\n')
            print(f'--------{subopciones_names[2]}--------')
            while True:
                print('-------------------')
                print('1. Buscar registro ')
                print('R. Regresa al menu anterior')
                eleccion = input('Selecciona una opcion: ')
                if eleccion == '1':
                    #Mostramos todas las rutas de las consultas disponibles
                    print('\nReportes disponibles: ')
                    with open('Reportes de consulta API/rutas_registros_historicos_pais.txt') as f:
                        for ruta in f:
                            print(ruta)
                    respuesta = input('Ingresa el nombre del registro (formato reporte_fecha_hora) a buscar: ')
                    try:
                        with open(f'Reportes de consulta API/reportes_historicos_pais/{respuesta}') as f:
                            print('\nRegistro encontrado:\n')
                            print(f'Reportes de consulta API/reportes_historicos_pais/{respuesta}')
                            
                    except FileNotFoundError:
                        print('No se ha encontrado archivo con ese nombre...\n')
                    except:  # noqa: E722
                        print('Ha ocurrido un error. Intentalo de nuevo\n')
                elif eleccion == 'R':
                    break
                else:
                    print('Elije una opcion valida.\n')  
        elif opcion == '3': #"Registros Casos totales de COVID-19 para todos los paises"
            print('\n')
            print(f'--------{subopciones_names[3]}--------')
            
            while True:
                print('-------------------')
                print('1. Buscar registro ')
                print('R. Regresa al menu anterior')
                eleccion = input('Selecciona una opcion: ')
                if eleccion == '1':
                    #Mostramos todas las rutas de las consultas disponibles
                    print('\nReportes disponibles: ')
                    with open('Reportes de consulta API/rutas_registros_globales.txt') as f:
                        for ruta in f:
                            print(ruta)
                    respuesta = input('Ingresa el nombre del registro (formato reporte_fecha_hora) a buscar: ')
                    try:
                        with open(f'Reportes de consulta API/reportes_globales/{respuesta}') as f:
                            print('\nRegistro encontrado:\n')
                            print(f'Reportes de consulta API/reportes_globales/{respuesta}')
                            
                    except FileNotFoundError:
                        print('No se ha encontrado archivo con ese nombre...\n')
                    except:  # noqa: E722
                        print('Ha ocurrido un error. Intentalo de nuevo\n')
                elif eleccion == 'R':
                    break
                else:
                    print('Elije una opcion valida.\n')  
        elif opcion == '4': #"Registros Casos globales acumulados historicos de COVID-19"
            print('\n')
            print(f'--------{subopciones_names[4]}--------')
            
            while True:
                print('-------------------')
                print('1. Buscar registro ')
                print('R. Regresa al menu anterior')
                eleccion = input('Selecciona una opcion: ')
                if eleccion == '1':
                    #Mostramos todas las rutas de las consultas disponibles
                    print('\nReportes disponibles: ')
                    with open('Reportes de consulta API/rutas_registros_globales_historicos.txt') as f:
                        for ruta in f:
                            print(ruta)
                    respuesta = input('Ingresa el nombre del registro (formato reporte_fecha_hora) a buscar: ')
                    try:
                        with open(f'Reportes de consulta API/reportes_globales_historicos/{respuesta}') as f:
                            print('\nRegistro encontrado:\n')
                            print(f'Reportes de consulta API/reportes_globales_historicos/{respuesta}')
                            
                    except FileNotFoundError:
                        print('No se ha encontrado archivo con ese nombre...\n')
                    except:  # noqa: E722
                        print('Ha ocurrido un error. Intentalo de nuevo\n')
                elif eleccion == 'R':
                    break
                else:
                    print('Elije una opcion valida.\n') 
        elif opcion == '5': #"Registros Dosis de vacunas administradas para pais en especifico"
            print('\n')
            print(f'--------{subopciones_names[5]}--------')
            
            while True:
                print('-------------------')
                print('1. Buscar registro ')
                print('R. Regresa al menu anterior')
                eleccion = input('Selecciona una opcion: ')
                if eleccion == '1':
                    #Mostramos todas las rutas de las consultas disponibles
                    print('\nReportes disponibles: ')
                    with open('Reportes de consulta API/rutas_registros_vacunas.txt') as f:
                        for ruta in f:
                            print(ruta)
                    respuesta = input('Ingresa el nombre del registro (formato reporte_fecha_hora) a buscar: ')
                    try:
                        with open(f'Reportes de consulta API/reportes_vacunas/{respuesta}') as f:
                            print('\nRegistro encontrado:\n')
                            print(f'Reportes de consulta API/reportes_vacunas/{respuesta}')
                            
                    except FileNotFoundError:
                        print('No se ha encontrado archivo con ese nombre...\n')
                    except:  # noqa: E722
                        print('Ha ocurrido un error. Intentalo de nuevo\n')
                elif eleccion == 'R':
                    break
                else:
                    print('Elije una opcion valida.\n') 
        elif opcion == 'R': #Regresar
            break
        else:
            print('Ingresa una opcion valida')
        
#submenú para consultar las estadísticas de las consultas a la API
def submenu_estadisticas():
    """ Muestra algunos datos estadísticos"""
    def buscar_y_abrir_excel(ruta_carpeta, nombre_archivo):
    # Crear la ruta completa del archivo
        ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)
        
        # Verificar que el archivo exista y tenga la extensión correcta
        if not os.path.isfile(ruta_completa):
            print(f"Error: El archivo '{nombre_archivo}' no existe en la carpeta '{ruta_carpeta}'.")
            return
        
        if not nombre_archivo.endswith('.xlsx'):
            print("Error: El archivo debe tener la extensión '.xlsx'.")
            return
        
        try:
            # Leer el archivo Excel
            df = pd.read_excel(ruta_completa)
            print(f"El archivo '{ruta_completa}' se ha abierto exitosamente.")
            print("Contenido del archivo:")
            print(df)
        except Exception as e:
            print(f"Ocurrió un error al abrir el archivo Excel: {e}")

    while True:
        subopciones_names= [{"submenu_name":"Estadisticas"},
                                "Estadisticas de Casos totales de COVID-19 para pais en especifico (ultima consulta)",
                                "Estadisticas de Casos historicos totales de COVID-19 para pais en especifico (ultima consulta)",
                                "Estadisticas de Casos totales de COVID-19 para todos los paises (ultima consulta)",
                                "Estadisticas de Casos globales acumulados historicos de COVID-19 (ultima consulta)",
                                "Estadisticas de Dosis de vacunas administradas para pais en especifico (ultima consulta)",
                                ]
        mostrar_submenu(subopciones_names) 
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            print("Ha seleccionado {}".format(subopciones_names[1]))
            
            ruta_carpeta = 'Reportes datos numericos/datos_totales_pais'
            print
            if not os.path.exists(ruta_carpeta):
                print(f"La carpeta '{ruta_carpeta}' no existe.")
                return
            nombre_archivo = input("Introduce el nombre del archivo de Excel a buscar (con extensión .xlsx): ").strip()
            buscar_y_abrir_excel(ruta_carpeta, nombre_archivo)
            
        elif opcion == '2':
            print("Ha seleccionado {}".format(subopciones_names[2]))
            pass
        elif opcion == '3':
            print("Ha seleccionado {}".format(subopciones_names[3]))
            break
        elif opcion == '4':
            print("Ha seleccionado {}".format(subopciones_names[4]))
            break
        elif opcion == '5':
            print("Ha seleccionado {}".format(subopciones_names[5]))
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 3.")
    
#submenú para consultar las graficas de las consultas a la API
def submenu_graficas():
    """
    Muestra la gráficas buscadas por el usuario.
    """
    def mostrar_imagen(ruta_archivo):
        try:
            # Abre la imagen usando Pillow
            with Image.open(ruta_archivo) as img:
                img.show()  # Muestra la imagen
                print(f"Mostrando la imagen '{ruta_archivo}'.")
        except FileNotFoundError:
            print(f"El archivo '{ruta_archivo}' no existe.")
        except PermissionError:
            print(f"Permiso denegado para leer el archivo '{ruta_archivo}'.")
        except Exception as e:
            print(f"Ocurrió un error al intentar leer el archivo '{ruta_archivo}': {e}")
            
    while True:
        print('\n--- Submenú Buscar gráficas ---')
        print('Opciones:')
        print('1. Buscar grafica')
        print('2. Regresar')
        elegir = input('Selecciona una opcion: ')
        
        if elegir == '1':
            carpeta = 'Graficas'
            if not os.path.isdir(carpeta):
                print("La carpeta 'Graficas' no existe.")
                return

            nombre_archivo = input("Introduce el nombre del archivo de la grafica (con extension)\nAsegurate que el archivo se encuentre en la carpeta Graficas: ").strip()
            ruta_archivo = os.path.join(carpeta, nombre_archivo)

            if os.path.isfile(ruta_archivo):
                mostrar_imagen(ruta_archivo)
            else:
                print(f"El archivo '{nombre_archivo}' no se encontró en la carpeta '{carpeta}'.")

           
        elif elegir =='2':
            break
        else:
            print('Elije una opcion valida')
        

def submenu_borrar_registros():
    """ Borra los archivos de los registros guardados por el usuario"""
    print('\n--- Submenú Borrar archivos ---')
    def borrar_archivos_en_carpeta(carpeta, archivos):
        for archivo in archivos:
            ruta_archivo = os.path.join(carpeta, archivo)
            try:
                os.remove(ruta_archivo)
                print(f"Archivo '{ruta_archivo}' borrado exitosamente.")
            except FileNotFoundError:
                print(f"El archivo '{ruta_archivo}' no existe.")
            except PermissionError:
                print(f"Permiso denegado para borrar el archivo '{ruta_archivo}'.")
            except Exception as e:
                print(f"Ocurrió un error al intentar borrar el archivo '{ruta_archivo}': {e}")
    
    def borrar_todos_los_archivos(carpeta):
        try:
            for archivo in os.listdir(carpeta):
                ruta_archivo = os.path.join(carpeta, archivo)
                if os.path.isfile(ruta_archivo):
                    os.remove(ruta_archivo)
                    print(f"Archivo '{ruta_archivo}' borrado exitosamente.")
        except Exception as e:
            print(f"Ocurrió un error al intentar borrar los archivos en '{carpeta}': {e}")
            
    while True:
        print('Opciones:')
        print('1. Borrador de archivos en una carpeta específica')
        print('2. Borrador todos los archivos de una carpeta específica')
        print('R. Regresar ')
        elegir = input('Selecciona una opcion: ')
        
        if elegir == '1':
            carpeta = input("Introduce la ruta de la carpeta: ").strip()
            
            if not os.path.isdir(carpeta):
                print("La carpeta especificada no existe.")
                return
            archivos_a_borrar = input("Introduce los nombres de los archivos a borrar, separados por comas: ").split(',')
            archivos_a_borrar = [archivo.strip() for archivo in archivos_a_borrar]  # Elimina espacios en blanco adicionales

            confirmar = input(f"¿Seguro que quieres borrar estos archivos en '{carpeta}'? {archivos_a_borrar} (s/n): ")
            if confirmar.lower() == 's':
                borrar_archivos_en_carpeta(carpeta, archivos_a_borrar)
            else:
                print("Operación cancelada.")
        elif elegir== '2':
            carpeta = input("Introduce la ruta de la carpeta: ").strip()
            confirmar = input(f"¿Seguro que quieres borrar todos los archivos en '{carpeta}'? (s/n): ")
            if confirmar.lower() == 's':
                borrar_todos_los_archivos(carpeta)
            else:
                print("Operación cancelada.")
        elif elegir== 'R':
            break
        else:
            print('Ingresa una opcion valida')
#iniciar el programa
if __name__ == "__main__":
    menu_principal() 

