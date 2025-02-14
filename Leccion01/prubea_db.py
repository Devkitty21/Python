import psycopg2

conexion = psycopg2.connect(user='test', password='whatyousee',host='127.0.0.1',port='5432',database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Proporcione el id_persona a eliminar (separado por comas): ')
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia,valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminado: {registros_eliminados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
