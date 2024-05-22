import matplotlib.pyplot as plt 
import seaborn as sns

def graficar_totales_pais(df):

    df_grafica = df.loc[['3','7','9','5'],:]
    # Extraer datos del df
    x = df_grafica['Nombre']
    y = df_grafica['Valor']

    # Crear un bar chart
    plt.bar(x, y)

    # Agregar titulo y leyendas
    plt.xlabel('Categoria')
    plt.ylabel('Valor')
    return plt
    
def graficar_historicos_pais(df, current_date, current_time):
    
    df['cases'].plot(kind='line', figsize=(8, 4))
    
    df['recovered'].plot(kind='line', figsize=(8, 4))
    
    df['deaths'].plot(kind='line', figsize=(8, 4), title='Casos (azul) vs Recuperados (naranja) vs Muertes (verde)')
    plt.savefig(f'Graficas/casosVSrecuperadosVSmuertes_{current_date}_{current_time}.png') #guardar grafica
    
