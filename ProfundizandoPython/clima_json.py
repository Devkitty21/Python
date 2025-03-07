# Recuperar la descripcion del clima
# y la temp_max y temp_min
import urllib.request
import json

respuesta_pagina = urllib.request.urlopen('https://globalmentoring.com.mx/api/clima.json')
# print(respuesta_pagina)

# Procesar la respuesta de tipo json
json_respuesta = json.loads(respuesta_pagina.read().decode('utf-8'))
print(json_respuesta)

# Ejercicio
print(f'Descripcion del clima: {json_respuesta["clima"][0]["descripcion"]}')
print(f'Temperatura maxima: {json_respuesta["principal"]["temp_max"]}')
print(f'Temperatura minima: {json_respuesta["principal"]["temp_min"]}')





# Test 1
#
# informacion_pagina = urllib.request.urlopen('https://jsonplaceholder.typicode.com/posts')
#
# # Leer informacion de la pagina
# json_informacion = json.loads(informacion_pagina.read().decode('utf-8'))
#
# for i in range(5):
#     print(f"Post {json_informacion[i]['id']}: {json_informacion[i]['title']}")



# Test 2

# url = urllib.request.urlopen('https://jsonplaceholder.typicode.com/users')
#
# # Leer la informacion de la url
#
# url_json = json.loads(url.read().decode('utf-8'))
# for i in range(5):
#     print(f"Name: {url_json[i]['name']} | Username: {url_json[i]['username']} | Email: {url_json[i]['email']}")
#     print(f"Ciudad: {url_json[i]['address']['city']} | Calle: {url_json[i]['address']['street']}")
#     print('\n')