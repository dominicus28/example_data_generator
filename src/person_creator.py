import utilities as utils
import random
import string
import mysql_config as mysql
from datetime import datetime, timedelta


class PersonBuilder:
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
        date = PersonBuilder.gen_datetime()
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
        sum = PersonBuilder.multiply_part(part_pesel)

        if sum == 10:
            ctrl_digit = 0
        elif sum > 9:
            ctrl_digit = 10 - (sum % 10)
        else:
            ctrl_digit = 10 - sum

        final_pesel = part_pesel + str(ctrl_digit)

        return final_pesel

    @staticmethod
    def create_telephone():
        return '+48' + str(random.randint(100000000, 999999999))

    @staticmethod
    def create_mail():
        domains = ['gmail.com', 'wp.pl', 'yahoo.com', 'hotmail.com', 'outlook.com', 'interia.pl']

        def random_char(char_num):
            return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

        return random_char(random.randint(5, 20)) + '@' + domains[random.randint(0, len(domains)-1)]

    @staticmethod
    def select_random_person():
        mysql.mycursor.execute("SELECT * FROM person ORDER BY RAND() LIMIT 1")

        myresult = mysql.mycursor.fetchone()

        return myresult

    @staticmethod
    def select_random_surname(gender):
        sql = "SELECT * FROM person_surname WHERE gender = %s ORDER BY RAND() LIMIT 1"
        gen = (gender, )

        mysql.mycursor.execute(sql, gen)

        myresult = mysql.mycursor.fetchone()

        return myresult

class Person:
    def __init__(self):
        self.row = PersonBuilder.select_random_person()
        self.name = self.row[0]
        self.gender = self.row[1]
        self.surname = PersonBuilder.select_random_surname(self.gender)[0]
        self.mail = PersonBuilder.create_mail()
        self.telephone = PersonBuilder.create_telephone()
        self.pesel = PersonBuilder.create_pesel(self.row[1])





