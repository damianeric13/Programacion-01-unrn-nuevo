
# print (type(lista_super))
# print(lista_super)
lista_super=["huevos",
             "pan",
             "coca",
             "azucar",
             "leche",
             "fideos"
             ]
lista_vacia=[]
# #for indice in range(int(input("ingrese numero:"))):
# for indice in range(len(lista_super)):
#  #   print(indice)
#   #  print(lista_super[indice])
#     print(f"{indice}: {lista_super[indice]}")

indice = 0
while indice < len(lista_super):
    print(indice, lista_super[indice])
    indice +=1
while True:
    indice_seleccionado= int(input("elegi la comida:"))
    if indice_seleccionado< len(lista_super):
        comida= lista_super[indice_seleccionado]
        print(f"elegiste el indice {indice_seleccionado}:{comida}")
    else:
        print("elegiste una comida invalida")