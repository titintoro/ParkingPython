from datetime import datetime


class Cobro:

    def __init__(self, precio):
        self.__precio = precio
        self.__fecha_cobro = datetime.now()

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
        return f"Plaza\t{self.__fecha_cobro}\t{self.__precio}."
