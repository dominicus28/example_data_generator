import random
from datetime import datetime, timedelta

def generate_random_datetime():
    start_datetime = datetime.now()
    end_datetime = start_datetime + timedelta(days=2*30)
    start_datetime = datetime.strptime(start_datetime.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    end_datetime = datetime.strptime(end_datetime.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')

    delta = (end_datetime - start_datetime).total_seconds()

    random_seconds = random.randint(0, int(delta))

    random_datetime = start_datetime + timedelta(seconds=random_seconds)

    return random_datetime.strftime('%Y-%m-%d %H:%M:%S'), (random_datetime+delta)