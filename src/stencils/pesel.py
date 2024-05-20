import src.utilities as utils
import random
from datetime import datetime, timedelta


def gen_datetime(min_year=1900, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)

    return start + (end - start) * random.random()


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


def create_pesel(gender=None):
    if gender is None:
        gender = random.choice(['M', 'F'])
    date = gen_datetime()
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
        gender_digit = ((random.randint(0, 10) * 2) - 1) % 10

    part_pesel += str(gender_digit)
    sum = multiply_part(part_pesel)

    if sum == 10:
        ctrl_digit = 0
    elif sum > 9:
        ctrl_digit = 10 - (sum % 10)
    else:
        ctrl_digit = 10 - sum

    final_pesel = part_pesel + str(ctrl_digit)

    return final_pesel