
import tkinter as tk
from tkinter import ttk, messagebox, StringVar

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x130')
        self.title('Login')
        self.iconbitmap('icono.ico')
        self.resizable(0,0) # Hacemos que no se pueda modificar el tamanio de la ventana

        # Configuracion del grid
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=3)

        # Definir el metodo crear_componentes
        self._crear_componentes()

#       Definir el metodo crear componentes
    def _crear_componentes(self):
        # Agregamos las etiquetas
        usuario_label = tk.Label(self, text='Usuario:')
        usuario_label.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        password_label = tk.Label(self, text='Password:')
        password_label.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

        # Creamos las entradas
        self.usuario_entrada = tk.Entry(self, width=30, )
        self.usuario_entrada.grid(row=0, column=1, sticky=tk.W, pady=5, padx=5)
        self.password_entrada = tk.Entry(self, width=30, show='*')
        self.password_entrada.grid(row=1, column=1, sticky=tk.W, pady=5, padx=5)

        login_boton = tk.Button(self, text='Login', command=self._login)
        login_boton.grid(row=3, column=0, columnspan=2)


    def _login(self):
        if self.usuario_entrada.get() and self.password_entrada.get():
            messagebox.showinfo('Datos Login',f'Usuario: {self.usuario_entrada.get()}, Password: {self.password_entrada.get()}')
        else:
            messagebox.showerror('Error Login','Debes indicar un usuario y un password para loguearte!')


if __name__ == '__main__':
    login_ventana = Login()
    login_ventana.mainloop()