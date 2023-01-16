class Plaza:
    __estado = bool
    __id_plaza = int
    __tipo_vehiculo = ''

    def __init__(self, estado, id_plaza,tipo_vehiculo ):
        self.__estado = estado
        self.__id_plaza = id_plaza
        self.__tipo_vehiculo = tipo_vehiculo

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
    def tipo_vehiculo(self):
        return self.__tipo_vehiculo

    @tipo_vehiculo.setter
    def tipo_vehiculo(self, x):
        self.__tipo_vehiculo = x
