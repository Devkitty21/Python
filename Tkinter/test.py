import tkinter as tk

root = tk.Tk()

# Botón sin borde
boton1 = tk.Button(root, text="Sin borde", bd=0, bg="lightgray")
boton1.pack(pady=10)

# Botón con borde de 5 píxeles
boton2 = tk.Button(root, text="Con borde", bd=5, bg="lightgray")
boton2.pack(pady=10)

root.mainloop()