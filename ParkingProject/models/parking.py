class Parking:

    def __init__(self, plazas=[]):
        self.__plazas = plazas
        self.__cobros = []
        self.__abonados = []

    def mostrar_todas_las_plazas(self):
        for p in self.plazas:
            print(p)

    @property
    def abonados(self):
        return self.__abonados

    @abonados.setter
    def abonados(self, x):
        self.__abonados = x

    @property
    def plazas(self):
        return self.__plazas

    @plazas.setter
    def plazas(self, x):
        self.__plazas = x

    @property
    def cobros(self):
        return self.__plazas

    @cobros.setter
    def cobros(self, x):
        self.__cobros = x

    def add_plaza_to_parking(self, plaza):
        self.__plazas.append(plaza)

    def add_cobro_to_parking(self, cobro):
        self.__cobros.append(cobro)

    def add_abonado_to_parking(self, abonado):
        self.__abonados.append(abonado)

    def mostrar_todos_los_cobros(self):
        for c in self.__cobros:
            print(c)
