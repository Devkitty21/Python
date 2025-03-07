# Leer archivo json
# JSON = JavaScript Object Notation
import json
import urllib.request

respuesta = urllib.request.urlopen('http://globalmentoring.com.mx/api/personas.json')
print(respuesta)
cuerpo_respuesta = respuesta.read()
print(cuerpo_respuesta)
# Procesamos la respuesta
json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
print(json_respuesta)
# Imprimir solo los nombres de las personas
# JSON se convierte a listas y diccionarios en python
for persona in json_respuesta['personas']:
    print(f'Persona: {persona["nombre"]}, {persona["edad"]}')
# Accedemos a los variables independientes
print(f'Total de personas: {json_respuesta["total"]}')
print(f'Mensaje: {json_respuesta["mensaje"]}')