import sys
from random import randint

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit


class NuevaVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Nueva Ventana')
        layout = QVBoxLayout()
        self.etiqueta = QLabel(f'Nueva Ventana: {randint(0,100)}')
        layout.addWidget(self.etiqueta)
        self.setLayout(layout)




class VentanaPrincipal(QMainWindow):
    def __init__(self):
        # self.nueva_ventana = None
        # Creamos una instancia, no varias
        self.nueva_ventana = NuevaVentana()
        super().__init__()
        self.setWindowTitle('Ventanas')
        self.boton = QPushButton('Mostrar/Ocultar nueva ventana')
        self.boton.clicked.connect(self.mostrar_nueva_ventana)
        # Definimos una entrada de texto
        self.entrada_texto = QLineEdit()
        self.entrada_texto.textChanged.connect(self.nueva_ventana.etiqueta.setText)
        layout = QVBoxLayout()
        layout.addWidget(self.boton)
        layout.addWidget(self.entrada_texto)
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def mostrar_nueva_ventana(self, estado):
        if self.nueva_ventana.isVisible(): # Comprobamos que el objeto es visible, en ese caso, lo ocultamos
            self.nueva_ventana.hide()
        else:
            self.nueva_ventana.show() # En el caso de que no sea visible, se muestra con el metodo show

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())