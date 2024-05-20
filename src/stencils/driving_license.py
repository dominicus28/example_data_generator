import csv
import random
import os

def create_driving_lic_number():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../county_numbers.csv')
    with open(filename, mode='r',
              encoding='utf-8') as file:
        csvFile = csv.reader(file, delimiter=';')
        chosen_row = random.choice(list(csvFile))
        county_number = str(chosen_row[0]) + str(chosen_row[1])

    digits = ''
    for _ in range(5):
        digits += str(random.randint(0, 9))

    year = str(random.choice(["%02d" % random.randint(0, 24), random.randint(50, 99)]))
    
    return digits + '/' + year + '/' + county_number