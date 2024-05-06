from src.entity_creators import person_creator as prs
import numpy as np

def person_generator(limit, name, gender, surname, telephone, mail):
    tmp = 0

    while tmp < limit:
        yield prs.Person(name, gender, surname, telephone, mail)
        tmp += 1

def person_fabric(limit, name, gender, surname, telephone, mail):
    persons = np.empty(shape=[0, 2])

    for i, j in enumerate(person_generator(limit, name, gender, surname, telephone, mail)):
        persons = np.append(persons, [[i+1, j]], axis=0)

    return persons