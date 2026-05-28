# Ejercicio 5 - Codigo de materia
# Pedir al usuario un codigo de materia con este formato:
# PROG-101
# El programa tiene que validar que:
#     tenga un solo guion -;
#     la parte de la izquierda tenga solo letras;
#     la parte de la derecha tenga solo numeros.
# Si el codigo es valido, mostrarlo normalizado en mayusculas (metodo upper).
# Ejemplo:
# Codigo valido: PROG-101
# Si no es valido, mostrar un mensaje de error claro.
def codigo_de_materia():
    codigo=input("ingrese su codigo de materia.\nejemplo;prog-101\nIngrese el suyo:")
    lista_de_codigo=[]
    lista_de_codigo=codigo.split("-")
    lista_de_codigo[0].isalpha

    if lista_de_codigo[0].isalpha() and lista_de_codigo[1].isnumeric() and codigo.count("-") == 1:
        print(lista_de_codigo[0].upper()+"-"+lista_de_codigo[1])
    else:
        print("error usted no siguio las intruciones")
codigo_de_materia()