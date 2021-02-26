import pandas as pd
import multiprocessing
import sys, getopt
import json

from .BMI import *


def call(data: dict) -> dict:

    """
    @NAME   :   call()
    @TYPE   :   Method
    @SYNTAX :   call(dict)
    @DESC   :   initiate BMI object for calculation
    @AUTHOR :   Aniket Basu
    @EMAIL  :   aniketbasu7@gmail.com
    """
    
    bmi = BMI(data)
    bmi.run()
    
    return bmi.get_data()["DATAFRAME"]


def calculate(data: list) -> list():
   
    """
    @NAME   :   calculate()
    @TYPE   :   Method
    @SYNTAX :   calculate(list)
    @DESC   :   initiate BMI object for calculation
    @AUTHOR :   Aniket Basu
    @EMAIL  :   aniketbasu7@gmail.com

    Usage Example:
        >>> from bmi_calculator import main
        >>> import json
        >>> json_path = <json path>
        >>> fp = open(json_path, )
        >>> data = json.loads(fp.readlines()[0])
        >>> main.calculate(data)
    """

    try:

        job_pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        async_outputs = job_pool.map_async(call, data)
        outputs = async_outputs.get()

        return outputs

    except Exception as e:
        print("Error: ", str(e))
