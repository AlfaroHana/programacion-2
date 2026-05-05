import math

def area_circulo(r):
    resultado = math.pi * (r**2)
    return resultado

radio = int(input("Ingresa el radio del circulo: "))
print("area del radio", radio, "=", area_circulo(radio))