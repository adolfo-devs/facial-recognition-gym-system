def menu_historial():
    print("==== HISTORIAL ====")
    print("1. Registrar entrada")
    print("2. Ver historial")
    print("3. Buscar")
    print("4. Volver")

    opcion = input("Opcion: ")

    if opcion.isdigit():
        opcion = int(opcion)
        if 1 <= opcion <= 4:
            if opcion == 1:
                registrar_entrada_historial()
            elif opcion == 2:
                ver_historial()
            elif opcion == 3:
                buscar_historial()
            else:
                print("Has vuelto...")
                return
        else:
            print("Error: Opcion invalida")

    else:
        print("Error: No has ingresado un numero entero")

def registrar_entrada_historial():
    pass
def ver_historial():
    pass
def buscar_historial():
    pass