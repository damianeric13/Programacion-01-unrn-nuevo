# Escribir un programa que determine si un número es:
#     Par o impar
#     Mayor, menor o igual a 10
numero = int(input("ingrese numero:"))
if numero % 2 == 0: 
    print (f"el numero {numero} es par")
else:
    print(f"el numero {numero} es impar")
if numero < 10:
    print(f"el numero {numero} es menor a 10")
elif numero == 10:
    print(f"el numero {numero} es igual a 10")
else:
    print(f"el numero {numero} es mayor a 10")