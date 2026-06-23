matriz= [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]
suma= 0
multi= 1

for i in range(4):
    for j in range(4):
        if(i==j): # esto está preguntando si la columna y la filas  son iguales. 
           suma=suma+matriz[i][j] # acumulador. se van a guardar y sumar las filas y columnas? 
           multi=multi*matriz[j][i] 
               
print("la suma es: ", suma)
print("La multiplicación es: ", multi)

matriz= [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]
suma= 0
multi= 1

for i in range(4):
    for j in range(4):
        if(i+j==3):#Esto se hace porque la suma entre la fila y las columnas de la otra diagonal da tres. Entonces hay que preguntar si la suma de ambos da tres :D   
           suma=suma+matriz[i][j] 
           multi=multi*matriz[j][i] 
               
print("(otra diagonal) la suma es: ", suma)
print("(otra diagonal) La multiplicación es: ", multi)





