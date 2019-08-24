if __name__ == '__main__':
    print('FONDA LA SABROSONA')
    print("------------------\n")

    cliente = input("Cliente: ")

    factura = []



    print('\nMENU')
    menu_lista = ['1. Mondongo\t$1.50', '2. Lengua\t$0.75', '3. Pata\t\t$2.00']
    for comida in menu_lista:
        print(comida)

    while True:


        try:
            opcion = int(input("Opcion: "))
        except:
            opcion = -1

        if opcion == 1:

            precio = 1.5
            comida = "mondongo"
            print("Cuantas ordenes de ", comida, "deseas ?")
            cantidad = int(input())
            factura.append(comida)
            break
        elif opcion == 2:
            precio = 0.75
            comida = "lengua"
            print("Cuantas ordenes de ", comida, "deseas ?")
            cantidad = int(input())
            factura.append(comida)
            break
        elif opcion == 3:
            precio = 2.0
            comida = "pata"
            print("Cuantas ordenes de ", comida, "deseas ?")
            cantidad = int(input())
            factura.append(comida)
            break
        else:
            print("Opcion invalida")

    total = precio * cantidad * 1.07

    pago = input("Pago? (S/N)")
    if pago.upper() == "S":
            for sel in factura:
                    print("Su seleccion fue: ", sel)
                    print("Usted debe pagar $" + str(total))

                    print("Gracias por preferirnos", ",", cliente)
    else:
            print('Pedido cancelado!!!')