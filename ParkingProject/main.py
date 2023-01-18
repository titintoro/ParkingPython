import views
from datetime import datetime
from models.plaza import Plaza
from models.parking import Parking
from services.cliente_service import ClienteService
from models.vehiculo import Vehiculo

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
            ClienteService.depositar_vehiculo_sin_abono(parking)

        if opCliente == 2:
            ClienteService.depositar_vehiculo_con_abono(parking)

        if opCliente == 3:
            ClienteService.retirar_vehiculo_sin_abono(parking)

        if opCliente == 4:
            ClienteService.retirar_vehiculo_con_abono(parking)

        if opCliente == 5:
            ClienteService.crear_abonado(parking)
    if authType == 2:
        print("Ha entrado como administrador")

    authType = int(views.init_menu())

