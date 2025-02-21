import logging as log
from logging import FileHandler

log.basicConfig(level=log.DEBUG,
                format='[%(asctime)s %(filename)s %(lineno)s] %(levelname)s: %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[log.FileHandler('logs.log'),
                          log.StreamHandler()])

if __name__ == '__main__':
    log.debug(f'Mensaje a nivel de debug')
    log.info(f'Mensaje a nivel de info')
    log.warning(f'Mensaje a nivel de warning')
    log.error(f'Mensaje a nivel de error')
    log.critical(f'Mensaje a nivel de critical')