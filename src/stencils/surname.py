import src.mysql_config as mysql
import random

def select_random_surname(gender=None):
    if gender is None:
        gender = random.choice(['M', 'F'])
    sql = "SELECT * FROM person_surname WHERE gender = %s ORDER BY RAND() LIMIT 1"
    gen = (gender,)

    mysql.mycursor.execute(sql, gen)

    myresult = mysql.mycursor.fetchone()

    return myresult[0]
