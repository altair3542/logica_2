# #que es un cilco o un bucle en progrmacion?

# # un bucle (o ciclo) es una estructua de control que permite
# # repetir una o varias veces instrucciones multiples hasta que se cumpla una condicion.

# # esto evita repetir codigo manualmente y nos permite procesar datos en lote, automatizar tareas, recorrer listas etc.


# #como se ejecutan?

# # las ejecuciones del codigo pueden ser de dos formas:

# # Secuencial: en esta se ejecuta una instruccion tras otra sin repetir:
# print("hola")
# print("mundo")

# # repetitiva:
# # ejecuta un bloque de codigo o instrucciones varias veces bajo una condicion.

# print("ejecucion secuencial")
# print("Hello, how are you")
# print("Hello, how are you")
# print("Hello, how are you")
# print("Hello, how are you")
# print("Hello, how are you")

# print("ejecucion repetitiva")
# for i in range(5):
#     print("hello, how are you?")

# # Tipos de ciclo en python

# # ciclo for:
# # repite un bloque un numero de veces determinado (cuando conocemos cuantas veces hay que repetirlo.)

# for i in range(10):
#     print(i)

# # Ciclo while:
# # repite un bloque mientras una condicion se mantenga verdadera

# contador = 0

# while contador < 5:
#     print("1, 2, 3 por castro")
#     contador +=1


# # simulacion de do...while

# # python no tiene esta estructura directamente, pero se puede simular con un while True y un break.

# while True:
#     dato = input("escribir 'salir' para terminar")
#     if dato == "salir":
#         break


# #cuando se que bucle debo usar...

# # for lo uso cuando se la cantidad de repeticiones que debo hacer

# # while lo uso cuando no estoy seguro de cuantas veces lo debo repetir, pero depende de una unica condicion que puede cambiar.

# # do...while (simulado): necesitamos ejecutar el bloque al menos una vez, y luego evaluar la condicion para cerrar el ciclo.


# # Ejercicios
# # imprimir los numeros del 1 al 100

# for num in range(1, 101):
#     print(num)

#ejemplo 2
# repetir un mensaje N numero de veces

n = int(input("Oiste, vos cuantas veces vas a cosiampirar esta cosiampiradera?: "))
for i in range(n):
    print("Ese cosiampiro")
