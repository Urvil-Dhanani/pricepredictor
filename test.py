import sys
from src.exception.exception import CustomException

try:
    a = 1/0
except Exception as e:
    raise CustomException(e, sys)
