frase=input("Ingresa la oración: ") #
resultado=""
desp=int(input("Ingrese de cuánto en cuánto es su desplazamiento (número entero positivo): "))

for caracter in frase:
    if caracter.isalpha():
        
        if caracter.islower():
            limite=ord('z')
            inicio=ord('a')
        else:
            limite=ord('Z')
            inicio=ord('A')
            
        
        valor=ord(caracter)+desp
        if valor>limite:
            valor-= 26
        resultado+=chr(valor)
    else:
        
        resultado+=caracter

print(resultado)