
import logging

logging.basicConfig(filename="myfile.log", filemode="w",
                    level=logging.WARNING,
                    format= '%(asctime)s : %(levelname)s : %(name)s : %(message)s')

def diff(x, y):
    return x - y

a = 20
b = 8
logging.debug(f"The difference between {a} and {b} is :{diff(a, b)}")
logging.info(f"The difference between {a} and {b} is  :{diff(a, b)}")

a = 8; b = 20
logging.warning(f"The difference between {a} and {b} is :{diff(a, b)}")

a = 2; b = 10
logging.error(f"The difference between {a} and {b} is :{diff(a, b)}")
logging.critical(f"The difference between {a} and {b} is :{diff(a, b)}")
