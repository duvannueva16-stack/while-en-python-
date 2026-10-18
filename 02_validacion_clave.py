contraseña = 1234
ingreso = int(input("ingrese su contraseña"))

while contraseña != ingreso:
    print("error de contraseña")
    ingreso = int(input("ingrese su contraseña"))
print("bienvenido")