#from turtle import color
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
    return plt #Se retorna la grafica
    
def graficar_historicos_pais(df_historicos, current_date, current_time):
    #linea para los casos
    df_historicos['cases'].plot(kind='line', figsize=(8, 4))
    #linea para los casos recuperados
    df_historicos['recovered'].plot(kind='line', figsize=(8, 4))
    #linea para las muertes
    df_historicos['deaths'].plot(kind='line', figsize=(8, 4), title='Casos (azul) vs Recuperados (naranja) vs Muertes (verde)')
    plt.savefig(f'Graficas/casosVSrecuperadosVSmuertes_{current_date}_{current_time}.png') #guardar grafica
    
def graficar_globales(df_globales, current_date, current_time):
    # Numero mas alto de casos activos por pais.
    df_globales.sort_values('Activos', ascending=False).head(10).plot(x='País', y='Activos', kind='bar')
    plt.savefig(f'Graficas/casos_activos_{current_date}_{current_time}.png') #guardar grafica
    
    # Continente vs Muertes grafico tipo violin
    figsize = (12, 1.2 * len(df_globales['Continente'].unique()))
    plt.figure(figsize=figsize)
    sns.violinplot(df_globales, x='Muertes', y='Continente', inner='stick', palette='Dark2')
    sns.despine(top=True, right=True, bottom=True, left=True)
    plt.savefig(f'Graficas/continenteVSmuertes{current_date}_{current_time}.png') #guardar grafica
    
    #Continente vs Casos
    figsize = (12, 1.2 * len(df_globales['Continente'].unique()))
    plt.figure(figsize=figsize)
    sns.violinplot(df_globales, x='Casos', y='Continente', inner='stick', palette='Dark2')
    sns.despine(top=True, right=True, bottom=True, left=True)
    plt.savefig(f'Graficas/continenteVScasos{current_date}_{current_time}.png') #guardar grafica
    
def graficar_globales_historicos(df_globales_historicos, current_date, current_time):
    #Crea la primera linea relativa a los casos
    df_globales_historicos['cases'].plot(kind='line', figsize=(8, 4))
    
    #Crea la segunda linea  relativa a los casos recuperados
    df_globales_historicos['recovered'].plot(kind='line', figsize=(8, 4))

    #Crear la tercera linea relativa a las muertes
    df_globales_historicos['deaths'].plot(kind='line', figsize=(8, 4), title='Casos (azul) vs Casos recuperados (naranja) vs Muertes (verde)')
    plt.gca().spines[['top', 'right']].set_visible(False) #mostrar la grafica
    plt.savefig(f'Graficas/casosVSrecuperadosVSmuertes_hist_{current_date}_{current_time}.png') #guardar grafica

def graficar_vacunas(df_vacunas, current_date, current_time):
    """
    Muestra grafica de series temporales de las dosis administradas de un pais desde el inicio de la pandemia.
    """
    # grafica dosis administradas a traves del tiempo
    df_vacunas['dosis administradas'].plot(kind='line', figsize=(8, 4), title='dosis administradas', color = 'orange')
    plt.gca().spines[['top', 'right']].set_visible(False)
    plt.savefig(f'Graficas/dosis_administradas_{current_date}_{current_time}.png')