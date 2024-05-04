#Agregar directorios de los modulos al PATH de python
import sys
sys.path.append('Modulos')
#Modulos del menu
import modulo_consulta_web as mcw
import modulo_consulta_registros as mcr


#MENÚ PRINCIPAL

dict_menu = {
    "1": "Consulta web",
    "2": "Consulta registros",
    "3": "Estadísticas",
    "4": "Graficas",
    "5": "Salir"
       }

print("-----MENÚ-----")
#Mostrar Menu principal
for clave, valor in dict_menu.items():
    print(clave + "-" + valor)

opcion = input("Elegir opción: ")

if opcion == "1": #submenu - consulta web
    mcw.iniciar()
elif opcion == "2":#submenu - consulta registros
    pass
elif opcion == "3": #submenu - estadisticas
    pass
elif opcion == "4": #submenu - graficas
    pass
else: #salir
    pass


