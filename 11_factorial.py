numero = int(input("ingrese un numero para calcular su factorial que sea positivo"))
contador = 1
factorial = 1

while contador <= numero:
    factorial = factorial * contador 
    contador = contador + 1 
    
print("el factorial del numero es: ", factorial)
    
    
    