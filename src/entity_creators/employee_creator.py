import random


class EmployeeBuilder:
    @staticmethod
    def create_position():
        positions = ['agent', 'junior specialist', 'specialist', 'logistics specialist']
        return random.choice(positions)

class Employee:
    def __init__(self, id, position):
        if position is not None:
            self.position = EmployeeBuilder.create_position()
        self.person_reference = id





