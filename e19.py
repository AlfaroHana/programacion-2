#Los argumentos que tienen el igual son opcionales y pueden ir en cualquier orden. Los que no los tienen son obligatorios.
#Clase: Tipo de variable definida por una biblioteca

import tkinter as tk
import random

 
secreto= random.randint(1,20)
app=tk.Tk() #Variable de clase TK
resultado=tk.StringVar(app) #Se usan para mostrarse en Tkinter
entrada=tk.StringVar(app)
vidas=6
vidasSV=tk.StringVar(app)

vidasSV.set("vidas:" + str(vidas))

def intentar():
    global vidas
    if(vidas<=0):
        resultado.set("Perdiste... TT ¡Intentalo de nuevo! :D")
        return
    vidas= vidas-1
    vidasSV.set("vidas:" + str(vidas))

    numero= int(entrada.get())
    
    
    if(numero<secreto):
        resultado.set("Ingresa un número más grande :b")
    if(numero>secreto):
        resultado.set("Ingresa un número más pequeño :b")
    if(numero==secreto):
        resultado.set("¡Ganaste! Felicitaciones :D")
    
    

app.geometry("500x500") #ancho por alto, para el tamaño


app.configure(background="beige") #Color de fondo. App=variable 

tk.Wm.wm_title(app, "¡Adivina el número!") #Titulo

tk.Label(app, text="¡Adivina el número entre el 1 y 20!", font= ("Century Gothic", 20), bg= "#F4A261", fg= "black", justify="center").pack(fill= tk.BOTH)

tk.Label(app, text="vidas: ",textvariable=vidasSV, font= ("Trebuchet MS", 20), bg= "#FDF6EC", fg= "black", justify="center").pack(fill= tk.BOTH, expand= False)

tk.Entry(app, fg= "black", bg="#F4A261", justify="center", textvariable= entrada, font=("Arial",20), width=10 ).pack(pady=10)

tk.Button(app, text= "¡Intenta!", bg= "#E76F51", fg= "black", font=("Arial", 16), command= intentar, ).pack(fill= tk.BOTH)

tk.Label(app, textvariable=resultado, font= ("Trebuchet MS", 20), bg= "#FDF6EC",fg= "black", justify="center").pack(fill= tk.BOTH, expand= True)





app.mainloop() #Refresca continuamente lo que está en la pantalla  pady= Sirve para el tamaño del entry width= Sirve para la cantidad de caracteres que se puede ingresar