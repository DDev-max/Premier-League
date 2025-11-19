import pandas as pd

class Jugador:
    def __init__(self, name, team, position, age, minutes, goals, assists):
        self.__name = name
        self.__team = team
        self.__position = position
        self.__age = age
        self.__minutes = minutes
        self.__goals = goals
        self.__assists = assists

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, nuevo_nombre):
        self.__name = nuevo_nombre


    @property
    def team(self):
        return self.__team
    @team.setter
    def team(self, nuevo_equipo):
        self.__team = nuevo_equipo

    @property
    def position(self):
        return self.__position
    @team.setter
    def position(self, nueva_posicion):
        self.__position = nueva_posicion

    @property
    def age(self):
        return self.__age
    @team.setter
    def age(self, nueva_edad):
        self.__age = nueva_edad

    @property
    def goals(self):
        return self.__goals

    @goals.setter
    def goals(self, nuevo_valor: int):
        if nuevo_valor >= 0:
            self.__goals = nuevo_valor
        else:
            raise ValueError("El valor de goles no puede ser negativo.")


    @property
    def minutes(self):
        return self.__minutes


    @minutes.setter
    def minutes(self, nuevo_valor: float):
        if nuevo_valor >= self.__minutes:
            self.__minutes = nuevo_valor
        else:
            print("Advertencia: Los minutos solo deben ser incrementados.")

    @property
    def assist(self):
        return self.__assists
    @team.setter
    def assist(self, nueva_assist):
        self.__assists = nueva_assist
