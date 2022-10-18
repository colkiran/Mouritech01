
import logging

logging.basicConfig(level=logging.DEBUG)

def diff(x, y):
    return x - y

a = 20
b = 8
logging.debug(f"The difference between {a} and {b} is :{diff(a, b)}")
logging.info(f"The difference between {a} and {b} is  :{diff(a, b)}")

a = 8; b = 20
logging.warning(f"The difference between {a} and {b} is :{diff(a, b)}")

a = 'x'; b = 10
logging.error(f"The difference between {a} and {b} is :{diff(a, b)}")
logging.critical(f"The difference between {a} and {b} is :{diff(a, b)}")

