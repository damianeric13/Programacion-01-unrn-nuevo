mediciones = [
    ("temp", 18.5, "Aula 1"),
    ("humedad", 40, "Aula 1"),
    ("temp", 21.0, "Laboratorio"),
    ("presion", 1012, "Laboratorio"),
    ("humedad", 55, "Aula 2")
]
diccionario={}
tipos_mediciones=[]
for tipo_medicion, valor, ubicacion in mediciones:
    tipos_mediciones.append(tipo_medicion)
    mediciones_limpias=set(tipos_mediciones)
    if ubicacion not in diccionario:
        diccionario[ubicacion]=[]
    diccionario[ubicacion].append(valor)

print(diccionario)
print(mediciones_limpias)