from src.entity_creators import client_creator as clnt
import numpy as np

def client_generator(person, id, pesel, id_card_number, driving_license_number):
    yield clnt.Client(person, id, pesel, id_card_number, driving_license_number)

def client_fabric(limit, persons, pesel, id_card_number, driving_license_number):
    clients = np.empty(shape=[0, 2])
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

    for _ in range(limit):
        choose_index(indexes)
        pesels = []
        while True:
            client_candidate = next(client_generator(persons[indexes[-1]][1], persons[indexes[-1]][0],
                                                     pesel, id_card_number, driving_license_number))
            if client_candidate.pesel not in pesels:
                pesels.append(client_candidate.pesel)
                client = client_candidate
                break

        clients = np.append(clients, [[int(client.pesel), client]], axis=0)

    return clients