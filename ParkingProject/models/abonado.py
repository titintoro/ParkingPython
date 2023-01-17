class Abonado:
    def __init__(self, dni, nombre, apellidos, num_tarjeta, tipo_abono, email, vehiculo, plaza, pin,
                 fecha_activacion_abono, fecha_caducidad_abono):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__num_tarjeta = num_tarjeta
        self.__tipo_abono = tipo_abono
        self.__email = email
        self.__vehiculo = vehiculo
        self.__plaza = plaza
        self.__pin = pin
        self.__fecha_activacion_abono = fecha_activacion_abono
        self.__fecha_caducidad_abono = fecha_caducidad_abono

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self._apellidos = apellidos

    @property
    def num_tarjeta(self):
        return self.__num_tarjeta

    @num_tarjeta.setter
    def num_tarjeta(self, num_tarjeta):
        self.__num_tarjeta = num_tarjeta

    @property
    def tipo_abono(self):
        return self.__tipo_abono

    @tipo_abono.setter
    def tipo_abono(self, tipo_abono):
        self.__tipo_abono = tipo_abono

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo

    @property
    def plaza(self):
        return self.__plaza

    @plaza.setter
    def plaza(self, plaza):
        self.__plaza = plaza

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    @property
    def fecha_activacion_abono(self):
        return self.__fecha_activacion_abono

    @fecha_activacion_abono.setter
    def fecha_activacion_abono(self, fecha_activacion_abono):
        self.__fecha_activacion_abono = fecha_activacion_abono

    @property
    def fecha_caducidad_abono(self):
        return self.__fecha_caducidad_abono

    @fecha_caducidad_abono.setter
    def fecha_caducidad_abono(self, fecha_caducidad_abono):
        self.__fecha_caducidad_abono = fecha_caducidad_abono
