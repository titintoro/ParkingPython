def menu_cliente():
    res = input("<< Cliente >>"
                "\n\n\tElija la opción que desea realizar:"
                "\n\t1. Depositar Coche sin abono."
                "\n\t2. Depositar coche con abono."
                "\n\t3. Retirar coche sin abono."
                "\n\t4. Retirar coche con abono."
                "\n\t5. Menú de abonos.")
    return res;


def init_menu():
    res = input("\nIndique su rol en el parking (PRESIONE 1 o 2):"
                "\n\t1. Cliente"
                "\n\t2. Administrador")
    return res
