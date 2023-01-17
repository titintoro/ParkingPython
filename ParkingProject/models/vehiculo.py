class Vehiculo:

    def __init__(self, tipo):
        self.tipo = tipo
        self.matricula = ''

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    def __str__(self):
        return f'{self.__tipo} {self.__matricula}'