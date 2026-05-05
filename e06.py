cantidad=int(input("ingresa cuanta cantidad deseas extraer: "))

mil=cantidad//1000
resto=cantidad%1000

doscientos=resto//200
no_extraido=resto%200

print("se extrajeron ", mil," billetes de $1000")
print("se extrajeron ", doscientos," billetes de $200")
print("No se pudo extraer: ", no_extraido)