from faker import Faker
from faker.providers import BaseProvider
import random

towns = ["Wrocław", "Poznań", "Katowice", "Warszawa", "Olsztyn", "Łódź",
         "Szczecin", "Bydgoszcz", "Białystok", "Lublin", "Kraków", "Gdańsk"]

class CustomAddressProvider(BaseProvider):
    def town(self):
        return random.choice(towns)

fake = Faker(['pl_PL'])
fake.add_provider(CustomAddressProvider)

def generate_random_address(scope):
    if scope == "town":
        return fake.town()
    elif scope == "street":
        return fake.street_name()
    elif scope == "postal_code":
        return fake.postcode()
    elif scope == "coordinates":
        return "Point({} {})".format(str(fake.latitude()), str(fake.longitude()))
