print('*** Sistema de Envios ***')

print("\n***** Costo Tarifas *****")
print("""
Nacional = 10 x kilo
Internacional = 20 x kilo
""")

NACIONAL = 10
INTERNACIONAL = 20

destino = input("Introduce el destino de tu paquete (nacional/intenacional): ")
peso = float(input('Introduce el peso (kilogramos) del paquete: '))

coste_envio = None

destino = destino.strip().lower()
if destino == 'nacional':
    coste_envio = NACIONAL * peso
elif destino == 'internacional':
    coste_envio = INTERNACIONAL * peso
else:
    print('Destino desconocido, vuelva a intentarlo!')

if coste_envio is not None:
    print(f'\nEl destino de tu paquete es: {destino}')
    print(f'El peso de tu paquete es: {peso}')
    print(f'Coste de envio: ${coste_envio:.2f}')