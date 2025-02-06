try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Agregamos informacion al archivo\n')
    archivo.write('Adios')
except Exception as error:
    print(f'Ha ocurrido un error: {error}')
finally:
    print('Fin del archivo...')
    archivo.close()
    # archivo.write('Nueva informacion') Error, ya que el archivo ya ha sido cerrado con el .close()