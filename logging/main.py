import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s:%(asctime)s:%(message)s',
    handlers=[
        logging.FileHandler("log.txt", "w"),
        logging.StreamHandler()
    ]
)

logging.debug('MSG1')
logging.info('MSG2')
logging.warning('MSG3')
logging.error('MSG4')
logging.critical("MSG5")
