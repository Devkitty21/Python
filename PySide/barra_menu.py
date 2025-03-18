from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon, QFont, QKeySequence
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar, QCheckBox
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Barra de Herramientas')
        # Publicamos una etiqueta
        etiqueta = QLabel('Hola')
        etiqueta.setFont(QFont('Cascadia Code',15))

        etiqueta.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(etiqueta)

        # Creamos la barra de herramientas
        barra = QToolBar('Mi barra de Herramientas')
        barra.setIconSize(QSize(16,16))
        # Configuracion para mostrar la barra de herramientas
        # barra.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.addToolBar(barra)
        # barra.setToolButtonStyle(Qt.ToolButtonTextOnly)
        # barra.setToolButtonStyle(Qt.ToolButtonIconOnly)
        # barra.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # barra.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)


        # Agregamos un elemento a nuestra barra de herramientas
        boton_nuevo= QAction(QIcon('nuevo.png'),'Nuevo',self)
        # Agregamos el boton a la barra
        barra.addAction(boton_nuevo)
        # Barra de estado
        self.setStatusBar(QStatusBar(self))
        # Mostramos mensaje del boton accion
        boton_nuevo.setStatusTip('Nuevo Archivo')
        # Asociamos la signal click
        boton_nuevo.triggered.connect(self.click_boton_nuevo)

        # Agregamos la opcion de guardar archivo

        boton_guardar = QAction(QIcon('guardar.png'),'Guardar',self)
        barra.addAction(boton_guardar)
        boton_guardar.setStatusTip('Guardar Archivo')
        boton_guardar.triggered.connect(self.click_boton_guardar)
        # Hacemos checkable el boton
        # boton_nuevo.setCheckable(True)

        boton_acerca_de = QAction(QIcon('acerca.png'),'Acerca De', self)
        barra.addAction(boton_acerca_de)
        boton_acerca_de.setStatusTip('Acerca de')
        boton_acerca_de.triggered.connect(self.click_boton_acerda_de)

        barra.addSeparator()

        barra.addWidget(QCheckBox())
        barra.addWidget(QLabel('Salir'))

        # Creamos un objeto de tipo menu
        menu = self.menuBar()

        menu_archivo = menu.addMenu('&Archivo') # Con el &, haciendo alt + a podremos abrir el menu
        menu_archivo.addAction(boton_nuevo)

        # Agregamos una segunda opcion
        menu_archivo.addAction(boton_guardar)

        # Agregamos un separador
        menu_archivo.addSeparator()

        # Agregamos una tercera opcion
        boton_salir = QAction('Salir',self)
        menu_archivo.addAction(boton_salir)

        # Submenu ayuda
        menu_ayuda = menu.addMenu('Ayuda')
        menu_ayuda.addAction(boton_acerca_de)

        # Agregamos el submenu ayuda como un submenu de archivo
        menu_archivo.addMenu(menu_ayuda)


        # Creacion de atajos para nuestro menu
        # Ej. Combinacion de teclas
        # boton_nuevo.setShortcut(QKeySequence('Ctrl+n'))
        boton_nuevo.setShortcut(Qt.CTRL | Qt.Key_N) # Esto es mas generico para todos los sistemas
        # Atajo acerca de - Ctrl + 1
        boton_acerca_de.setShortcut(Qt.CTRL | Qt.Key_1)

        # Atajo guardar - Ctrl + g
        boton_guardar.setShortcut(Qt.CTRL | Qt.Key_G)


    def click_boton_nuevo(self,s):
        print(f'Nuevo Archivo {s}')

    def click_boton_guardar(self,s):
        print(f'Guardando archivo... {s}')

    def click_boton_acerda_de(self,s):
        print('Acerca de...', s)

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())