from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, \
    QPushButton, QTabWidget
from PySide6.QtGui import QPalette
import sys

class Color(QWidget):
    def __init__(self, nuevo_color):
        super().__init__() # Inicializamos los atributos y metodos de la clase QWidget
        self.setAutoFillBackground(True) # True -> Para que a los widgets se les pueda agregar un fondo
        paletaColores = self.palette() # Obtenemos la paleta de colores actual del widget.
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color)) # Cambia el color del fondo del widget
        self.setPalette(paletaColores) # Aplica la nueva paleta modificada al widget

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tabulador en PySide')

        # Creamos el componente de tab
        tabulador = QTabWidget()
        # Posicion de las etiquetas del tabulador
        tabulador.setTabPosition(QTabWidget.West)
        # Indicamos si queremos que se muevan las etiquetas del tabulador
        tabulador.setMovable(True)
        # Para que se vea similar en MacOs
        tabulador.setDocumentMode(True)

        # Agregamos los colores a cada tabulador
        tabulador.addTab(Color('red'),'Rojo')
        tabulador.addTab(Color('yellow'),"Amarillo")
        tabulador.addTab(Color('green'),'Verde')

        self.setCentralWidget(tabulador) # No podemos publicar desde aqui directamente un layout



if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())