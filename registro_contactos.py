# Tarea Semana 15: Funciones, Colecciones y Archivos
# Registro de contactos utilizando un diccionario

# Diccionario para almacenar los contactos
contactos = {}


# Función para agregar un contacto
def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")

    contactos[nombre] = telefono
    print("Contacto agregado correctamente.")


# Función para mostrar todos los contactos
def mostrar_contactos():
    if len(contactos) == 0:
        print("No hay contactos registrados.")
    else:
        print("\n LISTA DE CONTACTOS ")
        for nombre, telefono in contactos.items():
            print("Nombre:", nombre, "| Teléfono:", telefono)


# Función para buscar un contacto
def buscar_contacto():
    nombre = input("Ingrese el nombre que desea buscar: ")

    if nombre in contactos:
        print("Contacto encontrado.")
        print("Nombre:", nombre)
        print("Teléfono:", contactos[nombre])
    else:
        print("El contacto no existe.")


# Programa principal
while True:
    print("\n REGISTRO DE CONTACTOS ")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_contacto()

    elif opcion == "2":
        mostrar_contactos()

    elif opcion == "3":
        buscar_contacto()

    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")