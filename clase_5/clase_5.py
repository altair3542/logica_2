# Sesion 5: Ciclos con condiciones complejas

# Aprender a combinar bucles con condicionales complejos, usandos flags (booleanos) y aplicar multiples condiciones para controlar el flujo de la ejecucion.

# que es una condicion compleja?

# es una condicion que combina dos o mas expresiones logicas con operadores..

# and para que sea la sentencia completa verdadera todas las sentencias deben ser verdaderas

# or solo necesito una sentencia verdadera para que todo el statement sea verdadero.

# not niega el resultado de la sentencia...

# edad = int(input("Oe, dame tu edad: "))
# tiene_documento = False

# if edad >= 18 and tiene_documento:
#     print("puedes votar, ojo con 2026")


# banderas o flags.
# es una variable, booleana que puede ser definida directamente...  esta sirve para recordar si algo ha sucedido dentro de un bucle...

# encontrado = False
# for numero in [2, 4, 15, 7]:
#     if numero == 5:
#         encontrado = True

# if encontrado:
#     print("El numero 5 esta en el arreglo")
# else:
#     print("El numero no fue encontrado")

# numeros = [1, 3, 5, 10, 4]
# encontrado = False
# buscado = int(input("Dame un numero para buscar: "))

# for num in numeros:
#     if num == buscado:
#         encontrado = True
#         break

# if encontrado:
#     print(f"Se encontro el numero {buscado}")
# else:
#     print("Papi, no encontré nada... que falla...")

# leer numeros hasta encontrar tres negativos seguidos.

# negativos_seguidos = 0

# while negativos_seguidos < 3:
#     numero = int(input("ingrese un numero: "))
#     if numero < 0:
#         negativos_seguidos += 1
#     else:
#         negativos_seguidos = 0

# print("ya conte 3 negativos seguidos")

# usar un flag para detectar si hay numeros mayores a 100

# encontrado = False
# for i in range(5):
#     numero = int(input("Ingresa un numero: "))
#     if numero > 100:
#         encontrado = True

# if encontrado:
#     print("lo encontré en al menos una parte del ingreso")
# else:
#     print("nada pah")

#construccion de condiciones multiples y cuando usar un operador especifico.

# cuando usamos and?

# cuando en una validacion necesito que las condiciones a validar sean verdaderas para que el flujo continue.


# cuando usamos or:
# cuando solo necesitamos que una condicion se cumpla...

# cuando usamos NOT

# cuando necesito negar una condicion...


# if not activo:
#     print("cuenta suspendida")
