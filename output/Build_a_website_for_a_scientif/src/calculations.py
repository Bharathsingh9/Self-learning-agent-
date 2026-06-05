python
import re
import math
from logging.config import dictConfig
from logging import getLogger

# Define logging configuration
dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            'datefmt': '%d-%b-%y %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'default',
            'filename': 'calculator.log',
            'maxBytes': 1024*1024*5,  # 5 MB
            'backupCount': 10,
            'encoding': 'utf-8'
        }
    },
    'loggers': {
        'calculator': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
})

# Create logger
logger = getLogger('calculator')

def validate_input(value):
    """
    Validate the input value
    """
    try:
        float(value)
        return True
    except ValueError:
        try:
            int(value)
            return True
        except ValueError:
            try:
                value = re.match(r'\d*\.\d+', str(value))
                if value:
                    return True
                else:
                    return False
            except Exception:
                return False

def calculate_addition(a, b=None):
    """
    Validate and perform addition operation
    """
    try:
        if validate_input(str(a)) and validate_input(str(b)):
            logger.debug(f"Addition operation: a = {a}, b = {b}")
            return float(a) + float(b)
        else:
            logger.error("Malicious input detected: Invalid type for operands")
            return None
    except Exception as e:
        logger.error(f"An error occurred while performing addition operation: {str(e)}")
        return None

def calculate_subtraction(a, b=None):
    """
    Validate and perform subtraction operation
    """
    try:
        if validate_input(str(a)) and validate_input(str(b)):
            logger.debug(f"Subtraction operation: a = {a}, b = {b}")
            return float(a) - float(b)
        else:
            logger.error("Malicious input detected: Invalid type for operands")
            return None
    except Exception as e:
        logger.error(f"An error occurred while performing subtraction operation: {str(e)}")
        return None

def calculate_multiplication(a, b=None):
    """
    Validate and perform multiplication operation
    """
    try:
        if validate_input(str(a)) and validate_input(str(b)):
            logger.debug(f"Multiplication operation: a = {a}, b = {b}")
            return float(a) * float(b)
        else:
            logger.error("Malicious input detected: Invalid type for operands")
            return None
    except Exception as e:
        logger.error(f"An error occurred while performing multiplication operation: {str(e)}")
        return None

def calculate_division(a, b=None):
    """
    Validate and perform division operation
    """
    try:
        if validate_input(str(a)) and validate_input(str(b)):
            logger.debug(f"Division operation: a = {a}, b = {b}")
            if float(b) != 0:
                return float(a) / float(b)
            else:
                logger.error("Division by zero is not allowed")
                return None
        else:
            logger.error("Malicious input detected: Invalid type for operands")
            return None
    except Exception as e:
        logger.error(f"An error occurred while performing division operation: {str(e)}")
        return None

def calculate_root(a):
    """
    Calculate the square root of a number
    """
    try:
        if validate_input(str(a)):
            if float(a) >= 0:
                logger.debug(f"Square root operation: a = {a}")
                return math.sqrt(float(a))
            else:
                logger.error("Cannot calculate square root of a negative number")
                return None
        else:
            logger.error("Malicious input detected: Invalid type for operand")
            return None
    except Exception as e:
        logger.error(f"An error occurred while performing square root operation: {str(e)}")
        return None

def calculate_power(a, b):
    """
    Validate and perform a^b operation
    """
    try:
        if validate_input(str(a)) and validate_input(str(b)):
            logger.debug(f"Power operation: a = {a}, b = {b}")
            return float(a) ** float(b)
        else:
            logger.error("Malicious input detected: Invalid type for operands")
            return None
    except Exception as e:
        logger.error(f"An error occurred while performing power operation: {str(e)}")
        return None

def calculate_logarithm(a):
    """
    Calculate the natural logarithm of a number
    """
    try:
        if validate_input(str(a)) and float(a) > 0:
            logger.debug(f"Natural logarithm operation: a = {a}")
            return math.log(float(a))
        else:
            logger.error("Malicious input detected: Invalid type for operand or operand is not positive")
            return None
    except Exception as e:
        logger.error(f"An error occurred while performing natural logarithm operation: {str(e)}")
        return None
