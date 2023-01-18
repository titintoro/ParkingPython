from datetime import datetime


class Cobro:

    def __init__(self, precio, is_abonado):
        self.__precio = precio
        self.__fecha_cobro = datetime.now()
        self.__is_abonado = is_abonado

    @property
    def is_abonado(self):
        return self.__is_abonado

    @is_abonado.setter
    def is_abonado(self, x):
        self.__is_abonado = x


    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, x):
        self.__precio = x


    @property
    def fecha_cobro(self):
        return self.__fecha_cobro

    @fecha_cobro.setter
    def fecha_cobro(self, x):
        self.__fecha_cobro = x

    def __str__(self):
        return f"Cobro: \t{self.__fecha_cobro}\t{self.__precio}."
