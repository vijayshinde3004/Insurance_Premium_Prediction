from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os ,sys
from Insurance.utils import get_collection_as_dataframe


if __name__=="__main__":
    try:
      get_collection_as_dataframe(database_name="INSURANCE",collection_name="INSURANCE_PROJECT")
    except Exception as e:
        print(e)