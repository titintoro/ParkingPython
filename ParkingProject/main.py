import views
from datetime import datetime
from models.plaza import Plaza
from models.parking import Parking
import services.cliente_service as cserv
from models.vehiculo import Vehiculo
import services.admin_service as aserv

print("<< PARKING BOSCO >>")

plazas = []
parking = Parking(plazas)

for p in range(1, 51):
    if 1 <= p <= 35:
        plaza = Plaza('libre', p, Vehiculo('Turismo'), datetime.now())
        parking.add_plaza_to_parking(plaza)
    if 36 <= p <= 42:
        plaza = Plaza('libre', p, Vehiculo('Moto'), datetime.now())
        parking.add_plaza_to_parking(plaza)
    if 43 <= p <= 51:
        plaza = Plaza('libre', p, Vehiculo('Movilidad reducida'), datetime.now())
        parking.add_plaza_to_parking(plaza)

authType = int(views.init_menu())

while authType != 0:
    print(authType)

    if authType == 1:
        opCliente = int(views.menu_cliente())

        if opCliente == 1:
            cserv.depositar_vehiculo_sin_abono(parking)

        if opCliente == 2:
            cserv.depositar_vehiculo_con_abono(parking)

        if opCliente == 3:
            cserv.retirar_vehiculo_sin_abono(parking)

        if opCliente == 4:
            cserv.retirar_vehiculo_con_abono(parking)

    if authType == 2:

        op = int(views.menu_admin())
        if op == 1:
            aserv.mostrar_datos_plazas_parking(parking)

        if op == 2:
            aserv.consultar_cobros_no_abonos(parking)

        if op == 3:
            aserv.consultar_cobros_abonos(parking)

        if op == 4:
            aserv.crear_abonado(parking)

        if op == 5:
            aserv.modificar_abono(parking)

    authType = int(views.init_menu())
