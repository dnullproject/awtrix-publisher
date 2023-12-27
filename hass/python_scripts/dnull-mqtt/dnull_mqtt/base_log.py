import logging
from config import Config

config = Config()
logging.basicConfig(format='%(asctime)s - %(message)s')
log = logging.getLogger(__name__)
log.setLevel(config.log_level)
