Ejercicio 1 — Estructuras de datos

Explicá con tus palabras la diferencia entre:

    Lista
    Tupla
    Conjunto
    Diccionario

Para cada estructura, indicá un ejemplo de situación donde podría resultar útil.
Ejercicio 2 — Registro de sensores

Dada la siguiente lista de tuplas:

mediciones = [
    ("temp", 18.5, "Aula 1"),
    ("humedad", 40, "Aula 1"),
    ("temp", 21.0, "Laboratorio"),
    ("presion", 1012, "Laboratorio"),
    ("humedad", 55, "Aula 2")
]

Cada tupla tiene el formato:

(tipo_medicion, valor, ubicacion)

Escribí un programa que:

    Cree un diccionario donde la clave sea la ubicación.
    Cada ubicación debe guardar una lista con sus mediciones.
    Cree un conjunto con todos los tipos de medición sin repetir.
    Muestre el diccionario final.
    Muestre el conjunto de tipos encontrados.

Ejercicio 3 — Base de datos de alumnos

Escribí un programa que:

    Pida al usuario el nombre de 4 alumnos.
    Valide que el nombre no esté vacío.
    Guarde los nombres válidos en una lista.
    Escriba los nombres en un archivo llamado alumnos.txt, un nombre por línea.
    Cierre el archivo.

Ejercicio 4 — Lectura de archivo

Se tiene un archivo llamado temperaturas.txt con el siguiente contenido:

Bariloche;12
Viedma;20
Roca;18
Bariloche;15

Escribí un programa que:

    Lea el archivo línea por línea.
    Separe cada línea usando split(";").
    Genere un diccionario donde:
        la clave sea la ciudad;
        el valor sea una lista de temperaturas registradas.
    Muestre el diccionario final.

Ejercicio 5 — Interpretación de código

Leer el siguiente código sin ejecutarlo:

def limpiar(texto):
    return texto.strip().capitalize()

def es_valido(nombre):
    if len(nombre) >= 3:
        return True
    return False

nombres = [" bart ", "ED", " walter", "rick "]
validos = []

for nombre in nombres:
    nombre_limpio = limpiar(nombre)

    if es_valido(nombre_limpio):
        validos.append(nombre_limpio)

print(validos)

Responder:

    ¿Qué hace el programa?
    ¿Qué hace la función limpiar?
    ¿Qué hace la función es_valido?
    ¿Qué nombres quedan almacenados en validos?
    ¿Qué imprime el programa al finalizar?

