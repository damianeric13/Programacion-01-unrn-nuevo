# Ejercicio 4 - Edad valida
# Pedir una edad por teclado. Antes de usarla como numero, 
# revisar que el dato tenga sentido.
# El programa tiene que aceptar edades numericas 
# entre 0 y 120. Si la persona escribe espacios de mas,
# el programa deberia poder limpiarlos antes de validar.
# Si el dato sirve, mostrar algo como:
# Edad registrada: 25
# Si no sirve, mostrar un mensaje de error claro. No alcanza con que el programa se rompa.
def edad_valida():
    edad= input("por favor ponga su edad:")
    edad_corregida="".join(edad.split())
    if edad_corregida.isnumeric() and int(edad_corregida)< 120 and int(edad_corregida)> 0:
        print(f"edad registrada:{edad_corregida}")
    elif edad_corregida.isnumeric() and (int(edad_corregida)> 120 or int(edad_corregida)< 0):
        print(f"edad no registrada")
    else:
        print("por favor ingrese numeros no letras")
edad_valida()

