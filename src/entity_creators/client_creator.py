import src.utilities as utils
import random
from datetime import datetime, timedelta
import string
import csv


class ClientBuilder:
    @staticmethod
    def gen_datetime(min_year=1900, max_year=datetime.now().year):
        # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
        start = datetime(min_year, 1, 1, 00, 00, 00)
        years = max_year - min_year + 1
        end = start + timedelta(days=365 * years)

        return start + (end - start) * random.random()

    @staticmethod
    def multiply_part(part):
        weights = [1, 3, 7, 9]
        w_iter = utils.gentr_fn(weights)
        sum = 0

        for i in range(10):
            next_item = w_iter.__next__()

            if int(part[i]) * next_item > 9:
                sum += (int(part[i]) * next_item) % 10
            else:
                sum += int(part[i]) * next_item

        return sum

    @staticmethod
    def create_pesel(gender):
        date = ClientBuilder.gen_datetime()
        birth = str(date)

        if int(birth[0:4]) > 1999:
            month = str(int(birth[5:7]) + 20)
            part_pesel = (birth[2:4] + month + birth[8:10] + str(random.randint(1, 9)) +
                          str(random.randint(1, 9)) + str(random.randint(1, 9)))
        else:
            part_pesel = (birth[2:4] + birth[5:7] + birth[8:10] + str(random.randint(1, 9)) +
                          str(random.randint(1, 9)) + str(random.randint(1, 9)))

        if gender == 'F':
            gender_digit = (random.randint(0, 10) * 2) % 10
        elif gender == 'M':
            gender_digit = ((random.randint(0, 10) * 2) - 1 ) % 10

        part_pesel += str(gender_digit)
        sum = ClientBuilder.multiply_part(part_pesel)

        if sum == 10:
            ctrl_digit = 0
        elif sum > 9:
            ctrl_digit = 10 - (sum % 10)
        else:
            ctrl_digit = 10 - sum

        final_pesel = part_pesel + str(ctrl_digit)

        return final_pesel

    @staticmethod
    def create_id_number():
        chars = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20,
                 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31,
                 'w': 32, 'x': 33, 'y': 34, 'z': 35}
        weights = [7, 3, 1, 7, 3, 1, 7, 3]
        letters = ''.join(random.choice(string.ascii_letters) for _ in range(3)).lower()
        digits = ''
        for _ in range(5):
            digits += str(random.randint(0, 9))
        sum = chars[letters[0]] * 7 + chars[letters[1]] * 3 + chars[letters[2]] * 1 + int(digits[0]) * 7 + int(
            digits[1]) * 3 \
              + int(digits[2]) * 1 + int(digits[3]) * 7 + int(digits[4]) * 3
        control = sum % 10
        return letters.upper() + str(control) + digits
    @staticmethod
    def create_driving_lic_number():
        with open(r'C:\Users\domin\Desktop\bd_proj\example_data_generator\src\county_numbers.csv', mode='r', encoding='utf-8') as file:
            csvFile = csv.reader(file, delimiter=';')
            chosen_row = random.choice(list(csvFile))
            county_number = str(chosen_row[0]) + str(chosen_row[1])

        digits = ''
        for _ in range(5):
            digits += str(random.randint(0, 9))

        year = str(random.choice(["%02d" % random.randint(0, 24), random.randint(50, 99)]))

        return digits + '/' + year + '/' + county_number

class Client:
    def __init__(self, person, id):
        self.pesel = ClientBuilder.create_pesel(person.gender)
        self.id_card_number = ClientBuilder.create_id_number()
        self.driving_license_number = ClientBuilder.create_driving_lic_number()
        self.person_reference = id





