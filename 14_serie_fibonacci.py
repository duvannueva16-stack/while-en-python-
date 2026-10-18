lectura = int(input("ingrese la cantidad de terminos "))
numero_1 = 0
numero_2 = 1
contador = 1

while contador <= lectura: 
    print(numero_1)
    contador = contador + 1
    siguiente = numero_1 + numero_2
    numero_1 = numero_2
    numero_2 = siguiente
    
    
