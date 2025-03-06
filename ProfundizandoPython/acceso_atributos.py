# Ejemplo atributos publicos, protegidos, privados

class MiClase:
    def __init__(self,publico,protegido,privado):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado


objeto = MiClase('Valor Publico','Valor protegido','Valor privado')
# Acceso al atributo publico
print(objeto.publico)
# Modificar el valor publico
objeto.publico = 'Nuevo valor publico'
print(objeto.publico)

# Acceso al atributo protegido
print(objeto._protegido) # No es buena practica pero solo deberiamos usarlo dentro de la misma clase o subclases
# Modificar atributo protegido
objeto._protegido = 'Nuevo valor protegido' # No es buena practica tampoco pero si podemos hacerlo
print(objeto._protegido)

# Acceder al valor privado
# print(objeto.__privado) No se puede acceder directamente
# Pero, convierte: objeto._clase__atributo_privado
print(objeto._MiClase__privado)
# Modificar valor privado
objeto._MiClase__privado = 'Nuevo valor privado'
print(objeto._MiClase__privado)