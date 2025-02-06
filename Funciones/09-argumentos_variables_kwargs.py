# *args - arguments - tupla
# **kwargs - keyword arguments (key-value) como un dict

print(f'*** Argumentos Variables en forma de Diccionario ***')
def superheroe_superpoder(nombre, *args, **kwargs): # Primero todos los parametros posicionales luego los *args y luego los **kwargs
    print(f'Superheroe: {nombre} - {args} - Mas info: {kwargs}')

# Llamamos la funcion

superheroe_superpoder('Spiderman', 'Instinto Aracnido', edad=17, empresa='Marvel')
superheroe_superpoder('Ironman', 'Armadura','Playboy',edad=48)

# Es opcional enviar argumentos variable
superheroe_superpoder('Mi vecino',personalidad='Es buena gente')

superheroe_superpoder('Mi vecino') # Se puede ver que *args y **kwargs son opcionales
