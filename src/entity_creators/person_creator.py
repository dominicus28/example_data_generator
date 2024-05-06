import random
import string
import src.mysql_config as mysql


class PersonBuilder:
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
    def __init__(self, name, gender, surname, telephone, mail):
        row = PersonBuilder.select_random_person()
        if name is not None:
            self.name = row[0]
        if gender is not None:
            self.gender = row[1]
        if surname is not None:
            self.surname = PersonBuilder.select_random_surname(self.gender)[0]
        if telephone is not None:
            self.telephone = PersonBuilder.create_telephone()
        if mail is not None:
            self.mail = PersonBuilder.create_mail()





