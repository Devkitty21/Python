# Ejemplo de herencia simple
class ListaSimple:
    def __init__(self,elementos):
        self._elementos = list(elementos)

    def agregar_elemento(self,elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos!r})'

class ListaOrdenada(ListaSimple):
    def __init__(self, elementos=[]):
        super().__init__(elementos)
#         Ordenamos siempre los elementos una vez inicializados
        self.ordenar()

    def agregar_elemento(self,elemento):
        super().agregar_elemento(elemento)
#         Ordenamos el nuevo elemento
        self.ordenar()


# Lista solo acepta numeros
class ListaEnteros(ListaSimple):
    def __init__(self,elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
        # Una vez validados los elementos los agregamos al atributo definido en la clase padre
        super().__init__(elementos)

    def _validar(self,elemento):
#     Validamos si el elemento es de tipo entero
        if not isinstance(elemento,int):
            raise ValueError(f'No es un valor entero: {elemento}')

        # Sobreescribimos el metodo agregar de la clase padre
    def agregar_elemento(self,elemento):
        self._validar(elemento)
        # Una vez validado lo agregamos a la lista
        super().agregar_elemento(elemento)



# Lista simple
lista_simple = ListaSimple([5,3,6,8])
print(lista_simple)

# Lista ordenada
lista_ordenada = ListaOrdenada([4,3,6,9,10,-1])
print(lista_ordenada)
lista_ordenada.agregar_elemento(-14)
print(lista_ordenada)
print(len(lista_ordenada))

# Lista enteros
lista_enteros = ListaEnteros([1,3,4,-15])
print(lista_enteros)