import copy
from abc import ABC, abstractmethod
import time


class Prototype(ABC):
    def __init__(self):
        time.sleep(3)
        self.height = None
        self.age = None
        self.defense = None
        self.attack = None

    @abstractmethod
    def clone(self):
        pass


class Shopkeeper(Prototype):
    def __init__(self, height, age, defense, attack):
        super().__init__()
        time.sleep(3)
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        self.charisma = 30

    def clone(self):
        return copy.deepcopy(self)


class Warrior(Prototype):
    def __init__(self, height, age, defense, attack):
        self.stamina = 60

    def clone(self):
        return copy.deepcopy(self)
