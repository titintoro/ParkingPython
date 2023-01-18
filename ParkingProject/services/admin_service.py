from models.parking import Parking
from datetime import datetime
from models.cobro import Cobro
from models.abonado import Abonado
import views

import random


def mostrar_datos_plazas_parking(parking):
    for p in parking.plazas:
        print(f"Plaza\t{p.id_plaza}\t\t{p.estado}")


def consultar_cobros_abonos(parking):
    for a in parking.abonados:
        print(f'Abonado: {a.nombre}\t\tAbono: {a.tipo_abono}\t\tPrecio: {a.cobro.precio}')


def consultar_cobros_no_abonos(parking):
    anio_inicio = int(input('Introduzca el año de inicio'))
    mes_inicio = int(input('Introduzca el mes de inicio'))
    dia_inicio = int(input('Introduzca el dia de inicio'))
    hora_inicio = int(input('Introduzca la hora de inicio'))
    min_inicio = int(input('Introduzca el minuto de inicio'))
    seg_inicio = int(input('Introduzca el segundo de inicio'))

    anio_fin = int(input('Introduzca el año de fin'))
    mes_fin = int(input('Introduzca el mes de fin'))
    dia_fin = int(input('Introduzca el dia de fin'))
    hora_fin = int(input('Introduzca la hora de fin'))
    min_fin = int(input('Introduzca el minuto de fin'))
    seg_fin = int(input('Introduzca el segundo de fin'))

    fecha_inicio = datetime(anio_inicio, mes_inicio, dia_inicio, hora_inicio, min_inicio, seg_inicio)
    fecha_fin = datetime(anio_fin, mes_fin, dia_fin, hora_fin, min_fin, seg_fin)
    for c in parking.cobros:
        if not c.is_abonado and fecha_inicio < c.fecha_cobro < fecha_fin:
            print(f'Fecha cobro:{c.fecha_cobro}\t\t {c.precio}')


def crear_abonado(parking):
    salir = False
    matricula = input('Introduzca la matrícula de su vehículo:\n')
    dni = input('Introduzca su DNI:\n')
    nombre = input('Introduzca su nombre:\n')
    num_tarjeta = input('Introduzca su número de tarjeta:\n')
    apellidos = input('Introduzca sus apellidos:\n')
    email = input('Introduzca su email:\n')
    tipo_abono = int(input('Introduzca su tipo de abono(SELECCIONE 1, 2, 3 O 4):'
                           '\n1. Mensual'
                           '\n2. Trimestral'
                           '\n3. Semestral'
                           '\n4. Anual'))
    tipo = int(input(
        'Seleccione el tipo de vehículo (SELECCIONE 1, 2 O 3):\n\t1. Turismo\n\t2. Moto\n\t3. Vehículo Minusválidos'))

    for p in parking.plazas:
        if tipo == 1 and salir == False:
            if p.estado.__eq__('libre') and p.vehiculo.tipo.__eq__('Turismo'):
                p.estado = 'abono libre'
                p.fecha_ocupacion = datetime.now()
                p.vehiculo.matricula = matricula
                p.pin = random.randrange(1000, 10000)
                fecha_caducidad = 0
                precio = 0
                print(f'\nSe le ha reservado la plaza {p.id_plaza} para su abono.\n')

                if tipo_abono == 1:
                    fecha_caducidad = datetime.now().replace(month=+1)
                    precio = 25
                if tipo_abono == 2:
                    fecha_caducidad = datetime.now().replace(month=+3)
                    precio = 70

                if tipo_abono == 3:
                    fecha_caducidad = datetime.now().replace(month=+6)
                    precio = 130

                if tipo_abono == 4:
                    fecha_caducidad = datetime.now().replace(year=+1)
                    precio = 200

                cobro = Cobro(precio, fecha_caducidad, True)
                parking.add_cobro_to_parking(cobro)

                Parking.add_abonado_to_parking(parking,
                                               Abonado(dni, nombre, apellidos, num_tarjeta, tipo_abono, email,
                                                       p.vehiculo, p, p.pin,
                                                       p.fecha_ocupacion, fecha_caducidad, cobro))

                Parking.mostrar_todas_las_plazas(parking)
                salir = True
                views.ticket(p.fecha_ocupacion, p.vehiculo.matricula, p.id_plaza, p.pin)
                parking.mostrar_todos_los_cobros()

        if tipo == 2 and salir == False:
            if p.estado.__eq__('libre') and p.vehiculo.tipo.__eq__('Moto'):
                p.estado = 'abono libre'
                p.fecha_ocupacion = datetime.now()
                p.vehiculo.matricula = matricula
                p.pin = random.randrange(1000, 10000)
                fecha_caducidad = 0
                print(f'\nSe le ha reservado la plaza {p.id_plaza} para su abono.\n')
                if tipo_abono == 1:
                    fecha_caducidad = datetime.now().replace(month=+1)
                    precio = 25
                if tipo_abono == 2:
                    fecha_caducidad = datetime.now().replace(month=+3)
                    precio = 70

                if tipo_abono == 3:
                    fecha_caducidad = datetime.now().replace(month=+6)
                    precio = 130

                if tipo_abono == 4:
                    fecha_caducidad = datetime.now().replace(year=+1)
                    precio = 200

                cobro = Cobro(precio, True)
                parking.add_cobro_to_parking(cobro)
                Parking.add_abonado_to_parking(parking,
                                               Abonado(dni, nombre, apellidos, num_tarjeta, tipo_abono, email,
                                                       p.vehiculo, p, p.pin,
                                                       p.fecha_ocupacion, fecha_caducidad, cobro))

                Parking.mostrar_todas_las_plazas(parking)
                salir = True
                views.ticket(p.fecha_ocupacion, p.vehiculo.matricula, p.id_plaza, p.pin)
                parking.mostrar_todos_los_cobros()

        if salir == False and tipo == 3:
            if p.estado.__eq__('libre') and p.vehiculo.tipo.__eq__('Movilidad reducida'):
                p.estado = 'abono libre'
                p.fecha_ocupacion = datetime.now()
                p.vehiculo.matricula = matricula
                p.pin = random.randrange(1000, 10000)
                fecha_caducidad = 0
                precio = 0
                print(f'\nSe le ha reservado la plaza {p.id_plaza} para su abono.\n')
                if tipo_abono == 1:
                    fecha_caducidad = datetime.now().replace(month=+1)
                    precio = 25
                if tipo_abono == 2:
                    fecha_caducidad = datetime.now().replace(month=+3)
                    precio = 70

                if tipo_abono == 3:
                    fecha_caducidad = datetime.now().replace(month=+6)
                    precio = 130

                if tipo_abono == 4:
                    fecha_caducidad = datetime.now().replace(year=+1)
                    precio = 200

                cobro = Cobro(precio, fecha_caducidad, True)
                parking.add_cobro_to_parking(cobro)
                Parking.add_abonado_to_parking(parking,
                                               Abonado(dni, nombre, apellidos, num_tarjeta, tipo_abono, email,
                                                       p.vehiculo, p, p.pin,
                                                       p.fecha_ocupacion, fecha_caducidad, cobro))

                parking.mostrar_todas_las_plazas()
                salir = True
                views.ticket(p.fecha_ocupacion, p.vehiculo.matricula, p.id_plaza, p.pin)
                parking.mostrar_todos_los_cobros()

        if not salir:
            print('El parking está lleno, vuelva más tarde, disculpe las molestias.\n')

        elif 1 > tipo > 3:
            print('Ha introducido un valor incorrecto.')


