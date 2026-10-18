contraseña = 1234

ingresoContraseña = int(input("ingrese su contraseña")) 
contador = 0


while ingresoContraseña != contraseña and contador<2:
        
        ingresoContraseña = int(input("ingrese su contraseña"))
        contador = contador + 1 

if ingresoContraseña == contraseña :
    print("bienvenido ")
else:
    print("cuenta bloqueada")
        
    
    
    
    
     
    
    
    
    
         
    
    