lista_de_nombres=[]
for i in range(4):
    nombre= input("ingrese un nombre del alumno:")
    if nombre.isalpha():
        lista_de_nombres.append(nombre)
archivo = open("alumnos.txt", "w")  
for nombre in lista_de_nombres:
    archivo.write( nombre +"\n")
archivo.close()
   