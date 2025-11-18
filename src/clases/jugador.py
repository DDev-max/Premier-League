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


@property
def team(self):
    return self.__team


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
