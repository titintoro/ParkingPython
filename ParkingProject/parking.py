class Parking:
    __plazas = []  # Esta lista contendrá objetos de la clase plaza
    __numplazas_libres = 0

    def __init__(self, plazas=[]):
        self.__plazas = plazas

    def agregar(self, p):  # p será un objeto plaza
        self.plazas.append(p)

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
    def numplazas_libres(self):
        return self.__numplazas_libres

    @numplazas_libres.setter
    def numplazas_libres(self, x):
        self.__numplazas_libres = x
