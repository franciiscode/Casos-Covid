import os

def crear_archivo_excel(dataframe,ruta_carpeta, nombre_archivo):
    
    ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)
    # Guardar el DataFrame en un archivo Excel
    
    dataframe.to_excel(ruta_completa, index=False)
    print(f"El archivo '{ruta_completa}' se ha creado exitosamente.")
