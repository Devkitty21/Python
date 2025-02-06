print("*** Operaciones con Sets ***")

a = {1,2,3,4}
b = {3,4,5,6}

union = a | b # Se unen los dos sets sin repetir los elementos
print(f"Union a | b: {union}")

interseccion = a & b # Muestra los valores que coinciden en los dos sets
print(f'Interseccion a & b: {interseccion}')

diferencia = a - b # Que elementos hay en a que no hay en b (En el caso de que dos elementos se repitan no se incluyen en la diferencia)
print(f'Diferencia de a - b: {diferencia}')