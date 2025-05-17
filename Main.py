def mostrar_menu():
    print("\n--- Menú del Taller ---")
    print("1. Ingresar Cliente")
    print("2. Ver Clientes")
    print("3. Agregar Equipo")
    print("4. Ver Equipos por Cliente")
    print("5. Salir")

def ejecutar_programa():
    taller = Taller()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            apellidos = input("Apellidos del cliente: ")
            nombres = input("Nombres del cliente: ")
            telefono = input("Teléfono del cliente: ")
            taller.ingresar_cliente(apellidos, nombres, telefono)

        elif opcion == "2":
            taller.ver_clientes()

        elif opcion == "3":
            cliente_nombres = input("Nombre del cliente: ")
            numero_parte = input("Número de parte del equipo: ")
            tipo = input("Tipo de equipo (ej. teléfono, portátil, PC): ")
            descripcion = input("Descripción del problema: ")
            taller.agregar_equipo(numero_parte, tipo, descripcion, cliente_nombres)

        elif opcion == "4":
            cliente_nombres = input("Nombre del cliente: ")
            taller.ver_equipos_por_cliente(cliente_nombres)

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")
