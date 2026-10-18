base = int(input("ingrese base como un numero "))
exponente = int(input("ingrese ahora su exponente"))
contador = 1 
acumulador = 1 



while contador <= exponente:
    acumulador  = acumulador * base 
    contador = contador + 1 
    
print(acumulador)
    