from models.parking import Parking
from models.vehiculo import Vehiculo
from datetime import datetime


class ClienteService:

    def depositar_vehiculo_sin_abono(parking):
        Parking.mostrar_todas_las_plazas(parking)
        salir = False
        matricula = input('Introduzca la matrícula de su vehículo:')
        tipo = int(input(
            'Seleccione el tipo de vehículo (SELECCIONE 1, 2 O 3):\n\t1. Turismo\n\t2. Moto\n\t3. Vehículo Minusválidos'))
        for p in parking.plazas:
            if tipo == 1 and salir == False:
                if p.estado.__eq__('libre') and p.vehiculo.tipo.__eq__('Turismo'):
                    p.estado = 'ocupado'
                    p.fecha_ocupacion = datetime.now()
                    p.vehiculo.matricula = matricula
                    print(f'\nSe le ha asignado la plaza {p.id_plaza}, adelante.\n')
                    salir = True
            if tipo == 2 and salir == False:
                if p.estado.__eq__('libre') and p.vehiculo.tipo.__eq__('Moto'):
                    p.estado = 'ocupado'
                    p.fecha_ocupacion = datetime.now()
                    p.vehiculo.matricula = matricula
                    print(f'\nSe le ha asignado la plaza {p.id_plaza}, adelante.\n')
                    salir = True
            if salir == False and tipo == 3:
                if p.estado.__eq__('libre') and p.vehiculo.tipo.__eq__('Movilidad reducida'):
                    p.estado = 'ocupado'
                    p.fecha_ocupacion = datetime.now()
                    p.vehiculo.matricula = matricula
                    print(f'\nSe le ha asignado la plaza {p.id_plaza}, adelante.\n')
                    salir = True
        if not salir:
            print('El parking está lleno, vuelva más tarde, disculpe las molestias.\n')

    def depositar_vehiculo_con_abono(parking):
        salir = False
        matricula = input('Introduzca la matrícula de su vehículo:\n')
        dni = input('Introduzca su DNI:\n')

        for p in parking.plazas:
            if salir == False and p.estado.__eq__('libre'):
                p.estado = 'ocupado'
                print(f'\nSe le ha asignado la plaza {p.id_plaza}')
                salir = True
