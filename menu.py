from usuarios import menu_usuarios
from historial import menu_historial
from configuracion import menu_configuracion

def menu_principal():
    while True:
        print("==== MENU PRINCIPAL ====")
        print("1. Usuarios")
        print("2. Historial")
        print("3. Configuracion")
        print("4. Salir")

        opcion = input("Opcion: ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 4:
                if opcion == 1:
                    menu_usuarios()
                elif opcion == 2:
                    menu_historial()
                elif opcion == 3:
                    menu_configuracion()
                else:
                    print("Has salido...")

            else: 
                print("Error: Opcion invalida")

        else:
            print("Error: No has ingresado un numero entero")

        
