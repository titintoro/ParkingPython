import pickle


class Ticket:

    def __init__(self, matricula_vehiculo, fecha_ocupacion, id_plaza, pin):
        self.__matricula_vehiculo = matricula_vehiculo
        self.__fecha_ocupacion = fecha_ocupacion
        self.__id_plaza = id_plaza
        self.__pin = pin

    @property
    def matricula_vehiculo(self):
        return self.__matricula_vehiculo

    @matricula_vehiculo.setter
    def matricula_vehiculo(self, matricula_vehiculo):
        self.__matricula_vehiculo = matricula_vehiculo

    @property
    def fecha_ocupacion(self):
        return self.__fecha_ocupacion

    @fecha_ocupacion.setter
    def fecha_ocupacion(self, fecha_ocupacion):
        self.__fecha_ocupacion = fecha_ocupacion

    @property
    def id_plaza(self):
        return self.__id_plaza

    @id_plaza.setter
    def id_plaza(self, id_plaza):
        self.__id_plaza = id_plaza

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin
