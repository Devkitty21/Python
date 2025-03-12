import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

class sumar(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x130')
        self.title('Sumadora')
        self.iconbitmap('icono.ico')
        self.resizable(0,0)

        # self.columnconfigure(0,weight=1)
        # self.columnconfigure(1,weight=3)
        # self.rowconfigure(2,weight=1)
        # self.rowconfigure(3,weight=3)
        # Creamos las entradas
        self.n1_entrada = tk.Entry(self,width=15)
        self.n1_entrada.grid(row=0,column=1, padx=10, pady=10)
        self.n2_entrada = tk.Entry(self,width=15)
        self.n2_entrada.grid(row=1,column=1, padx=10, pady=10)

        # Creamos las etiquetas
        self.n1_etiqueta = tk.Label(self,text='Valor 1:')
        self.n2_etiqueta = tk.Label(self,text='Valor 2:')
        self.n1_etiqueta.grid(row=0,column=0, padx=10,pady=10)
        self.n2_etiqueta.grid(row=1,column=0, padx=10,pady=10)

        # Creamos un boton
        self.boton = tk.Button(self,text='Sumar', commantd=self._sumar)
        self.boton.grid(row=2,column=0,columnspan=2)

        # Creamos un menu de ayuda y de salir
        self.menu_principal = tk.Menu(self)
        self.submenu_salir = Menu(self.menu_principal, tearoff=False)
        self.submenu_salir.add_command(label='Salir', command=self._salir)
        self.menu_principal.add_cascade(label='Salir',menu=self.submenu_salir)
        self.submenu_ayuda = Menu(self.menu_principal, tearoff=0)
        self.submenu_ayuda.add_command(label='Como lo hago', command=self._como)
        self.menu_principal.add_cascade(label='Ayuda',menu=self.submenu_ayuda)
        self.config(menu=self.menu_principal)


    def _sumar(self):
        if self.n1_entrada.get() and self.n2_entrada.get():
            self.resultado = int(self.n1_entrada.get()) + int(self.n2_entrada.get())
            messagebox.showinfo('Resultado de la suma',f'El resultado de la suma de los valores: {self.resultado}')
        elif self.n1_entrada.get() or self.n2_entrada.get():
            messagebox.showwarning('Cuidado!','Es necesario que ingreses los dos valores')
        else:
            messagebox.showerror('Error!','Debes ingresar los valores que quieres sumar')

    def _salir(self):
        self.quit()
        print('Salimos..')
        self.destroy()
        sys.exit()

    def _como(self):
        messagebox.showinfo('Como lo hago','Debes introducir los dos valores que quieres sumar,\na continuacion haz click en el boton de \'sumar\' y ya tendras el resultado')

if __name__ == '__main__':
    sumar_ventana = sumar()
    sumar_ventana.mainloop()