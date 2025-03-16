import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# Clase base de Qt (PySide) #Qt Es la implementacion de paga, la implementacion gratuita es Pyside
# Se encarga de procesar los eventos (event loop)
app = QApplication()
# Crear un objeto ventana
# En PySide Cualquier componente puede ser una ventana en PySide
# ventana = QPushButton('Boton PySide')
ventana = QMainWindow()
# Cambiar el titulo
ventana.setWindowTitle('Hola Mundo con PySide')
# Modificamos el tamanio de la ventana
ventana.resize(600,400)
# Mostrar la ventana
ventana.show()
# Se ejecuta la aplicacion
sys.exit(app.exec())