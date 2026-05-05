caramelos=int(input("ingresa cuantos caramelos hay: "))
estudiantes=int(input("ingresa cuántos estudiantes hay: "))

caramelos_estudiantes= caramelos//estudiantes
sobra= caramelos%estudiantes

print("A cada estudiante le corresponden ", caramelos_estudiantes," caramelos")

print("sobran ", sobra, "caramelos")