from Clases_y_Objetos.MundoPC.dispositivo_entrada import DispositivoEntrada


class Teclados(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        Teclados.contador_teclados += 1
        self.id_teclado = Teclados.contador_teclados
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f' ID: {self.id_teclado}, Marca: {self._marca}, Tipo de entrada: {self._tipo_entrada}'

if __name__ == '__main__':
    teclado1 = Teclados('HP', 'USB')
    print(teclado1)
    teclado2 = Teclados('Acer', 'Bluetooth')
    print(teclado2)
