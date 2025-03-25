# De manera explicita
def funcion1(valor):
    if valor:
        return valor
    else:
        return None

print(funcion1(0)) # Si pasamos algun valor que se considere falso se devuelve la parte de else

# De manera implicita
def funcion2(valor):
    if valor:
        return valor

print(funcion2(0)) # De igual manera se devuelve el valor de None aunque no este definido de manera explicita

def funcion3(valor):
    print(valor)

funcion3(15)
# print(funcion3(10)) # Esto nos devuelve 10 y None porque la funcion3 ya imprime el valor
# por lo cual como no tiene nada para imprimir despues imprime None (Ausencia de valor)
