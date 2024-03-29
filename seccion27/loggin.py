import logging as log;

log.basicConfig(level=log.DEBUG,     # Aqui se modifica el nivel
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])
                
if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel de info')
    log.warning('Mensaje a nivek de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel critico')