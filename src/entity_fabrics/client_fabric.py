from src.entity_creators import client_creator as clnt
import numpy as np

def client_generator(person, id):
    yield clnt.Client(person, id)

def client_fabric(limit, persons):
    clients = np.array([])
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

    choose_index(indexes)

    for _ in range(limit):
        client = next(client_generator(persons[indexes[-1]][1], persons[indexes[-1]][0]))
        clients = np.append(clients, [client], axis=0)
        choose_index(indexes)

    return clients