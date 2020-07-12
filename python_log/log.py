import os
import logging
def logging_init(level, filename):
    DATEFMT ="[%Y-%m-%d %H:%M:%S:%MS]"
    FORMAT = "%(asctime)s %(levelname)s - %(message)s"
    logging.basicConfig(level=level,format=FORMAT,datefmt=DATEFMT,filename=filename)

#test
if __name__ == "__main__":
    logging_init(logging.DEBUG, 'test.log')
    logging.debug("hello logging")
    logging.info("hello logging")
    logging.warning("hello logging")
    logging.error("hello logging")
    logging.critical("hello logging")