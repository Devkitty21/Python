print('*** Casa de Los Espejos ***')

# Definimos las variables
EDAD_MINIMA = 10 # Ponemos una constante para que este valor sea fijo y no se pueda modificar

edad = int(input("Cuantos años tienes? "))
miedo_oscuridad = input('Te da miedo la oscuridad? (Si/No) ')

miedo_oscuridad = miedo_oscuridad.strip().lower() == "si"

if not miedo_oscuridad and edad >= EDAD_MINIMA:
    print('Puedes entrar a la casa de los espejos')
else:
    print('Lo siento, no puedes entrar a la casa de los espejos, podria darte miedo')