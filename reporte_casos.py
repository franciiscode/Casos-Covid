#Modulos del menu
import modulo_consulta_web as mcw
import modulo_consulta_registros as mcr


#MENÚ PRINCIPAL
print("-----MENÚ-----")

opcion = input("Elegir opción: ")

if opcion == "1": #Submenu-Consultas Web
    mcw.prueba()
    
"""
if opcion == "2": #Submenu-Consultas registros
    def consulta_registros():
        pass

if opcion == "4": #Submenú-Estadísticas
    def mostrar_estadisticas():
        pass

if opcion == "5": #Submenu-Graficas
    def mostrar_graficas():
        pass
    
if opcion == "6": #Submenu-Eliminar todo
    def eliminar_registros():
        pass
else:
    pass
"""
