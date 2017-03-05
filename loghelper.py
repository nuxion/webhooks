import os
import logging
import logging.config
import yaml
""" taking from:
https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/ .
"""

def setup_logging(
    default_path='config/log.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level) 
if __name__ == "__main__":
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting program...")
    logger.debug("test debug")
    logger.error("test error")
    logger.info("Finish")
