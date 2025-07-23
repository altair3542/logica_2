# 🧠 Sesión 7: Aplicaciones integradoras con menú

# Aplicar todo lo aprendido durante el curso (ciclos, condicionales, contadores, acumuladores, estructuras anidadas y control de flujo) para construir aplicaciones completas con menú interactivo.

# Esta sesión se enfoca en la integración de conocimientos en ejercicios funcionales con menús, entradas dinámicas y múltiples opciones.

# Agenda de contactos simple que maneje una busqueda y un listado.

# agenda = {}

# while True:
#     print("\n--- Agenda de contactos ---")
#     print("1. Agregar contacto")
#     print("2. Buscar contacto")
#     print("3. Listar contactos")
#     print("4. Salir")
#     opcion = input("Selecciona una opcion: ")

#     if opcion == "1":
#         nombre = input("Nombre: ")
#         telefono = input("Telefono: ")
#         agenda[nombre] = telefono
#         print("Contacto agregado")
#     elif opcion == "2":
#         contacto = input("Nombre a buscar: ")
#         if contacto in agenda:
#             print(f"Telefono: {agenda[nombre]}")
#         else:
#             print("Contacto no encontrado")
#     elif opcion == "3":
#         print("--- Lista de Contactos ---")
#         for nombre, telefono in agenda.items():
#             print(f"{nombre}: {telefono}")
#     elif opcion == "4":
#         print("Saliendo de la agenda")
#         break
#     else:
#         print("Opcion invalida.")

agenda = {}

while True:
    print("\n--- AGENDA DE CONTACTOS ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Listar contactos")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        agenda[nombre] = telefono
        print("Contacto agregado.")
    elif opcion == "2":
        nombre = input("Nombre a buscar: ")
        if nombre in agenda:
            print("Teléfono:", agenda[nombre])
        else:
            print("Contacto no encontrado.")
    elif opcion == "3":
        print("--- Lista de contactos ---")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")
    elif opcion == "4":
        print("Saliendo de la agenda.")
        break
    else:
        print("Opción inválida.")
