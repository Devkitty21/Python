import tkinter

ventana = tkinter.Tk()
ventana.geometry('600x400')
ventana.title('Esta es mi ventana')
ventana.iconbitmap('C:\\Users\\vieir\\PycharmProjects\\Tkinter\\icono.ico')

label1 = tkinter.Label(ventana, text='Hola, Tkinter!')
label1.grid(row=0, column=0, padx=5, pady=5, sticky=tkinter.W)

def evento():
    label1.config(text='Texto Tkinter cambiado!')

boton1 = tkinter.Button(ventana, text='Cambiar texto', bd=1, bg='#eee', command=evento)
boton1.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

entrada1 = tkinter.Entry(ventana, width=15)
entrada1.grid(row=1, column=0, padx=5, pady=5, sticky=tkinter.W)

label2 = tkinter.Label(ventana, text='Este es el texto por default')
label2.grid(row=2,column=0, padx=5, pady=5, sticky=tkinter.W)
def evento2():
    label2.config(text=entrada1.get())


boton2 = tkinter.Button(ventana, text='Enviar', bd=1, bg='#eee', command=evento2)
boton2.grid(row=1, column=1, padx=5, pady=5)


ventana.mainloop()