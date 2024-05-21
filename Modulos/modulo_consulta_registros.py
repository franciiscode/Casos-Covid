


def cargar_rutas(rutas):
   """
   Escribe las rutas de los archivos almacenados

   Args:
       rutas (dict): Diccionario con las rutas de los archivos almacenados
   """
   f = open('Reportes de consulta API/rutas_registros_totales_pais.txt', mode = 'a')
   f.write(f'{rutas}')
   f.close()
