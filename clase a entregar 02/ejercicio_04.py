archivo= open("temperaturas.txt", "r")

diccionario={}
for linea in archivo:
    lineas=linea.split(";")
    ciudad=lineas[0]
    temperatura=lineas[1]
    if ciudad not in diccionario:
        diccionario[ciudad]=[]    
    diccionario[ciudad].append(temperatura)
archivo.close()
print(diccionario)

