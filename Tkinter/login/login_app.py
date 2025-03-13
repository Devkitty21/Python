import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Login')
ventana.configure(background='#1d2d44')
# Grid de la ventana
ventana.columnconfigure(0, weight=1) # Sirve para definir como se expanden las filas y columnas
ventana.rowconfigure(0, weight=1) # Cuando la ventana cambia de tamanio

# Creamos un estilo
estilos = ttk.Style() # Creamos un objeto de tipo style
estilos.theme_use('clam') # Agregamos un theme com la funcion theme_use()
estilos.configure(ventana, background='#1d2d44', foreground='white',
                  fieldbackground='black') #
estilos.configure('TButton',background='#005f73')
estilos.map('TButton',background=[('active','#0a9396')])

# Agregamos un frame (Es como un contenedor invisible)
frame = ttk.Frame(ventana)
frame.columnconfigure(0, weight=1) # Aqui indicamos que la columna 0 tiene el peso de 1
frame.columnconfigure(1, weight=3) # Aqui indicamos que la columna 1 , por lo cual es 3 veces mas grande que la columna 1

# Titulo de Login
etiqueta = ttk.Label(frame,text='Login',font=('Arial',20)) # Los componentes que vamos a empezar a trabajar los administra el frame
etiqueta.grid(row=0,column=0, columnspan=2) # Estos valores se configuran en relacion al frame y no a la ventana

# Usuario
usuario_etiqueta = ttk.Label(frame, text='Usuario: ')
usuario_etiqueta.grid(row=1,column=0, sticky=tk.W, padx=5, pady=5)

usuario_caja_texto = ttk.Entry(frame)
usuario_caja_texto.grid(row=1,column=1, sticky=tk.E, padx=5, pady=5)

# Password
password_etiqueta = ttk.Label(frame, text='Password: ')
password_etiqueta.grid(row=2,column=0, sticky=tk.W, padx=5, pady=5)

password_caja_texto = ttk.Entry(frame, show='*') # Cuando escribamos algo sobre la caja de texto, solo se van a ver *
password_caja_texto.grid(row=2,column=1, sticky=tk.E, padx=5, pady=5)

# Boton
login_boton = ttk.Button(frame, text='Enviar')
login_boton.grid(row=3, column=0, columnspan=2, padx=5, pady=5) # Aplicamos columnspan para que se expanda dos columnas desde la suya

def validar(event): # Recibe el parametro de event
    usuario = usuario_caja_texto.get()
    password = password_caja_texto.get()
    # Usuario = root y password = admin son los valores correctos
    if usuario == 'root' and password == 'admin':
        showinfo(title='Login', message='Datos correctos!')
    else:
        showerror(title='Login',message='Datos incorrectos')

# Asociar eventos al boton de login
login_boton.bind('<Return>', validar) # Presionar la tecla de enter
login_boton.bind('<Button-1>', validar) # Click izquierdo del mouse

frame.grid(row=0, column=0)

ventana.mainloop()