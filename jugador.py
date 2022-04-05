
class Jugador:
    def __init__(self, nombre, dado):
        self.__nombre = nombre
        self.dado = dado

    @property
    def nombre(self):
        return self.__nombre

    def lanzarDado(self):
        lado = self.dado.dameUnNumero()
        print('Cara: {}'.format(lado))
        return lado
