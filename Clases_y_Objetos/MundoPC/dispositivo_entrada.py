class DispositivoEntrada:
    def __init__(self, marca, tipo_entrada):
        self._marca = marca
        self._tipo_entrada = tipo_entrada

    def get_marca(self):
        return self._marca

    def get_tipo_entrada(self):
        return self._tipo_entrada