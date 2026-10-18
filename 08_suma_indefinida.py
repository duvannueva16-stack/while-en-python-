suma = 0
numero = float(input("ingrese un numero real y 0 para terminar"))

while numero != 0:
    suma = suma + numero
    numero = float(input("ingrese el siguiente numero"))
    
print(suma)