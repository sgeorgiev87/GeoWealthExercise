import logging.config
import os

logging.config.fileConfig(os.path.realpath(os.path.dirname(__file__) + '/logger.conf'))

# create logger
logger = logging.getLogger('Prod_env')
