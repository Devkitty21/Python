import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton


class VentanaPyside(QMainWindow):
    def __init__(self):
        super().__init__() # Llamamos al metodo init de la clase padre (Importante!!)\
        self.setWindowTitle('POO Con PySide')
        # self.resize(600,400)
        # Colocamos los valores de ancho y alto de manera fija
        self.setFixedSize(QSize(600,400))
        # Creamos algunos componentes
        self._agregar_componentes()

    def _agregar_componentes(self):
        # Agregamos un menu
        menu = self.menuBar() # Creamos la barra de menu
        menu_archivo = menu.addMenu('Archivo') # Al menu le agregamos la opcion de archivo

        # Agregamos algunas opciones al menu
        accion_nuevo = QAction('Nuevo',self)
        menu_archivo.addAction(accion_nuevo)
        # Agregamos un texto a la barra de estado
        accion_nuevo.setStatusTip('Nuevo Archivo')
        # Agregamos un mensaje en la barra de estado
        self.statusBar().showMessage('Informacion de la barra de estado...')

        # Agregamos un boton
        boton = QPushButton('Nuevo Boton')
        # Publicamos el bnoton en la ventana
        self.setCentralWidget(boton)



if __name__ == '__main__':
    app = QApplication([])
    # Creamos un objeto de tipo ventana
    ventana = VentanaPyside()
    ventana.show()
    # Ejecutamos la ventana
    sys.exit(app.exec())