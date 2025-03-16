# Signals y slots
# Signal es el evento al hacer algo, (pulsar un boton por ejemplo) y slot es la funcion de ese evento
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        self.setFixedSize(400,200)
        # Definimos la etiqueta y linea de edicion
        self.etiqueta = QLabel()
        self.entrada_texto = QLineEdit()
        # Conectar el widget de entrada de texto con la etiqueta
        # La senial es textChanged, y el slot es setText
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)
        # Publicamos los componentes usando un layout
        disposicion = QVBoxLayout()
        disposicion.addWidget(self.entrada_texto)
        disposicion.addWidget(self.etiqueta)
        # Crear un contenedor
        contenedor = QWidget()
        contenedor.setLayout(disposicion)
        # Publicamos el contenedor, el cual ya incluye los demas elementos
        self.setCentralWidget(contenedor)



if __name__ == '__main__':
    # Creamos el objeto aplicacion
    app = QApplication()
    # Creamos una instancia (objeto) de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show() # Mostramos la ventana
    sys.exit(app.exec()) # Nos aseguramos de salir correctamente de la ventana