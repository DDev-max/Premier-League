import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re


class ProcesadorEDA:
    def __init__(self, dataFrame = pd.DataFrame()):
        self.__dataFrame = dataFrame
        self.__actualizar_resumen_y_tipos()


    def __actualizar_resumen_y_tipos(self):
        self.__resumen_descriptivo = self.__dataFrame.describe()
        self.__ver_tipos = {
            'numericas': self.__dataFrame.select_dtypes(include=['number']).columns.tolist(),
            'textual': self.__dataFrame.select_dtypes(include=['object']).columns.tolist(),
            'categoria': self.__dataFrame.select_dtypes(include=['category']).columns.tolist(),
            'fechas': self.__dataFrame.select_dtypes(include=['datetime']).columns.tolist(),
            'booleanos': self.__dataFrame.select_dtypes(include=['bool']).columns.tolist()
        }

    @property
    def dataFrame(self):
        return self.__dataFrame
    
    @dataFrame.setter
    def dataFrame(self, nuevo_df):
        self.__dataFrame = nuevo_df
        self.__actualizar_resumen_y_tipos()


    ## LIMPIEZA DE DATOS ##
    #Manejo de nulos
    def cambiar_nulos(self, metodo, columnas):
        if metodo == 'eliminar':
            self.__dataFrame.dropna(subset=columnas, inplace=True)

        elif metodo == 'promedio':
            self.__dataFrame[columnas] = self.__dataFrame[columnas].fillna(self.__dataFrame[columnas].mean())

        elif metodo == 'mediana':
            self.__dataFrame[columnas] = self.__dataFrame[columnas].fillna(self.__dataFrame[columnas].median())

        elif metodo == 'moda':
            self.__dataFrame[columnas] = self.__dataFrame[columnas].fillna(self.__dataFrame[columnas].mode().iloc[0])

    # Convertir a tipos correctos
    def convertir_a_fecha(self, columnas=[], formato=None):
        for col in columnas:
            if col in self.__dataFrame.columns:
                self.__dataFrame[col] = pd.to_datetime(
                    self.__dataFrame[col],
                    format=formato,
                    errors='coerce'
                )
        self.__actualizar_resumen_y_tipos()


    def convertir_a_numero(self, columnas=[], eliminar=None, reemplazar=[]):
        for col in columnas:
            if col in self.__dataFrame.columns:
                serie = self.__dataFrame[col].astype(str)

                if eliminar:
                    serie = serie.str.replace(eliminar, '', regex=True)

                if reemplazar:
                    serie = serie.str.replace(reemplazar[0], reemplazar[1])

                self.__dataFrame[col] = pd.to_numeric(serie, errors='coerce')
        self.__actualizar_resumen_y_tipos()



    def convertir_a_categoria(self, columnas = []):
        self.__dataFrame[columnas] = self.__dataFrame[columnas].astype('category')
        self.__actualizar_resumen_y_tipos()


    #Normalizar valores
    def normalizar_col_str(self, columnas=[],regex=None):
        for col in columnas:
            self.__dataFrame[col] = self.__dataFrame[col].apply(
                lambda str: self.__limpiar_texto(str, regex)
            )


    def __limpiar_texto(self, texto, regex=None):        
        if pd.isna(texto):
            return texto
        
        texto = str(texto).upper().strip()
        default_regex = r"[^A-ZÁÉÍÓÚÜÑ0-9\s]"  # elimina caracteres especiales
        regex_a_usar =  regex or default_regex
        texto = re.sub(regex_a_usar, "", texto)
        return texto
    
    # Quitar columnas
    def eliminar_cols(self, columnas = []):
        self.__dataFrame.drop(columns=columnas, inplace=True)
        self.__actualizar_resumen_y_tipos()


    # Combinar columnas (calcular porcentaje)
    def calc_porcentaje(self, dividendo, divisor, col_nombre):
        df = self.__dataFrame
        df[col_nombre] = ((df[dividendo] / df[divisor] * 100)
                        .where(df[divisor] != 0, other=0)
                        .round(1))
        self.__actualizar_resumen_y_tipos()


    ## RESUMEN DESCRIPTIVO ##
    @property
    def resumen_descriptivo(self):
        return self.__resumen_descriptivo
    
    @property
    def ver_tipos(self):
        return self.__ver_tipos
    
    
    ## MATRIZ DE CORRELACION
    def matriz_correlacion(self):
        correlaciones = self.__dataFrame.corr(numeric_only=True)
                
        plt.figure(figsize=(8, 6))
        sns.heatmap(correlaciones,center=0, cmap='coolwarm', annot=True,  annot_kws={"size": 5})

        plt.title("Matriz de Correlación")
        plt.tight_layout()
        plt.show()

