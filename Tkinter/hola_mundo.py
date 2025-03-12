import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu # Componentes de tkinter (Es lo comun para crear widgets)
# Tambien podemos crear botones usando tk

ventana = tk.Tk() #     Creamos un objeto de tipo tk
ventana.geometry('600x400')
ventana.title('Manejo de Componentes')
ventana.iconbitmap('icono.ico')


# Definimos una variable que podremos modificar posteriormente (set), leer(get)
entrada1 = ttk.Entry(ventana, width=30, state=tk.NORMAL)
entrada1.grid(row=0,column=0)

# Etiqueta (label)
etiqueta1 = tk.Label(ventana,text='Aqui se mostrara el contenido de la caja de texto')
etiqueta1.grid(row=1,column=0, columnspan=2)


# Definimos el metodo enviar
def enviar():
    etiqueta1.config(text=entrada1.get())
    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo('Mensaje Informativo', mensaje1 + ' Informativo')

def salir():
    ventana.quit()
    print('Salimos...')
    ventana.destroy()
    sys.exit()


def crear_menu():
    # Confiugurar el menu principal
    menu_principal = Menu(ventana)
    #tearoff = False para evitar que se separe el menu de la interfaz
    submenu_archivo = Menu(menu_principal,tearoff=False)
    # Agregamos una nueva opcion al menu de archivo
    submenu_archivo.add_command(label='Nuevo')
    # Agregamos un separador
    submenu_archivo.add_separator()
    # Agregamos la opcion de salir
    submenu_archivo.add_command(label='Salir', command=salir)
    #Agregamos el submenu al menu principal
    menu_principal.add_cascade(menu=submenu_archivo,label='Archivo')
    # Submenu ayuda
    submenu_ayuda = Menu(menu_principal,tearoff=False)
    # Agregamos una nueva opcion
    submenu_ayuda.add_command(label='Acerca De')
    # Agregamos al menu principal este nuevo submenu
    menu_principal.add_cascade(menu=submenu_ayuda,label='Ayuda')
    # Mostramos el menu en la ventana principal
    ventana.config(menu=menu_principal)

boton1 = ttk.Button(ventana,text='Enviar',command=enviar)
boton1.grid(row=0, column=1)


crear_menu() # Antes de que se despliegue la interfaz llamamos al metodo

ventana.mainloop()