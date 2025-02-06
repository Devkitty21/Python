from Clases_y_Objetos.MundoPC.computadora import Computadora
from Clases_y_Objetos.MundoPC.monitor import Monitor
from Clases_y_Objetos.MundoPC.ordenes import Ordenes
from Clases_y_Objetos.MundoPC.raton import Raton
from Clases_y_Objetos.MundoPC.teclado import Teclados

# Computadora 1
teclado = Teclados("USB", "HP")
raton1 = Raton("USB", "HP")
monitor = Monitor("HP", 15)
computadora1 = Computadora("HP", monitor, teclado, raton1)


# Computadora 2
teclado2 = Teclados("USB", "Acer")
raton2 = Raton("USB", "Acer")
monitor2 = Monitor("Acer", 27)
computadora2 = Computadora("Acer", monitor2, teclado2, raton2)

crear_lista_computadoras = [computadora1,computadora2]
orden1 = Ordenes(crear_lista_computadoras)


teclado3 = Teclados("USB", "HP")
raton3 = Raton("USB", "HP")
monitor3 = Monitor("HP", 15)
computadora3 = Computadora("HP", monitor3, teclado3, raton3)
