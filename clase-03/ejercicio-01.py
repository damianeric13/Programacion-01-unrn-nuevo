# Ejercicio 1
# Diseñar un algoritmo que determine si
#  una persona puede entrar a un evento.
# Datos:
#     edad
#     tiene_documento (True o False)
edad = int(input("ingrese edad: "))
documento = input("tiene documento: ")
if edad >= 18 and documento == "si":
    print(f"Usted puede pasar")
else :
    print (f"usted no puede pasar")