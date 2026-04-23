# Crear un programa que:
#     Calcule cuantos meses viviste aproximadamente.
#     Calcule tu edad dentro de 10 anios.
#     Calcule el doble de tu altura.
#     Imprima los resultados con mensajes descriptivos.
edad = int(input("ingrese edad: "))
altura = float(input("ingrese altura: "))
meses = edad * 12
doble = altura * 2
futuro = edad + 10
print(f"Mi edad es {edad}, vivi {meses} meses y en 10 años voy a tener {futuro}")
print(f"Mi altura es {altura} y el doble es {doble}")