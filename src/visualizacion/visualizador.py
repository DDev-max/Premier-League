import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px  # Usamos Plotly para un gráfico interactivo (opcional)
from typing import List


class Visualizador:
<<<<<<< Updated upstream
    def __init__(self):
        pass
=======
    """
    Clase encargada de crear visualizaciones estáticas e interactivas
    a partir de la DataFrame limpia.
    """

    def __init__(self, dataframe: pd.DataFrame):
        # Usamos un atributo privado para mantener la DataFrame encapsulada
        self.__dataFrame = dataframe

    @property
    def dataFrame(self):
        """Permite acceder a la DataFrame limpia."""
        return self.__dataFrame

    # --- REQUISITO: GRÁFICO 1 - HISTOGRAMA (Distribución) ---
    def generar_histograma_goles(self):
        columna = 'Goals'
        if columna not in self.__dataFrame.columns:
            print(f"Error: La columna '{columna}' no se encuentra en el DataFrame.")
            return

        plt.figure(figsize=(10, 6))
        sns.histplot(self.__dataFrame[columna], bins=15, kde=True, log_scale=False)

        # Requisito: Título claro y Narrativa/Insight
        plt.title(f'Distribución de Goles Marcados por Jugador (Premier League)', fontsize=14)
        plt.xlabel('Número de Goles')
        plt.ylabel('Frecuencia de Jugadores')
        plt.grid(axis='y', alpha=0.5)
        plt.show()

        print("--- INSIGHT (Narrativa) ---")
        print("La distribución de goles está fuertemente sesgada hacia el extremo inferior.")
        print("La mayoría de los jugadores tienen pocos o cero goles, indicando que la producción")
        print("ofensiva recae en una pequeña élite de delanteros.")
        print("-----------------------------\n")

    # --- REQUISITO: GRÁFICO 2 - SCATTER PLOT (Correlación) ---
    def generar_scatter_goles_asistencias(self):
        x_col, y_col = 'Goals', 'Assists'
        if x_col not in self.__dataFrame.columns or y_col not in self.__dataFrame.columns:
            print(f"Error: Faltan las columnas '{x_col}' o '{y_col}'.")
            return

        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=x_col, y=y_col, data=self.__dataFrame, hue='Position', palette='viridis', alpha=0.7)

        # Requisito: Título claro y Narrativa/Insight
        plt.title('Goles vs. Asistencias: Productividad de los Jugadores', fontsize=14)
        plt.xlabel('Total de Goles Marcados')
        plt.ylabel('Total de Asistencias Realizadas')
        plt.legend(title='Posición')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()

        print("--- 📝 INSIGHT (Narrativa) ---")
        print("Existe una correlación positiva moderada entre Goles y Asistencias, lo cual es")
        print("esperable en jugadores ofensivos. Los puntos más alejados (outliers superiores)")
        print("representan a los 'jugadores estrella' que dominan ambos métricas.")
        print("-----------------------------\n")

    # --- GRÁFICO ADICIONAL - BARRAS (Top 10) ---

    def generar_top_10_goleadores(self, n=10):
        """
        Muestra un gráfico de barras con el top N de jugadores con más goles.
        """
        top_goleadores = self.__dataFrame.sort_values(by='Goals', ascending=False).head(n)

        plt.figure(figsize=(12, 6))
        sns.barplot(x='Player', y='Goals', data=top_goleadores, palette='Reds_d', hue='Player', legend=False)
        plt.xticks(rotation=45, ha='right')

        # Título y etiquetas
        plt.title(f'Top {n} Goleadores de la Premier League', fontsize=16)
        plt.xlabel('Jugador')
        plt.ylabel('Número de Goles')
        plt.tight_layout()
        plt.show()

        print("---INSIGHT (Narrativa) ---")
        if not top_goleadores.empty:
            print(
                f"El máximo goleador es {top_goleadores['Player'].iloc[0]} con {top_goleadores['Goals'].iloc[0]} goles.")
            print(
                "Este gráfico destaca a los delanteros de élite cuya alta producción individual impulsa a sus equipos.")
        else:
            print("No hay suficientes datos para determinar los máximos goleadores.")
        print("-----------------------------\n")

    # --- GRÁFICO OPCIONAL/EXTRA - INTERACTIVO (Plotly) ---
    def generar_interactivo_minutos_goles(self):
        """
        Gráfico interactivo de Plotly para visualizar Goles vs. Minutos jugados.
        """
        # Aseguramos usar las columnas correctas ('Minutes' y 'Team') de tu CSV
        fig = px.scatter(self.__dataFrame, x='Minutes', y='Goals', color='Team',
                         # CORRECCIÓN FINAL: Usando 'Player' en hover_data
                         hover_data=['Player', 'Position', 'Assists'],
                         title='Productividad por Minutos Jugados (Gráfico Interactivo)')

        fig.show()

        print("---INSIGHT (Narrativa) ---")
        print("Este gráfico permite a los analistas identificar de forma interactiva a jugadores")
        print("que anotan muchos goles con pocos minutos, lo que sugiere una alta eficiencia.")
        print("-----------------------------\n")
>>>>>>> Stashed changes
