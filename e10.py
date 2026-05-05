def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

c= float(input("Ingresa los grados Celsius: "))

fahrenheit= celsius_a_fahrenheit(c)
print(c, " grados Celsius equivalen a ", fahrenheit, " grados Fahrenheit")