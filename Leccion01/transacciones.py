import psycopg2 as db

conexion = db.connect(user='test', password='whatyousee',host='127.0.0.1',port='5432',database='test_db')

try:
    with conexion:
            with conexion.cursor() as cursor:
                sentencia = 'INSERT INTO persona (nombre,apellido,email) VALUES(%s,%s,%s)'
                valores = ('Alex','Rojas','arojas@gmail.com')
                cursor.execute(sentencia, valores)

                sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
                valores = ('Juan', 'Perez','jperez@gmail.com',2)
                cursor.execute(sentencia,valores)

except Exception as e: # Se hace el roll back automaticamente en caso de error
    print(f'Ocurrio un error, se hizo un rollback de la transaccion: {e}')
finally:
    conexion.close()
print(f'Termina la transaccion, se hizo un commit')

# En el caso de que hagamos de forma manual el commit y el rollback esta bien pero esta es una mejor practica
# conexion.autocommit = False
# conexion.commit() and conexion.rollback()