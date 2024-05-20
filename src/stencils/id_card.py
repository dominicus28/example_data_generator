import random
import string

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