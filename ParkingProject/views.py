def menu_cliente():
    res = input("<< Cliente >>"
                "\n\n\tElija la opción que desea realizar:"
                "\n\t1. Depositar Coche sin abono."
                "\n\t2. Depositar coche con abono."
                "\n\t3. Retirar coche sin abono."
                "\n\t4. Retirar coche con abono.")
    return res;


def menu_admin():
    res = input("<< Admin >>"
                "\n\n\tElija la opción que desea realizar:"
                "\n\t1. Mostrar estado del parking."
                "\n\t2. Mostrar los cobros entre dos fechas."
                "\n\t3. Consultar Abonos."
                "\n\t4. Dar de alta un abono."
                "\n\t5. Modificar abono."
                "\n\t6. Dar de baja abono.\n"
                "\n\t7. Consultar abonos que caducan en el mes seleccionado."
                "\n\t8. Consultar abonos que caducan en los próximos 10 días")
    return res;

def init_menu():
    res = input("\nIndique su rol en el parking (PRESIONE 1 o 2):"
                "\n\t1. Cliente"
                "\n\t2. Administrado\n")
    return res


def ticket(fecha, matricula, id_plaza, pin):
    print("\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("|                                                            |")
    print("|\t\tFecha: {}/{}/{}\tHora: {}:{}:{}                   |".format(fecha.year, fecha.month, fecha.day, fecha.hour, fecha.minute, fecha.second))
    print("|                                                            |")
    print(f"|\t\tMatricula: {matricula}\t\tIDplaza: {id_plaza}                       |")
    print("|                                                            |")
    print(f"|\t\tPIN: {pin}                                            |")
    print("|                                                            |")
    print("|                                                            |")
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
