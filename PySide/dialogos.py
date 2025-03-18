import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, \
    QWidget, QMessageBox


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dialogos')
        # Agregamos un boton
        boton = QPushButton('Mostrar Dialogo')
        boton.clicked.connect(self.click_boton)

        # Publicamos el boton
        self.setCentralWidget(boton)

    def click_boton(self, estado):
        print(f'Click sobre boton: {estado}')
        # Creamos el dialogo personalizada

        dialogo = QMessageBox.critical(self,'Problema Critico',
                                       'Ventana con problema critico',
                                       buttons= QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore, defaultButton=QMessageBox.Discard)


        if dialogo == QMessageBox.Discard:
            print(f'Regreso el valor de Discard')

        elif dialogo == QMessageBox.NoToAll:
            print(f'Regreso el valor de NoToAll')
        else:
            print(f'Se presiono el boton de Ignore ( Ignorar_ )')
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())