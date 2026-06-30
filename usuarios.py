usuarios = []
def menu_usuarios():
    while True:
        print("==== USUARIOS ====")
        print("1. Registrar")
        print("2. Modificar")
        print("3. Eliminar")
        print("4. Buscar")
        print("5. Ver todos")
        print("6. Volver")

        opcion = input("Opcion: ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 6:
                if opcion == 1:
                    registrar_usuarios()
                elif opcion == 2:
                    modificar_usuarios()
                elif opcion == 3:
                    eliminar_usuarios()
                elif opcion == 4:
                    buscar_usuarios()
                elif opcion == 5:
                    ver_todos_usuarios()
                else:
                    print("Has vuelto...")
                    return
            else:
                print("Error: Opcion invalida")
        else: 
            print("Error: No has ingresado un numero entero")

def registrar_usuarios():
    usuario = {}
    print("==== REGISTRAR USUARIO ====")
    while True:
        documento = input("Documento: ")
        if documento.isdigit() and 6 <= len(documento) <= 10:
            break
        else: 
            print("Error: Documento invalido")

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")

    while True:
        telefono = input("Telefono: ")
        if telefono.isdigit() and len(telefono) == 10:
            break
        else:
            print("Error: Telefono invalido")

    usuario["documento"] = documento
    usuario["nombre"] = nombre
    usuario["apellido"] = apellido
    usuario["telefono"] = telefono
            
    usuarios.append(usuario)

    print(f"==== USUARIO AGREGADO ===="
            f"\nDocumento: {usuario['documento']}"
            f"\nNombre: {usuario['nombre']}"
            f"\nApellido: {usuario['apellido']}"
            f"\nTelefono: {usuario['telefono']}")
        

def modificar_usuarios():
    while True:
        if len(usuarios) > 0:
            print("==== MODIFICAR USUARIOS ====")
            for i, usuario in enumerate(usuarios, start = 1):
                print(f"{i}. Documento: {usuario['documento']} Nombre: {usuario['nombre']} Apellido: {usuario['apellido']} Telefono: {usuario['telefono']}")
            
            opcion = input("Opcion: ")

            if opcion.isdigit():
                opcion = int(opcion)
                if 1 <= opcion <= len(usuarios):

                    seleccionar_usuario_modificar(opcion)

                else:
                    print("Error: Opcion invalida")
            else:
                print("Error: No has ingresado un numero entero")
        else:
            print("Error: Aun no hay usuarios")
            return
def seleccionar_usuario_modificar(indice):
    seleccionado = usuarios[indice - 1]
    for i, campo in enumerate(seleccionado, start = 1):
        print(f"{i}. {campo}")
    editar = input("Opcion: ")
    if editar.isdigit():
        editar = int(editar)
        if 1 <= editar <= 4:
            if editar == 1:
                while True:
                    nuevo_documento = input("Nuevo documento: ")
                    if nuevo_documento.isdigit() and 6 <= len(nuevo_documento) <= 10:
                        seleccionado['documento'] = nuevo_documento
                        mostrar_usuario(seleccionado)
                        break
                    else:
                        print("Error: Documento invalido")
            elif editar == 2:
                nuevo_nombre = input("Nuevo nombre: ")
                seleccionado['nombre'] = nuevo_nombre
                mostrar_usuario(seleccionado) 
                
            elif editar == 3:
                nuevo_apellido = input("Nuevo apellido: ")
                seleccionado['apellido'] = nuevo_apellido
                mostrar_usuario(seleccionado)
            else:
                while True:
                    nuevo_telefono = input("Nuevo telefono: ")
                    if nuevo_telefono.isdigit() and len(nuevo_telefono) == 10:
                        seleccionado['telefono'] = nuevo_telefono
                        mostrar_usuario(seleccionado)
                        break
                    else:
                        print("Error: Telefono invalido")
        else:
            print("Error: opcion invalida")
    else:
        print("Error: No has ingresado un numero entero")

def mostrar_usuario(usuario):
    print("==== USUARIO ====")
    print(f"\nDocumento: {usuario['documento']}"
        f"\nNombre: {usuario['nombre']}"
        f"\nApellido: {usuario['apellido']}"
        f"\ntelefono: {usuario['telefono']}")



def eliminar_usuarios():
    if len(usuarios) == 0:
        print("Aun no hay usuarios")
        return
    
    for i, usuario in enumerate(usuarios, start = 1):
        print(f"{i}. Documento: {usuario['documento']} Nombre: {usuario['nombre']} Apellido: {usuario['apellido']} Telefono: {usuario['telefono']}")
    try:
        opcion = int(input("Opcion: "))
        if 1 <= opcion <= len(usuarios):
            seleccionado = usuarios[opcion - 1]
            mostrar_usuario(seleccionado)
                     
            print("¿Seguro que lo eliminaras?")
            print("1. Si")
            print("2. No")
            try:
                confirmar = int(input("opcion: "))
                if 1 <= confirmar <= 2:
                    if confirmar == 1:
                        usuarios.pop(opcion - 1)
                        print("Se ha eliminado con exito")
                        return
                            
                    elif confirmar == 2:
                        print("Cancelado")
                        return

                else:
                    print("Error: opcion invalida")
                                
                        
            except ValueError:
                print("Error: opcion invalida")
        else:
            print("Error: opcion invalida")

    except ValueError:
        print("Error: opcion invalida")


        
def buscar_usuarios():
    pass
def ver_todos_usuarios():
    pass
