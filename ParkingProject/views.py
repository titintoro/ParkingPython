def menu_cliente():
    res = input("<< Cliente >>"
                "\n\n\t|*| Elija la opción que desea realizar:"
                "\n\t|1| Depositar Coche sin abono."
                "\n\t|2| Depositar coche con abono."
                "\n\t|3| Retirar coche sin abono."
                "\n\t|4| Retirar coche con abono."
                "\n\t|*| Pulse otro número para volver.")
    return res


def menu_admin():
    res = input("\n\n<< Admin >>"
                "\n\n\t|*| Elija la opción que desea realizar:"
                "\n\t|1| Mostrar estado del parking."
                "\n\t|2| Mostrar los cobros entre dos fechas."
                "\n\t|3| Consultar Abonos."
                "\n\t|4| Dar de alta un abono."
                "\n\t|5| Modificar abono."
                "\n\t|6| Dar de baja abono."
                "\n\t|7| Consultar abonos que caducan en el mes seleccionado."
                "\n\t|8| Consultar abonos que caducan en los próximos 10 días."
                "\n\t|*|Pulse otro número para volver.")
    return res


def init_menu():
    res = input("\nIndique su rol en el parking (PRESIONE 1 o 2):"
                "\nRECUERDE GUARDAR ANTES DE CERRAR EL PROGRAMA"
                "\n\t|1| Cliente"
                "\n\t|2| Administrador\n"
                "\n\t|0| GUARDAR Y SALIR")
    return res


def ticket(fecha, matricula, id_plaza, pin):
    print("\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("|                                                            |")
    print("\t\tFecha: {}/{}/{}\tHora: {}:{}:{}                   ".format(fecha.year, fecha.month, fecha.day,
                                                                            fecha.hour, fecha.minute, fecha.second))
    print("|                                                            |")
    print(f"\t\tMatricula: {matricula}\t\tIDplaza: {id_plaza}                       |")
    print("|                                                            |")
    print(f"\t\tPIN: {pin}                                            ")
    print("|                                                            |")
    print("|                                                            |")
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
