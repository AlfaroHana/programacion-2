import tkinter as tk
from tkinter import ttk, messagebox

ABCD = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def cifrar_vigenere(mensaje, clave, descifrar=False):
    mensaje = mensaje.upper()
    clave = clave.upper()
    resultado = []
    
    # Filtrar solo letras válidas de la clave
    clave_limpia = [c for c in clave if c in ABCD]
    if not clave_limpia:
        return ""
    
    j = 0
    for char in mensaje:
        if char in ABCD:
            ind_men = ABCD.index(char)
            ind_cla = ABCD.index(clave_limpia[j % len(clave_limpia)])
            
            if descifrar:
                ind_res = (ind_men - ind_cla) % len(ABCD)
            else:
                ind_res = (ind_men + ind_cla) % len(ABCD)
                
            resultado.append(ABCD[ind_res])
            j += 1
        else:
            resultado.append(char)
            
    return "".join(resultado)

def procesar(descifrar=False):
    msg = entry_mensaje.get()
    key = entry_clave.get()
    
    if not msg or not key:
        messagebox.showwarning("Atención", "Por favor ingresa tanto el mensaje como la clave.")
        return
        
    res = cifrar_vigenere(msg, key, descifrar=descifrar)
    
    entry_resultado.config(state="normal")
    entry_resultado.delete(0, tk.END)
    entry_resultado.insert(0, res)
    entry_resultado.config(state="readonly")

def copiar_resultado():
    texto = entry_resultado.get()
    if texto:
        root.clipboard_clear()
        root.clipboard_append(texto)
        messagebox.showinfo("¡Listo!", "Resultado copiado al portapapeles 📋")

# --- Paleta de colores ---
BG_COLOR = "#F4F1DE"        # Crema suave
CARD_BG = "#FFFFFF"         # Blanco puro
TEXT_MAIN = "#3D405B"       # Gris azulado oscuro
ACCENT_PRIMARY = "#E07A5F"  # Terracota suave
ACCENT_SECONDARY = "#81B29A"# Verde salvia
ACCENT_HOVER = "#F2CC8F"    # Miel cálido
FONT_FAMILY = "Segoe UI"

# Configuración principal
root = tk.Tk()
root.title(" Cifrado Vigenère ")
root.geometry("460x480")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# Contenedor central 
card = tk.Frame(root, bg=CARD_BG, bd=0, highlightthickness=0)
card.place(relx=0.5, rely=0.5, anchor="center", width=400, height=420)

# Título
lbl_title = tk.Label(
    card, text="Cifrado Vigenère", font=(FONT_FAMILY, 16, "bold"),
    bg=CARD_BG, fg=TEXT_MAIN
)
lbl_title.pack(pady=(25, 5))


# Campo: Mensaje
lbl_mensaje = tk.Label(card, text="MENSAJE", font=(FONT_FAMILY, 9, "bold"), bg=CARD_BG, fg=TEXT_MAIN)
lbl_mensaje.pack(anchor="w", padx=30)

entry_mensaje = tk.Entry(
    card, font=(FONT_FAMILY, 10), bg="#F8F9FA", fg=TEXT_MAIN,
    bd=1, relief="solid", highlightthickness=1, highlightbackground="#E9ECEF"
)
entry_mensaje.pack(fill="x", padx=30, pady=(4, 12), ipady=6)

# Campo: Clave
lbl_clave = tk.Label(card, text="CLAVE", font=(FONT_FAMILY, 9, "bold"), bg=CARD_BG, fg=TEXT_MAIN)
lbl_clave.pack(anchor="w", padx=30)

entry_clave = tk.Entry(
    card, font=(FONT_FAMILY, 10), bg="#F8F9FA", fg=TEXT_MAIN,
    bd=1, relief="solid", highlightthickness=1, highlightbackground="#E9ECEF"
)
entry_clave.pack(fill="x", padx=30, pady=(4, 15), ipady=6)

# Botones de Acción
frame_botones = tk.Frame(card, bg=CARD_BG)
frame_botones.pack(fill="x", padx=30, pady=5)

btn_cifrar = tk.Button(
    frame_botones, text="🔒 Cifrar", font=(FONT_FAMILY, 10, "bold"),
    bg=ACCENT_PRIMARY, fg="white", activebackground="#D06A4F", activeforeground="white",
    bd=0, cursor="hand2", command=lambda: procesar(descifrar=False)
)
btn_cifrar.pack(side="left", expand=True, fill="x", padx=(0, 5), ipady=6)

btn_descifrar = tk.Button(
    frame_botones, text="🔓 Descifrar", font=(FONT_FAMILY, 10, "bold"),
    bg=ACCENT_SECONDARY, fg="white", activebackground="#70A189", activeforeground="white",
    bd=0, cursor="hand2", command=lambda: procesar(descifrar=True)
)
btn_descifrar.pack(side="right", expand=True, fill="x", padx=(5, 0), ipady=6)

# Campo: Resultado
lbl_resultado = tk.Label(card, text="RESULTADO", font=(FONT_FAMILY, 9, "bold"), bg=CARD_BG, fg=TEXT_MAIN)
lbl_resultado.pack(anchor="w", padx=30, pady=(15, 0))

frame_res = tk.Frame(card, bg=CARD_BG)
frame_res.pack(fill="x", padx=30, pady=(4, 10))

entry_resultado = tk.Entry(
    frame_res, font=(FONT_FAMILY, 10, "bold"), bg="#F1F3F5", fg=ACCENT_PRIMARY,
    bd=1, relief="solid", highlightthickness=1, highlightbackground="#E9ECEF", state="readonly"
)
entry_resultado.pack(side="left", expand=True, fill="x", ipady=6)

btn_copiar = tk.Button(
    frame_res, text="📋", font=(FONT_FAMILY, 10),
    bg="#E9ECEF", fg=TEXT_MAIN, activebackground="#DEE2E6",
    bd=0, cursor="hand2", command=copiar_resultado
)
btn_copiar.pack(side="right", padx=(5, 0), ipady=4, ipadx=8)

root.mainloop()