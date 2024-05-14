#Modulos
import sys
sys.path.append('Modulos') #Agrega los directorios de los modulos al PATH de python
import pandas as pd
import modulo_consulta_web as mcw
#import modulo_consulta_registros as mcr
#import modulo_estadisticas as mstats
#import modulo_graficas as mplots


#MENU PRINCIPAL
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
            pass
            #submenu_opcion2()
        elif opcion == '3': #estadisticas
            pass
            #submenu_opcion3()
        elif opcion == '4': #graficas
            pass
        elif opcion == '5':#borrar datos
            pass
        elif opcion == '6': #Salir del programa
            print("Has salido del programa.")
            break
        else: 
            print("Opción no válida. Elije una opción del 1 al 6.")

#OPCIONES DEL MENU PRINCIPAL
def mostrar_submenu(names_list):
    """ Muestra las subopciones para cada opcion del menú principal
    """
    print("\n--- Submenú {} ---\n".format(names_list[0]["submenu_name"]))
    print("Selecciona una opción a consultar")
    
    #Muestra las opciones para cada submenú
    for opcion in range(1,len(names_list)):
        print("{}. {}".format(opcion,names_list[opcion]))
    print("R. Regresar al Menú Principal")

def submenu_consulta_web():
    """Invoca las opciones"""
    while True:
        #Se manda la lista de los nombres de las subopciones del menu
        subopciones_names= [{"submenu_name":"Consulta Web"},
                            "Casos totales de COVID-19 en México",
                            "Casos históricos totales de COVID-19 en Mexico",
                            "Casos totales de COVID-19 para todos los paises",
                            "Casos globales históricos COVID-19",
                            "Dosis de vacunas administradas en México",
                            ]
        mostrar_submenu(subopciones_names) 
        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            country = input('Pais a buscar')
            
            data_totales = mcw.consultar_totales_paises(country) # "dict" data de la api
            #Se cambian los nombres y eliminan los datos innecesarios del JSON recibido 
            data_totales.pop("updated") 
            data_totales = {
                "1":["pais",data_totales["country"]],
                "2":["poblacion",data_totales["population"]],
                "3":["casos totales",data_totales["cases"]],
                "4":["casos de hoy",data_totales["todayCases"]],
                "5":["muertes totales",data_totales["deaths"]],
                "6":["muertes de hoy",data_totales["todayDeaths"]],
                "7":["casos recuperados",data_totales["recovered"]],
                "8":["casos recuperados_hoy", data_totales["todayRecovered"]],
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
            print('--------------------------------------')
            print(df_totales)
            print('--------------------------------------')
            print('\n(Datos de COVID-19 procedentes de Worldometers, actualizados cada 10 minutos)')  
                    
        elif opcion == '2':
            data_historicos_mx = mcw.consultar_historicos_mx()
            #Se guardan los datos recibidos en un dataframe
            print(data_historicos_mx)
            
            
            
        elif opcion == '3':
            data_globales = mcw.consultar_globales() #list
            
            df_globales = pd.DataFrame(data_globales) # "DataFrame"
            #Se eliminan las columnas que no se necesitan del dataframe
            df_globales.drop(labels =["updated", "countryInfo", "testsPerOneMillion", "oneCasePerPeople", "oneDeathPerPeople",
                                          "oneTestPerPeople", "activePerOneMillion", "recoveredPerOneMillion", "criticalPerOneMillion"],
                                 axis = 1, inplace = True )

            #Cambiamos los nombres de las columnas e imprimimos el dataframe
            df_globales.columns = ["País", "Casos", "CasosDeHoy", "Muertes", "MuertesDeHoy", "Recuperados","RecuperadosDeHoy", "Activos",
                                       "Críticos", "CasosPorMillon", "MuertesPorMillon","Pruebas", "Población", "Continente"]
            print(df_globales)
            
            
        elif opcion == '4':
            
            data_globales_historicos = mcw.consultar_globales_historicos()
            print(data_globales_historicos)
            print(type(data_globales_historicos))
            
        elif opcion == '5':
            data_vacunas = mcw.consultar_vacunas()
            print(data_vacunas)
            print(type(data_vacunas))
            
        elif opcion == 'R':
            break
             
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 5.")
            
#submenú para consultar los registros hechos de la función .submenu_consulta_web()
def submenu_consulta_registros():
    pass
    """
    Pendiente
    """
#submenú para consultar las estadísticas
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
#submenú para consultar las graficas
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
##Metodo para borrar todos los registros
def submenu_borrar_registros():
    pass

if __name__ == "__main__":
    menu_principal() #iniciar el programa

