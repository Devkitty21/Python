from Clases_y_Objetos.sistema_empleados.empresa import Empresa
from Clases_y_Objetos.sistema_empleados.empleado import Empleado

print(f'*** Sistema de Empleados ***')

# Crear una instancia de una empresa

empresa1 = Empresa('Global Mentoring')

# Contratar algunos empleados
empresa1.contratar_empleado('Juan','Ventas')
empresa1.contratar_empleado('Maria','Marketing')
empresa1.contratar_empleado('Pedro','Ventas')
empresa1.contratar_empleado('Ana','Recursos Humanos')

# Obtener el total de objetos de tipo empleado
print(f'Total de empleados: {Empleado.obtener_total_empleados()}')

# Obtener el numero de empleados en el departamento de ventas
print(f'Empleados en el departamento de ventas'
      f': {empresa1.obtener_numero_empleados_departamento("Ventas")}')

empresa1.obtener_total_de_empleados()