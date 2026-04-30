# Diseñar un programa que genere un número aleatorio entre 1 y 20. El jugador tiene 6 intentos.
# Si el número secreto es mayor o menor al número ingresado. Si es igual el jugador gana.

import random
secreto= random.randint(1,20)
intentos=6

print("Tenés 6 intentos para adivinar el número")

for i in range (1,6+1):
    intento=int(input("Ingresa un número "))

    if intento<secreto:
        print("Mayor")
    elif intento>secreto:
        print("Menor")
    else:
        print("Adivinaste el número ")
        break   
else:
    print("Perdiste. El número era ", secreto)