def modificar_abono(parking):
    id_plaza = int(input('Introduzca el id de su plaza abonada:'))
    pin = int(input('Introduzca el pin asociado a su abono:'))
    op = int(input('Qué desea hacer:'
               '\n\t1. Modificar Datos Personales'
               '\n\t2. Ampliar Abono'))
    for a in parking.abonados:
        if id_plaza == a.plaza.id_plaza and pin == a.plaza.pin:
            if op == 1:
                dni = input('Introduzca su nuevo DNI:\n')
                nombre = input('Introduzca su nuevo nombre:\n')
                apellidos = input('Introduzca sus nuevos apellidos:\n')
                num_tarjeta = input('Introduzca su nuevo número de tarjeta:\n')
                email = input('Introduzca su nuevo email:\n')

                a.nombre = nombre
                a.dni = dni
                a.num_tarjeta = num_tarjeta
                a.apellidos = apellidos
                a.email = a.email

            if op == 2:
                tipo_abono = int(input('Introduzca cuánto tiempo quiere ampliar su abono(SELECCIONE 1, 2, 3 O 4):'
                                       '\n1. Un mes'
                                       '\n2. Tres meses'
                                       '\n3. Seis meses'
                                       '\n4. Un año'))
                if tipo_abono == 1:
                    fecha_caducidad = a.fecha_caducidad_abono.replace(month=+1)
                    a.fecha_caducidad_abono = fecha_caducidad
                    precio = 25
                    cobro = Cobro(precio, fecha_caducidad, True)
                    a.cobro = cobro
                    parking.add_cobro_to_parking(cobro)
                    print('Ha ampliado su abono un mes.')

                if tipo_abono == 2:
                    fecha_caducidad = a.fecha_caducidad_abono.replace(month=+3)
                    a.fecha_caducidad_abono = fecha_caducidad
                    precio = 70
                    cobro = Cobro(precio, fecha_caducidad, True)
                    a.cobro = cobro
                    parking.add_cobro_to_parking(cobro)
                    print('Ha ampliado su abono tres meses.')

                if tipo_abono == 3:
                    fecha_caducidad = a.fecha_caducidad_abono.replace(month=+6)
                    a.fecha_caducidad_abono = fecha_caducidad
                    precio = 130
                    cobro = Cobro(precio, fecha_caducidad, True)
                    a.cobro = cobro
                    parking.add_cobro_to_parking(cobro)
                    print('Ha ampliado su abono seis meses.')

                if tipo_abono == 4:
                    fecha_caducidad = a.fecha_caducidad_abono.replace(year=+1)
                    a.fecha_caducidad_abono = fecha_caducidad
                    precio = 200
                    cobro = Cobro(precio, fecha_caducidad, True)
                    a.cobro = cobro
                    parking.add_cobro_to_parking(cobro)
                    print('Ha ampliado su abono un año.')

                else:
                    print('Ha introducido un valor incorrecto.')
