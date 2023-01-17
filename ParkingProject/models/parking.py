class Parking:

    def __init__(self, plazas=[]):
        self.__plazas = plazas
        self.__cobros = []

    def mostrar_todas_las_plazas(self):
        for p in self.plazas:
            print(p)

    @property
    def plazas(self):
        return self.__plazas

    @plazas.setter
    def plazas(self, x):
        self.__plazas = x

    @property
    def cobros(self):
        return self.__plazas

    @plazas.setter
    def plazas(self, x):
        self.__cobros = x

    def add_to_parking(self, plaza):
        self.__plazas.append(plaza)





