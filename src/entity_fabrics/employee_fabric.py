from src.entity_creators import employee_creator as empl
import numpy as np

def employee_generator(id, position):
    yield empl.Employee(id, position)

def employee_fabric(limit, persons, position):
    employees = np.empty(shape=[0, 2])
    indexes = []

    def choose_index(indexes):
        while True:
            index = np.random.choice(persons.shape[0], replace=False)
            if index in indexes:
                continue
            else:
                indexes.append(index)
                break
        return indexes


    for i in range(limit):
        choose_index(indexes)
        employee = next(employee_generator(persons[indexes[-1]][0], position))
        employees = np.append(employees, [[i+1, employee]], axis=0)

    return employees