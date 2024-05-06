#Modulos usados
import sys
sys.path.append('Modulos') #Agrega los directorios de los modulos al PATH de python
import pandas as pd
import modulo_consulta_web as mcw
import modulo_consulta_registros as mcr
#import modulo_estadisticas as mstats
#import modulo_graficas as mplots


#MENU PRINCIPAL
def mostrar_menu_principal():
    """
    Método para mostrar las opciones del menú principal.
    """ 
    print("\n--- Menú Principal ---")
    print("1. Consultar casos COVID-19")
    print("2. Consultar registros")
    print("3. Estadísticas")
    print("4. Gráficas")
    print("4. Salir")

def menu_principal():
    
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            submenu_consulta_web()
        elif opcion == '2':
            submenu_opcion2()
        elif opcion == '3':
            submenu_opcion3()
        elif opcion == '4':
            break
        else: #***PENDIENTE VALIDACIÓN***
            print("Opción no válida. Elije una opción del 1 al 4.")

#OPCIONES DEL MENU PRINCIPAL
def mostrar_submenu_helper(names_list):
    """ Muestra las subopciones para cada opcion del menú principal"""
    print("\n--- Submenú {} ---\n".format(names_list[0]["submenu_name"]))
    print("Selecciona una opción a consultar")
    
    #Muestra las opciones para cada submenú
    for opcion in range(1,len(names_list)):
        print("{}. {}".format(opcion,names_list[opcion]))
    print("R. Regresar al Menú Principal")
#data_totales = None #Guarda los datos recibidos del
#data_historicos = None
def submenu_consulta_web():
    while True:
        #Se manda la lista de los nombres de las subopciones del menu
        subopciones_names= [{"submenu_name":"Consulta Web"},
                            "Casos totales de COVID-19 en México",
                            "Casos COVID-19 en Mexico (series temporales)",
                            "Casos totales en Nuevo León",
                            "Dosis de vacunas administradas en México"
                            ]
        mostrar_submenu_helper(subopciones_names) 
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("Ha seleccionado {}".format(subopciones_names[0]["submenu_name"]))
            data_totales = mcw.consultar_totales_mx()
            
            #Guardamos los datos recibidos en un dataframe
            df_totales = pd.DataFrame(data_totales)
            print(df_totales.head(20))
        elif opcion == '2':
            print("Ha seleccionado {}".format(subopciones_names[0]["submenu_name"]))
            data_historicos = mcw.consultar_historicos_mx()
            #Guardamos los datos recibidos en un dataframe
            print(data_historicos)
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 3.")
#sub-menú para consultar los registros hechos de la función .submenu_consulta_web()
def submenu_consulta_registros():
    pass
    """
    while True:
        subopciones_names = [] #Agregar nombres de las opciones que tendrá el submenu estadisticas
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
#sub-menú para consultar las estadísticas
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
#sub-menú para consultar las graficas
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
def borrar_registros():
    pass
if __name__ == "__main__":
    menu_principal() #iniciar el programa

