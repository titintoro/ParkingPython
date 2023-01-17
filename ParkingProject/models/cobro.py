from datetime import datetime


class Cobro:

    def __init__(self, precio):
        self.__precio = precio
        self.__fecha_cobro = datetime.now()
