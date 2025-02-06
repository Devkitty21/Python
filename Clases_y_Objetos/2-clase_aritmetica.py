class Aritmetica:

    # Python solamente coje el ultimo constructor
    # def __init__(self,operando1):
    #     self.operando1 = int(operando1)

    def __init__(self,operando1=None, operando2=None):
        self._operando1 = operando1
        self._operando2 = operando2

    @property
    def operando1(self):
        return self._operando1

    @operando1.setter
    def operando1(self,operando1):
        self._operando1 = operando1

    @property
    def operando2(self):
        return self._operando2

    @operando2.setter
    def operando2(self,operando2):
        self._operando2 = operando2

    def sumar(self):
        resultado = self._operando1 + self._operando2
        print(f'Resultado de la suma: {resultado}')

    def resta(self):
        resultado = self._operando1 - self._operando2
        print(f'Resultado de la resta: {resultado}')

    def multi(self):
        resultado = self._operando1 * self._operando2
        print(f'Resultado de la multiplicacion: {resultado}')

    def div(self):
        resultado = self._operando1 / self._operando2
        print(f'Resultado de la division: {resultado:.2f}')

if __name__ == '__main__':
    print(f'\nObjeto 1:')
    aritmetica1 = Aritmetica(5,7) # Creando el objeto
    aritmetica1.operando1 = 10 # Cambiando los valores
    aritmetica1.operando2 = 10
    print(f'Valor de operando1: {aritmetica1.operando1}')
    print(f'Valor de operando2: {aritmetica1.operando2}')
    aritmetica1.sumar()
    aritmetica1.resta()

    # Segundo objeto
    print(f'\nSegundo objeto')
    aritmetica2 = Aritmetica(3,15)
    print(f'Valor inicial de operando1 y operando2: {aritmetica2.operando1, aritmetica2.operando2}')
    aritmetica2.operando1 = 5
    aritmetica2.operando2 = 10
    print(f'Nuevos valores de opernado1 y operando2: {aritmetica2.operando1, aritmetica2.operando2}')
    aritmetica2.sumar()
    aritmetica2.resta()

