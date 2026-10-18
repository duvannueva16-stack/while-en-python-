notas = float(input("ingrese las notas y escriba -1 para salir"))
sumanotas = 0
contador = 0

while notas != -1:
    sumanotas = sumanotas + notas
    contador = contador + 1
    notas = float(input("ingrese las notas y escriba -1 para salir"))
if contador > 0:
    print("el promedio notas es: ", sumanotas/contador)

else:
    print("no ha ingresado datos")     
    

