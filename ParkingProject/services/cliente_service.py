from models.parking import Parking
from models.vehiculo import Vehiculo
from datetime import datetime, timedelta
from models.cobro import Cobro
from models.abonado import Abonado
import views
import random


def depositar_vehiculo_sin_abono(parking):
    while (True):
        try:
            salir = False
            matricula = input('Introduzca la matrícula de su vehículo:')
            tipo = int(input(
                'Seleccione el tipo de vehículo (SELECCIONE 1, 2 O 3):\n\t1. Turismo\n\t2. Moto\n\t3. Vehículo '
                'Minusválidos'))

            for p in parking.plazas:
                if tipo == 1 and salir == False:
                    if p.estado.__eq__('libre') and p.vehiculo.tipo.__eq__('Turismo'):
                        p.estado = 'ocupado'
                        p.fecha_ocupacion = datetime.now()
                        p.vehiculo.matricula = matricula
                        p.pin = random.randrange(1000, 10000)
                        print(f'\nSe le ha asignado la plaza {p.id_plaza}, adelante.\n')
                        Parking.mostrar_todas_las_plazas(parking)
                        salir = True
                        views.ticket(p.fecha_ocupacion, p.vehiculo.matricula, p.id_plaza, p.pin)

                if tipo == 2 and salir == False:
                    if p.estado.__eq__('libre') and p.vehiculo.tipo.__eq__('Moto'):
                        p.estado = 'ocupado'
                        p.fecha_ocupacion = datetime.now()
                        p.vehiculo.matricula = matricula
                        p.pin = random.randrange(1000, 10000)
                        print(f'\nSe le ha asignado la plaza {p.id_plaza}, adelante.\n')
                        salir = True
                        views.ticket(p.fecha_ocupacion, p.vehiculo.matricula, p.id_plaza, p.pin)

                if salir == False and tipo == 3:
                    if p.estado.__eq__('libre') and p.vehiculo.tipo.__eq__('Movilidad reducida'):
                        p.estado = 'ocupado'
                        p.fecha_ocupacion = datetime.now()
                        p.vehiculo.matricula = matricula
                        p.pin = random.randrange(1000, 10000)
                        print(f'\nSe le ha asignado la plaza {p.id_plaza}, adelante.\n')
                        salir = True
                        views.ticket(p.fecha_ocupacion, p.vehiculo.matricula, p.id_plaza, p.pin)

            if not salir:
                print('El parking está lleno, vuelva más tarde, disculpe las molestias.\n')
        except:
            print("Ha ocurrido un error, introduce bien el tipo de vehículo")
        else:
            break


def retirar_vehiculo_sin_abono(parking):
    while (True):
        try:
            matricula = input('Introduzca la matrícula de su vehículo:')
            id_plaza = int(input('Introduzca el id de la plaza de su vehículo:'))
            pin = int(input('Introduzca el pin de su ticket:'))
            plaza = parking.plazas[id_plaza - 1]

            if pin == plaza.pin and id_plaza == plaza.id_plaza and matricula == plaza.vehiculo.matricula:
                diferencia = round(((datetime.now() - plaza.fecha_ocupacion).total_seconds() / 60), 2)
                if plaza.vehiculo.tipo == 'Turismo':
                    precio = diferencia * 0.12
                if plaza.vehiculo.tipo == 'Moto':
                    precio = diferencia * 0.08
                if plaza.vehiculo.tipo == 'Movilidad reducida':
                    precio = diferencia * 0.10
                print(precio)
                parking.add_cobro_to_parking(Cobro(precio, datetime.now(), False))
                plaza.estado = 'libre'
                plaza.vehiculo.matricula = ''
                plaza.pin = 0
        except:
            print("Ha ocurrido un error, introduce bien el id de la plaza o el pin")
        else:
            break


def depositar_vehiculo_con_abono(parking):
    while (True):
        try:
            matricula = input('Introduzca la matrícula de su vehículo:')
            dni = input('Introduzca su DNI')
            id_plaza = int(input('Introduzca el id de la plaza de su vehículo:'))

            for a in parking.abonados:
                if a.dni == dni and a.plaza.vehiculo.matricula == matricula and a.plaza.id_plaza == id_plaza and a.plaza.estado == 'abono libre':
                    a.plaza.estado = 'abono ocupado'

                else:
                    print('Ha introducido datos erróneos')
        except:
            print("Ha ocurrido un error, introduce bien el el id de la plaza")
        else:
            break


def retirar_vehiculo_con_abono(parking):
    while(True):
        try:
            id_plaza = int(input('Introduzca el id de su plaza'))
            matricula = input('Introduzca la matrícula de su vehículo:')
            pin = int(input('Introduzca el pin de su ticket:'))
            exists = False
            plaza = parking.plazas[id_plaza - 1]

            if plaza.id_plaza == id_plaza and plaza.vehiculo.matricula == matricula and plaza.pin == pin and plaza.estado == 'abono ocupado':
                plaza.estado = 'abono libre'
                exists = True

            if not exists:
                print('Ha introducido datos erróneos.')
        except:
            print("Ha ocurrido un error, introduce bien el el id de la plaza o el pin.")
        else:
            break
