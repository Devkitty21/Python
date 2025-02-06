class Animal:

    def comer(self):
        print(f'Como muchas veces al dia')

    def dormir(self):
        print(f'Duermo muchas horas')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar Guau!')

    # Sobreescritura del metodo dormir
    def dormir(self):
        print(f'Duermo 15 horas al dia')


# Programa prinipal
if __name__ == '__main__':
    print('*** Ejemplo de herencia en Python')
    print(f'Superclase, Animal')
    animal1 = Animal()
    animal1.comer()
    animal1.dormir()
    print(f'\nSubclase de Animal, Perro')
    perro1 = Perro()
    perro1.comer()
    perro1.dormir() # Se llama el metodo dormir() sobreescrito de la subclase de Aniaml (La Superclase)
    perro1.hacer_sonido()


class Animal:
    def comer(self, ):
        print(f'Como muchas veces al dia')

class Perro(Animal):
    def emitir_sonido(self):
        print('Guau')

class Gato(Perro):
    def sonido_gato(self):
        print('Miau')