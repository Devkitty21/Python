# Poliformismo

class Animal:
    def hacer_sonido(self):
        print('Hago un pitido')

class Perro(Animal):
    def hacer_sonido(self):
        print('Hago Guau!')
    def dormir(self):
        pass

class Gato(Animal):
    def hacer_sonido(self):
        print('Hago Miau!')


# Funcion polimorfica
def hacer_sonido_animal(animal): # Ducktyping
    animal.hacer_sonido()

print('*** Ejemplo de Polimorfismo ***')
print('Superclase Animal: ')
animal1 = Animal()
hacer_sonido_animal(animal1)
# Definimos un objeto de la clase perro (Subclase)
print('\nSubclase Perro: ')
perro1 = Perro()
hacer_sonido_animal(perro1) # Poliformismo
print('\nSubclase Gato: ')
gato1 = Gato()
hacer_sonido_animal(gato1)

