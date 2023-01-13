from auth import authentication

print("<< PARKING BOSCO >>")

authType = int(authentication())

print(authType)

if authType==1:
    print("Ha entrado como cliente")

if authType==2:
    print("Ha entrado como administrador")