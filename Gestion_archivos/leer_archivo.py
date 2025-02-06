try:
    # archivo = open('c:\\Users\\vieir\\PycharmProjects\\PythonProject\\Gestion_archivos\\prueba.txt', 'r', encoding='utf8')
    archivo = open('prueba.txt', 'r', encoding='utf8')
    # print(archivo.read())

    # Leer algunos caracteres
    # print(archivo.read(5))
    # print(archivo.read(4))

    # Leer lineas completas
    # print(archivo.readline())
    # print(archivo.readline())

    #  Iterar el archivo
    # for linea in archivo:
    #     print(linea)

    # Leer lineas
    # print(archivo.readlines())

    # Acceder a una linea de la lista
    # print(archivo.readlines()[0])

    # abrimos un nuevo archivo
    # a - anexar informacion
    archivo2 = open('prueba2.txt', 'a') # Si ponemos el parametro a es para agregar mas informacion sin borrar y si ponemos w sobreescribe lo escrito
    archivo2.write(archivo.read())


except Exception as error:
    print(error)
finally:
    print('Se ha terminado el proceso de leer y copiar archivos')
    archivo.close()
    archivo2.close()
