# Generador de emails
print("*** Generador de Emails ***")

#Definimos las variables
nombre_usuario = "Ubaldo Acosta Soto"
nombre_usuario_normalizado = nombre_usuario.lower()
nombre_usuario_normalizado = nombre_usuario_normalizado.replace(" ",".")
nombre_empresa = "Global Mentoring"
dominio = ".com.mx"
dominio_normalizado = nombre_empresa.lower()
dominio_normalizado = dominio_normalizado.replace(" ","") + dominio

# Imprimimos los valores

print(f"Nombre Usuario: {nombre_usuario}")
print(f"Nombre usuario normalizado: {nombre_usuario_normalizado}" )
print()
print(f"Nombre empresa: {nombre_empresa}")
print(f"Extension del dominio: {dominio}")
print(f"Dominio de email normalizado: @{dominio_normalizado}\n")
print(f"Email final generado: {nombre_usuario_normalizado}@{dominio_normalizado}")


