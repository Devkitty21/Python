import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QMenu


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu Contextual')
        # Mostramos y conectamos el menu contextual
        self.show()
        # Nos conectamos a la signal de CustomContextMenuRequested
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.mostrar_menu_contexto)



    def mostrar_menu_contexto(self, posicion):
        menu_contextual = QMenu(self)
        boton_nuevo = QAction(QIcon('nuevo.png'),'Nuevo',self)
        boton_guardar = QAction(QIcon('guardar.png'),'Guardar',self)
        boton_salir = QAction('Salir',self)
        # Agregamos las opciones al Menu Contextual
        menu_contextual.addAction(boton_nuevo)
        menu_contextual.addAction(boton_guardar)
        menu_contextual.addAction(boton_salir)
        # Agregamos las signals
        boton_nuevo.triggered.connect(self.click_boton_nuevo)
        boton_guardar.triggered.connect(self.click_boton_guardar)
        boton_salir.triggered.connect(self.click_boton_salir)

        # Recuperamos la posicion del cursor como posicion global de la ventana padre
        # Y ejecutamos el menu contextual
        menu_contextual.exec(self.mapToGlobal(posicion))

    # Slots de los botones
    def click_boton_nuevo(self,s):
        print(f'Opcion nuevo... {s}')
    def click_boton_guardar(self,s):
        print(f'opcion Guardar... {s}')
    def click_boton_salir(self,s):
        print(f'Opcion salir... {s}')





if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())