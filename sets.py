# Profundizando en set
# Un set es una coleccion de elementos unicos y es mutable
# Los elementos de un set deben de ser inmutbales, los elementos de un set no pueden ser por ejemplo una lista ya que es mutable
# Un set no guarda orden en cada elemento
# conjunto = {[1,3],[1,2]}
conjunto = {'Juan',True,18.0}
print(conjunto)

# Set vacio
# conjunto =  {}  Esto genera un diccionario vacio
# print(type(conjunto))

conjunto = set() # Esto si crea un objeto tipo set
print(conjunto)
print(type(conjunto))

# Mutable
conjunto.add('Juan')
print(conjunto)

# Contiene valores unicos

conjunto.add('Juan') # No se duplica su valor y se imprime tal cual esta el conjunto
print(conjunto)

# Crear un set a partir de un iterable
conjunto = set([4,5,7,8,4]) # El set no tiene valores duplicados, solo tenemos una vez cada valor
print(conjunto)

# Podemos agregar mas elementos o inlcuso otro set
conjunto2 = {100,200,300,300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,30,40,40]) # Se puede hacer de esta forma directamente sin tener que crear otro objeto de tipo set
print(conjunto)

# Copiar un set a otro set (copia poco profunda, solo copia referencia)
conjunto_copia = conjunto.copy()
print(conjunto_copia)
# verificar igualdad
print(f'Es igual en contenido: {conjunto_copia == conjunto}')
print(f'Es la misma referencia: {conjunto_copia is conjunto}') # Nos preguntamos si los dos sets apuntan al mismo objeto en memoria
print(f'Id del conjunto copia: {hex(id(conjunto_copia))}')
print(f'Id del conjunto original: {hex(id(conjunto))}')

# Operaciones de conjuntos con set
# Personas con distintas caracteristicas
pelo_negro = {'Juan','Karla','Pedro','Maria'}
pelo_rubio = {'Lorenzo','Laura','Marco'}
ojos_cafe = {'Karla','Laura'}
menores_30 = {'Juan','Karla','Maria'}

# Funcion UNION (Todos los elementos con ojos_cafe y pelo_rubio) (No se repiten los elementos en un set)
print(ojos_cafe.union(pelo_rubio))
# Invertir el orden con el mismo resultado (conmutativa)
print(pelo_rubio.union(ojos_cafe))

# Funcion Interseccion (Recupera solo los elementos que se encuentran en ambos set) (Recuperamos solo las personas con ojos cafe y pelo rubio)
print(ojos_cafe.intersection(pelo_rubio))
# Invierte el orden con el mismo resultado (conmutativa)
print(pelo_rubio.intersection(ojos_cafe))

# Funcion Diferencia (Pelo negro sin ojos cafe) (Devuelve los elementos que si estan en un set pero no en el otro)
# Las personas que se encuentran en el primer set pero NO en el segundo
print(pelo_negro.difference(ojos_cafe)) # No es conmutativa

# Funcion diferencia simetrica (Devuelve todos los elementos menos las coincidencias en los dos sets) (Es conmutativa)
print(pelo_negro.symmetric_difference(ojos_cafe)) # Se devuelven todos los elementos menos los que estan en comun


# Preguntar si un set esta contenido en otro (subset)
# Revisamos si los elementos del primer set estan contenidos en el segundo set
print(menores_30.issubset(pelo_negro)) # Preguntamos si todos los elementos de menores_30 se encuentran en el set pelo_negro


# Preguntar si un set contiene a otro set (superset)
# Revisar si los elementos del primer set estan contenidos en el segundo set
print(menores_30.issuperset(pelo_negro))  # No estan todos los elementos de pelo_negro en el set de menores_30 por lo cual, menores_30 no es el superset de pelo_negro

# Revisar si dos conjuntos no tienen nada en comun
# Preguntar si los de pelo negro no tienen pelo rubio (distjoint)
print(pelo_negro.isdisjoint(pelo_rubio)) # Nos devuelve True por que ningun elemento de pelo_negro tiene que ver con los elementos de pelo_rubio

