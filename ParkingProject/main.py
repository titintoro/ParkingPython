import views

print("<< PARKING BOSCO >>")

authType = int(views.init_menu())

print(authType)

if authType == 1:
    opCliente = int(views.menu_cliente())

    if opCliente == 1:
        matricula = int(input(''))



if authType == 2:
    print("Ha entrado como administrador")
