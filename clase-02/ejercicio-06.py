# Crear un programa de presentacion en un archivo llamado tp1.py y definir las siguientes variables:
#     Una variable con tu nombre.
#     Una variable con tu edad.
#     Una variable con tu altura aproximada en metros.
#     Una variable booleana que indique si te gusta programar.
#     Una variable que, a partir del anio actual y tu edad, calcule tu anio de nacimiento aproximado.
# Luego, imprimir toda esa informacion utilizando print().
nombre = "damian de la guarda"
edad = int(32)
altura = float(1.70)
programar = "me gusta programar" == "me gusta programar"
anio_actual = int (2026)
nacimiento = int (edad + anio_actual)

print (f"Mi nombres es {nombre}")
print (f"mi edad es {edad} y estamos en el año {anio_actual} ")
print (f"mi año de nacimiento es {(anio_actual - edad)}")
print (f"¿es verdad que me gusta programar ?{programar}")