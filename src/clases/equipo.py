from typing import List
from src.clases.jugador import Jugador

class Equipo:
    """
    Representa un equipo. Contiene una lista de objetos Jugador.
    """
    LIGA = "Premier League"  # Atributo fijo

    def __init__(self, name: str, jugadores: List[Jugador]):
        self.__name = name
        self.__jugadores = jugadores

    @property
    def name(self):
        return self.__name

    @property
    def jugadores(self):
        return self.__jugadores

    @property
    def total_jugadores(self) -> int:
        return len(self.__jugadores)

