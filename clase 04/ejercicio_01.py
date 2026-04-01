### for 
### while: itinerador que repite la hasta que se cumpla la condicion
contrasena_registrada= "1234"
contrasena_correcta= False
while contrasena_correcta == False:
    for i in range(0,4): 
        contrasena_ingresada= input("ingresar contraseña:")
    if contrasena_ingresada == contrasena_registrada:
        contrasena_correcta=True
        print("Acceso Concedido")
    else:
        print("acceso denegado")
        break
