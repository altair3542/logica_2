# El ciclo For

# dominar el uso del ciclo for para iterar sobre rangos, listas, cadenas y tuplas. aprender a usar contadore y acumuladores tanto dentro como por fuera del bucle.

# que es for.

#un ciclo que permite recorrer secuencias o estructuras que son iterables (listas o arreglos, strings, tuplas, diccionarios, rangos, etc.)

# for elemento in secuencia:
    #el codigo  que se debe ejecutar repetidamente.



# que es un rango...
# un rango es una lista de items que esta acotada tanto en principio como en fin, usualmente numerico


for i in range(1, 6):
    print(f"Hola soy el {i}")

#un rango originalmente puede tener 3 parametros, de los cuales solo el final del rango es obligatorio.

# range(inicio, fin)
# range(10, -10, -2)
for i in range(10, -11, -2):
    print(f"Hola soy el {i}, pero en reversa")

for cuenta in range(0,1001, 10):
    print(cuenta)


nombres = ["Ana", "Luis", "Marta"]
print(nombres)
for nombre in nombres:
    print(f"hola, {nombre}. ¿Como estas?")


print(f"hola, {nombres[1]}. Como estas?")

#cadenas
palabra = "Python"
print(palabra)
cosas = ["p","y","t","h","o","n"]

for letra in palabra:
    print(letra)

for cosa in cosas:
    print(cosa)

# Una tupla es una colección de objetos ordenados que encierra sus elementos con paréntesis () y los separa con comas. Las tuplas son muy similares a las listas, y pueden almacenar objetos de tipo distinto como enteros y strings entre otros. Sin embargo, al contrario que las listas presentan la propiedad de inmutabilidad. Esto implica que los elementos de una tupla no pueden reasignarse.

coordenada = (4, 7, 2)
for valor in coordenada:
    print(f"Valor de la coordenada: {valor}")

    
