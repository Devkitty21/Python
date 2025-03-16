import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QDial
from PySide6.QtCore import Qt

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__() # Tenemos que mandar a llamar el metodo init de la superclase
        self.setWindowTitle('Componentes')
        # QDial es una rueda similar al slider, utilizado para aplicaciones de audio
        componente = QDial()
        componente.setRange(-5,50) # Ponemos un rango, minimo -5, maximo 8

        # Conectamos a la signals
        componente.valueChanged.connect(self.cambio_valor)
        componente.sliderMoved.connect(self.slider_cambio_posicion)
        componente.sliderPressed.connect(self.slider_presionado)
        componente.sliderReleased.connect(self.slider_liberado)


        # Publicamos este componente
        self.setCentralWidget(componente)

    def cambio_valor(self, nuevo_valor):
        print(f'Nuevo valor: {nuevo_valor}')

    def slider_presionado(self):
        print('Slider Presionado')

    def slider_liberado(self):
        print('Slider liberado')

    def slider_cambio_posicion(self, nueva_posicion):
        print(f'Nueva posicion: {nueva_posicion}')

if __name__ == '__main__':
    app = QApplication([]) # De momento no recibe ningun parametro por lo que le pasamos una lista vacia

    # Creamos una instancia de nuestra clase
    ventana = Componentes()
    ventana.show() # Publicamos la ventana

    sys.exit(app.exec())