import random

lista= ["Hana", "Mia", "Mile", "Zoe", "Uma", "Chino"]
orden= []

for i in range(len(lista)):
    posicion = random.randint(0, len(lista) - 1)
    orden.append(lista[posicion])
    del(lista[posicion])

print("Tienen que pasar:", orden)