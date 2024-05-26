import sys
from src.exception.exception import CustomException
from src.logger.logging import logging

try:
    a = 1/0
except Exception as e:
    logging.info("Error Occured")
    raise CustomException(e, sys)
