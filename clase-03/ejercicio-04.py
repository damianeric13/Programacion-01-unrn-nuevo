# Sistema de acceso a un banco.
# Datos:
#     clave_almacenada
#     clave_ingresada
#     usa_token (True o False)
clave_almacenada = int(1234)
clave_ingresada = int(input("por favor ingrese contraseña: "))
token = str(input("usa token si/no:"))
if clave_almacenada == clave_ingresada :
    print ("puede ingresar usuario") 
elif token == "si":
    print("usted puede ingresar")
else:
    print("usted no puede ingresar")