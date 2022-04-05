import random


class Dado:
    def __init__(self, lados=6):
        self.__lados = lados

    def dameUnNumero(self):
        return random.randint(1, self.__lados)
