from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os ,sys

def testing():
    try:
        a=3/0
        logging.info("testing complited")
    except Exception as e:
        logging.info(str(e))
        raise InsuranceException(e,sys)

if __name__=="__main__":
    try:
        testing()
    except Exception as e:
        print(e)