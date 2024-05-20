import random
import string

def create_mail():
    domains = ['gmail.com', 'wp.pl', 'yahoo.com', 'hotmail.com', 'outlook.com', 'interia.pl']

    def random_char(char_num):
        return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

    return random_char(random.randint(5, 20)) + '@' + domains[random.randint(0, len(domains) - 1)]