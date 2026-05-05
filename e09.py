def calcular_factorial():
    num = int(input("Ingresa un número entero positivo: "))
    
    if num < 0:
        print("El número debe ser positivo")
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial = factorial * i
        print("El factorial es ", factorial)


calcular_factorial()