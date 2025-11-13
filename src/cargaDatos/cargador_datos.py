import pandas as pd

class CargadorDatos:
    def __init__(self, dataFrame=pd.DataFrame()):
        self.__dataFrame = dataFrame
        self.__actualizar_attr()

    def __actualizar_attr(self):
        self.__num_filas = self.__dataFrame.shape[0]
        self.__num_columnas = self.__dataFrame.shape[1]

        porcentaje_nulos = (self.__dataFrame.isnull().mean() * 100).round(2)
        self.__porcentaje_nulos = porcentaje_nulos[porcentaje_nulos > 0]

    @property 
    def dataFrame(self):
        return self.__dataFrame
    
    @dataFrame.setter
    def dataFrame(self, nuevo_df):
        self.__dataFrame = nuevo_df
        self.__actualizar_attr()

    @property
    def num_filas(self):
        return self.__num_filas
    
    @property
    def num_columnas(self):
        return self.__num_columnas
    
    @property
    def porcentaje_nulos(self):
        return self.__porcentaje_nulos