import src.mysql_config as mysql
import random

def select_random_car():
    sql = "SELECT * FROM car ORDER BY RAND() LIMIT 1"

    mysql.mycursor.execute(sql)

    myresult = mysql.mycursor.fetchone()

    return myresult

