from src.entity_creators import person_creator as prs
import numpy as np

def person_generator(limit):
    tmp = 0

    while tmp < limit:
        yield prs.Person()
        tmp += 1

def person_fabric(limit):
    persons = np.empty(shape=[0, 2])

    for i, j in enumerate(person_generator(limit)):
        persons = np.append(persons, [[i+1, j]], axis=0)

    return persons