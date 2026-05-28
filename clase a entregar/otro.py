# codigo="pfd312"
# letras=""
# numeros=""
# for c in codigo:
#     if c.isnumeric():
#         numeros = numeros + c
#     elif c.isalpha():
#         letras = letras + c
# if (len(letras)) == 3 and (len(numeros)) == 3:
codigo=input("ingrese su codigo de materia.\nejemplo;prog-101\nIngrese el suyo:")
lista_de_codigo=[]
lista_de_codigo=codigo.split("-")
lista_de_codigo[0].isalpha

if lista_de_codigo[0].isalpha() and lista_de_codigo[1].isnumeric() and codigo.count("-") == 1:
    print(lista_de_codigo[0].upper()+"-"+lista_de_codigo[1])
else:
    print("error usted no siguio las intruciones")