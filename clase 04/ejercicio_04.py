opcion=""
total= 0

print("selecciona la comida para llevar, al terminar tu pedido para registrarlo pone:terminar pedido")
while opcion !="terminar pedido":
    opcion = input("escriba lo que quiera agregar al pedido:"). lower()
    if opcion == "pizza":
        total+= 25 
        print(f"Excelente! agregamos una {opcion} a tu pedido:")
    elif opcion == "empanadas":
        total+= 20
        print(f"Excelente! agregamos una {opcion} a tu pedido:")
    elif opcion == "hamburguesa":
        total+= 15
        print(f"Excelente! agregamos una {opcion} a tu pedido:")
    elif opcion == "terminar pedido":
        print("cerramos pedido")
        print(f"pedido finalizado,tu total es {total}, gracias por confiar en nosotros")
    else:
        print(f"lo siento, no tenemos {opcion}; prueba otra cosa")
        