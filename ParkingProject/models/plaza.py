class Plaza:

    def __init__(self, estado, id_plaza, vehiculo, fecha_ocupacion):
        self.__estado = estado
        self.__id_plaza = id_plaza
        self.__vehiculo = vehiculo
        self.__fecha_ocupacion = fecha_ocupacion
        self.__pin = 0

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, x):
        self.__pin = x

    @property
    def fecha_ocupacion(self):
        return self.__fecha_ocupacion

    @fecha_ocupacion.setter
    def fecha_ocupacion(self, x):
        self.__fecha_ocupacion = x

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, x):
        self.__estado = x

    @property
    def id_plaza(self):
        return self.__id_plaza

    @id_plaza.setter
    def id_plaza(self, x):
        self.__id_plaza = x

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, x):
        self.__vehiculo = x

    def __str__(self):
        return f"Plaza\t{self.__id_plaza}\t{self.__pin}\t{self.__estado}\t\t{self.__vehiculo}"
