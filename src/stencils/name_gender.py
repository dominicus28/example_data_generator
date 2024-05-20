import src.mysql_config as mysql

def select_random_person():
    mysql.mycursor.execute("SELECT * FROM person ORDER BY RAND() LIMIT 1")

    myresult = mysql.mycursor.fetchone()

    return myresult[0], myresult[1]