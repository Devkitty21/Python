# Logging es una herramienta utilizada en programación para registrar mensajes que ayudan a monitorizar y entender
# cómo se ejecuta un programa. Permite detectar errores, registrar eventos importantes, y proporcionar información
# útil para el desarrollo y la depuración de aplicaciones sin necesidad de usar prints en la salida estándar.

import logging as log


# log = logging # Ambas opciones son validas aunque es mas comun la de arriba

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel de Info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel critico')
    
