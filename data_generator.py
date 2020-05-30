

import random

import argparse

parser = argparse.ArgumentParser(description='generate data')

parser.add_argument("-r", "--records", help="number of records to generate", action='store', type=int, default=10000)
parser.add_argument("-o", "--output", help="file in which to store the data", action='store', type=str, default='diabetes_data.csv')

# Read arguments from the command line
args = parser.parse_args()

required_records = args.records
file_name = args.output

f = open(file_name, "w")

header = 'GAD, AGE, BMI, HbA1c, HOMA_IR, HOMA_Beta \n'

f.write(header)

for j in range(0,required_records):
    GAD = random.randrange(1,1000)
    AGE = random.randrange(1,100)
    BMI = random.randrange(10,50)
    HbA1c = float(random.randrange(400, 1400))/100  # percentage

    glucose_level = float(random.randrange(351 , 1500))/100  # mmol/L
    insulin_level = random.randrange(2,10) # uIU/ml

    HOMA_IR = round(glucose_level*insulin_level/22.5,2)
    HOMA_Beta = round((20*insulin_level)/(glucose_level-3.5),2)

    data = str(GAD) + ',' + str(AGE) + ',' + str(BMI) + ',' + str(HbA1c) + ',' + str(HOMA_IR) + ',' + str(HOMA_Beta) + '\n'

    f.write(data)

f.close()
