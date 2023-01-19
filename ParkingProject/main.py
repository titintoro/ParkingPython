import views
from datetime import datetime
from models.plaza import Plaza
from models.parking import Parking
import services.cliente_service as cserv
from models.vehiculo import Vehiculo
import services.admin_service as aserv
import pickle
from threading import Thread
import threading
import time

# Tarea a ejecutarse cada determinado tiempo.

f = open('parkings.pckl', 'rb')
parkings = pickle.load(f)
parking = parkings[0]
f.close()


def auto_update():
    hilo_principal_is_alive = True
    while hilo_principal_is_alive:
        secs = 0
        while secs < 300:  # Autoguardado cada 5 minutos
            if hilo_principal.is_alive():
                time.sleep(1)
                secs += 1
            else:
                secs = 300
                hilo_principal_is_alive = False
        parking_sauto_update = [parking]
        auto_update_f = open('parkings.pckl', 'wb')
        pickle.dump(parking_sauto_update, auto_update_f)
        auto_update_f.close()
        print("HA SALIDO DEL PROGRAMA")

    # Iniciar la ejecución en segundo plano.


def metodo_principal():
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
                aserv.mostrar_abonos_mes_indicado(parking)

            if op == 8:
                aserv.mostrar_abonos_caducan_prox_10_dias(parking)

        if auth_type == 0:
            print('SALIENDO DEL PROGRAMA...')
            parkingsupdate = [parking]
            update_f = open('parkings.pckl', 'wb')
            pickle.dump(parkingsupdate, update_f)
            update_f.close()


hilo_principal = threading.Thread(target=metodo_principal)
hilo_actualizador = threading.Thread(target=auto_update)

hilo_principal.start()
hilo_actualizador.start()
