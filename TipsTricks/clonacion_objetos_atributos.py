# Copia de atributos de objetos
import copy


# Definimos una clase de tipo Punto 2D
class Punto:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Punto({self.x!r}, {self.y!r})'

    def __eq__(self, other):
        return isinstance(other, Punto) and self.x == other.x and self.y == other.y


punto_a = Punto(2,3)
punto_b = copy.copy(punto_a)
# Copia poco profunda (shallow), son distintos objetos
print(f'Copia poco profunda (shallow)')
print(f'Punto a: {punto_a}')
print(f'Punto b: {punto_b}')
print(f'Son objetos con el mismo contenido: {punto_a == punto_b}') # Tenemos que implementar el metodo dunder de __eq__ en estos casos
print(f'Son los mismos objetos (misma referencia)?: {punto_a is punto_b}') # No apuntan a la misma direccion en memoria

# Clase Rectangulo utiliza dos puntos (superior izquierdo e inferior derecho)
class Rectangulo:
    def __init__(self,sup_izq,inf_der):
        self.sup_izq = sup_izq
        self.inf_der = inf_der

    def __repr__(self):
        return f'Rectangulo({self.sup_izq!r}, {self.inf_der!r})'

rect_a = Rectangulo(Punto(0,1), Punto(3,4))
# Copia superficial (shallow)
rect_b = copy.copy(rect_a)
print(f'Copia superficial rectangulos')
print(f'Rectaungulo a: {rect_a}')
print(f'Rectangulo b: {rect_b}')
# Debido a que la copia fue superficial, un cambio en un punto afecta al otro rectangulo
rect_b.inf_der.y = 6
print(f'Cambio en un punto afecta al otro rectangulo por hacer una copia superficial (shallow)')
print(f'Rectaungulo a: {rect_a}')
print(f'Rectangulo b: {rect_b}')

# Creacion copia profunda (deepcopy)
rect_c = copy.deepcopy(rect_a)
# Modificamos un valor en un punto, esto no afecta al otro rectangulo (Copia profunda)
rect_c.sup_izq.x = 2
rect_a.sup_izq.y = 3 # Esto no afecta por que no apuntan al mismo objeto en memoria
print(f'Cambio en un punto NO afecta al otro rectangulo (deep copy)')
print(f'Rectaungulo a: {rect_a}')
print(f'Rectangulo c: {rect_c}')

