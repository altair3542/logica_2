# Contadores y acumuladores en python, donde y como usuarlos

# comprender, diferenciar y aplicar contadores y acumuladores en estructuras repetitivas para resolver problemas practicos relacionados con cantidades, totales, promedios y clasificaciones.

# Que es un contador...

# Un contador incrementa su valor en al menos una unidad cada vez que se cumple una condicion...

# contador = 0
# letras = input("ingresa la cadena a evaluar: ")
# for letra in letras:
#     if letra == "a":
#         contador += 1
# print(f"La cantidad de letras 'a' en la palabra proporcionada es {contador}")


# que es un acumulador:

# suma valores o los va acumulando en cada iteracion, no necesariamente en pasos de 1

# numeros = [5, 8, 3]
# suma = 0
# for n in numeros:
#     suma += n
# print(f"el total de esta suma fue: {suma}")

# Ejercicios:

# calcular un promedio de n notas...

# n = int(input("Cuantas notas vas a agergar?: "))
# suma = 0

# for i in range(n):
#     nota = float(input(f"Ingrese la nota {i+1}: "))
#     suma += nota

# promedio = suma / n
# print(f"El promedio de notas es: {promedio}")

# ejercicio 2: Contar cuantos numeros pares e impares hay en una lista:

numeros = [3, 4, 6, 7, 10, 13, 18]
pares = 0
impares = 0

for n in numeros:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"en la lista hay {pares} numeros pares")
print(f"en la lista hay {impares} numeros impares")

# ejercicio 4

# dado un numero por el usuario, vamos a imprimir los numeros del 1 hasta donde diga el usuario pero con las siguientes condiciones...
# si el numero es multliplo de 3 debes imprimir "fizz" en vez del numero
# si el numero es multiplo de 5 debes imprimir "fuzz" en vez del numero
# si el numero es multiplo de 3 y de 5 al mismo tiempo debes imprimir "FizzFuzz"


n = int(input("Hasta que numero queres contar pues ome?: "))

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzFuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Fuzz")
    else:
        print(i)
