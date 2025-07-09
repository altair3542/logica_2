# ciclo while y controles de flujo

# comprender y aplicar correctamente el ciclo while, ver sus diferencias con el ciclo for y las instrucciones de control de flujo que podemos usar con el... como break, continue y else.

# que es el ciclo while (mientras):

# while es un bucle que se ejecuta mientras una condicion sea VERDADERA, este es ideal cuando no sabemos cuantas veces se debe repetir una accion.

# contador = 1
# while contador <= 15:
#     print(f"1, 2, 3 por {contador}")
#     contador += 1

# Ejemplo 1.

# Leer numeros hasta que se ingrese un cero

# numero = int(input("Ingrese un numero (0 para salir)"))

# while numero != 0:
#     print(f"el numero ingresado fue: {numero}")
#     numero = int(input("Ingrese un numero (0 para salir)"))

# print("fin del programa")

# Ejemplo 2
# validacion de contraseña con un numero maximo de intentos.

# contraseña_correcta = "python123"
# intentos = 0
# acceso = False

# while intentos < 3:
#     ingreso = input("ingrese la contraseña: ")
#     if ingreso == contraseña_correcta:
#         acceso = True
#         break
#     intentos += 1

# if acceso:
#     print("Bienvenido, Sr. Stark")
# else:
#     print("Demasiados intentos incorrectos.")


# solicitar numeros y mostrar la suma total hasta que un usuario escriba 0

# suma = 0
# numero = int(input("Ingresa un numero (0 para terminar): "))

# while numero != 0:
#     suma += numero
#     print(suma)
#     numero = int(input("Ingresa un numero (0 para terminar): "))

# print(f"La suma total fue {suma}")

# Contar cuántos intentos tarda el usuario en adivinar un número secreto

# secreto = 15
# intentos = 0
# adivinanza = -1

# while adivinanza != secreto:
#     adivinanza = int(input("Adivina el numero entre 1 y 100: "))
#     intentos += 1

# print(f"Correcto, lo adivinaste en {intentos} intentos")

# import random

# secreto = random.randint(1, 10)
# intentos = 0
# adivinanza = -1

# while adivinanza != secreto:
#     adivinanza = int(input("Adivina el numero entre 1 y 10: "))
#     intentos += 1

# print(f"Correcto, lo adivinaste en {intentos} intentos")


import random
import string

letra = random.choice(string.ascii_letters)
print(f"letra aleatoria {letra}")
