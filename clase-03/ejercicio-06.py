#Usar un for para imprimir una tabla simple de multiplicar del 2.
numero = int(input("ingrese n° de tabla:"))

for i in range (1 , 11):
    print(f"{i}x{numero}={i * (numero)}")