# Diseñar un algoritmo que indique qué ropa usar según la temperatura.
# Dato:
#     temperatura
# Condiciones:
#     Menor a 10: abrigo
#     Entre 10 y 20: ropa media
#     Mayor a 20: ropa liviana
# Escribir los pasos en forma clara y ordenada.
temperatura = int(input("ingrese temperatura: "))
if temperatura < 10:
    print (f"esta fresco ponete abrigo")
elif (temperatura >10) and (temperatura < 20):
    print (f"esta lindo pero ponete ropa media")
else:
    print (f"esta re lindo sali asi nomas")