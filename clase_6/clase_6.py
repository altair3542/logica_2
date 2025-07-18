# Sesion 6: estructuras repetitivas anidadas.

# objetivo: comprender y aplicar ciclos dentro de ciclos para resolver problemas como la generacion de tablas de datos, impresion de patrones y simulacion de menus y submenus.

# que es un ciclo anidado:

# es un ciclo que en cada repeticion, ejecuta un ciclo internamente...

# for i in range(3):
#     for j in range(2):
#         print(f"este es el ciclo {i}, que ejecuta la repeticion {j}")

# tipos de anidacion mas comunes...

# tipo anidacion

# for dentro de for:
# para crear una tabla de datos, como las de multiplicar.

# for dentro de while:
# Menus con opciones dinamicas

# while dentro while:
# juegos o ciclos con validacion continua.


# live coding...

# ejemplo 1: tablas de multiplicar del 1 al 10.

# for i in range(1,2):
#     print(f"\nTabla del {i}")
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")

# Ejemplo 2

# n = int(input("Ingrese el tamaño de la matriz: "))

# for i in range(n):
#     for j in range(n):
#         print("*", end = " ")
#     print()


# ejemplo 3 un triangulo de numerales:
# filas = int(input("Cuantas filas quieres: "))

# for i in range(1, filas + 1):
#     for j in range(i):
#         print("#", end = " ")
#     print()

# ejemplo 4: simular un menú con sub menus

while True:
    print("\n---menu principal---")
    print("1. Operaciones")
    print("2. Información")
    print("3. Salir")
    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        while True:
            print("\n---submenu principal---")
            print("a. Sumar")
            print("b. Restar")
            print("c. Volver")
            subopcion = input("Seleccione una subopcion: ")

            if subopcion == "a":
                print("Resultado de 2 + 2 = ", 2 + 2)
            elif subopcion == "b":
                print("Resultado de 14 - 1 = ", 14 - 1)
            elif subopcion == "c":
                break
            else:
                print("opcion invalida")

    elif opcion == "2":
        print("Hecho con 🧠 y ♥️ por el grupo de martes y jueves")

    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opcion invalida.")
