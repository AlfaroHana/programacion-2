from PIL import Image  
import matplotlib.pyplot as plt
import numpy as np

Imagen= Image.open("kei.jpg") 
m= np.array(Imagen)       
dimensiones= np.shape(m)
grises= np.zeros((dimensiones[0], dimensiones[1]))

for i in range(dimensiones[0]):
    for j in range(dimensiones[1]): 
        grises[i][j]= int(m[i][j][0]*0.2989 + m[i][j][1]*0.5870 + m[i][j][2]*0.1140)
        
plt.imshow(grises, cmap="gray")
plt.show()