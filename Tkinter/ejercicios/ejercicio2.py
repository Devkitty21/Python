# Ejercicio 1: Conversor de Temperatura
# Crea una aplicación que convierta temperaturas entre Celsius y Fahrenheit.
#
# 📌 Requisitos:
#
# Un campo de entrada donde el usuario ingrese la temperatura.
# Dos botones: uno para convertir de Celsius a Fahrenheit y otro de Fahrenheit a Celsius.
# Una etiqueta que muestre el resultado de la conversión.
# Ejercicio 2: Lista de Compras
# Crea una interfaz donde el usuario pueda agregar elementos a una lista de compras.
#
# 📌 Requisitos:
#
# Un Entry donde el usuario escriba el nombre del producto.
# Un botón para agregar el producto a la lista.
# Un Listbox donde se muestren los productos agregados.
# Un botón para eliminar un elemento seleccionado de la lista.


import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title('Conversor de Grados a Fahrenheit')
ventana.iconbitmap('C:\\Users\\vieir\\PycharmProjects\\Tkinter\\icono.ico')
ventana.geometry('600x400')
ventana.resizable(0,0)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)

# Creamos un frame como si fuera el titulo
frame1_campo = tk.LabelFrame(ventana, text='Convertidor', bg='#eee')
frame1_campo.grid(row=0, column=0, columnspan=2, sticky='ew',padx=20, pady=10)

# Creamos el campo de entrada
texto_entrada = tk.Entry(frame1_campo, width=35, font=('Cascadia Code', 10))
texto_entrada.grid(row=1, column=0, padx=5, pady=20)

# Creamos otro frame
frame2_botones = tk.LabelFrame(ventana, text='Botones', bg='#eee')
frame2_botones.grid(row=1,column=0, columnspan=2, sticky='we',padx=20, pady=10)

def grados():
    try:
        # Obtener el valor del campo de entrada
        celsius = float(texto_entrada.get())

        # Realizar la conversión
        fahrenheit = (celsius * 9 / 5) + 32

        # Mostrar el resultado en la etiqueta
        messagebox.showinfo('Conversion Exitosa!',f'{celsius} grados, son {fahrenheit:.2f} Fahrenheit')

    except Exception as error:
        messagebox.showerror('Conversion Erronea',f'Se ha producido un error: {error}, {type(error)}')

def fahrenheit():
    try:
        faren = float(texto_entrada.get())
        celsius = (faren - 32) * 5/9
        messagebox.showinfo('Conversion Exitosa',f'{faren} fahrenheits, son {celsius:.2f} grados')

    except Exception as error:
        messagebox.showerror('Conversion Erronea',f'Se ha producido un error: {error}, {type(error)}')

# Creamos dos botones
boton1 = tk.Button(frame2_botones, text='Grados', bd=1,width=15, font=('Cascadia Code',10), height=2, command=grados)
boton1.grid(row=0, column=0, padx=10,pady=10)
boton2 = tk.Button(frame2_botones, text='Fahrenheit', bd=1, width=15, font=('Cascadia Code',10),height=2,command=fahrenheit)
boton2.grid(row=0, column=1, padx=10,pady=10)

ventana.mainloop()



