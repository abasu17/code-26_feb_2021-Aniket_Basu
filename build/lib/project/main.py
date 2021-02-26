import pandas as pd
import multiprocessing
import sys, getopt
import json

from src.BMI import *


def call(data: dict) -> dict:
    
    bmi = BMI(data)
    bmi.run()
    
    return bmi.get_data()["DATAFRAME"]


def main(argv):
   
    inputFile = ''
    outputFile = ''
   
    try:
        opts, _ = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   
    except getopt.GetoptError:
        print ('main.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
   
    for opt, arg in opts:
      
        if opt == '-h':
            print ('main.py -i <inputfile> -o <outputfile>')
            sys.exit()
      
        elif opt in ("-i", "--ifile"):
            inputFile = arg
      
        elif opt in ("-o", "--ofile"):
            outputFile = arg

    try:
        file_open = open(inputFile)
        data = json.load(file_open)

        job_pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        async_outputs = job_pool.map_async(call, data)
        outputs = async_outputs.get()

        with open(outputFile, "w") as fp:
            json.dump(outputs, fp)

    except FileNotFoundError:
        print ('main.py -i <inputfile> -o <outputfile>')



if __name__ == "__main__":
   main(sys.argv[1:])


