import logging

logging.basicConfig(filename='blue_ox.log')

logging.debug("Looks like rain")
logging.info("And hail")
logging.warn("Did I hear thunder?")

logging.basicConfig(level='DEBUG', filename='blue_ox.log')
logging.debug("It's raining again")
logging.info("With hail the size of hailstones")


fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level='DEBUG', format=fmt)
logger = logging.getLogger('bunyan')
logger.error("Where's my other plaid shirt?")