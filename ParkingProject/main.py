import views
from datetime import datetime
from models.plaza import Plaza
from models.parking import Parking
import services.cliente_service as cserv
from models.vehiculo import Vehiculo
import services.admin_service as aserv
import pickle


f = open('parkings.pckl', 'rb')
parkings = pickle.load(f)
parking = parkings[0]
f.close()

auth_type = 1

while auth_type != 0:
    auth_type = int(views.init_menu())
    print(auth_type)

    if auth_type == 1:
        opCliente = int(views.menu_cliente())

        if opCliente == 1:
            cserv.depositar_vehiculo_sin_abono(parking)

        if opCliente == 2:
            cserv.depositar_vehiculo_con_abono(parking)

        if opCliente == 3:
            cserv.retirar_vehiculo_sin_abono(parking)

        if opCliente == 4:
            cserv.retirar_vehiculo_con_abono(parking)

    if auth_type == 2:

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

        if op == 6:
            aserv.dar_de_baja_abono(parking)

        if op == 7:
            aserv.modificar_abono(parking)

        if op == 8:
            aserv.modificar_abono(parking)

    if auth_type == 0:
        parkingsupdate = [parking]
        f = open('parkings.pckl', 'wb')
        pickle.dump(parkingsupdate, f)
        f.close()



