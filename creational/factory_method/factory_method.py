from abc import ABC, abstractmethod


class Chair(ABC):

    @abstractmethod
    def response(self) -> str:
        pass


class OldChair(Chair):

    def response(self) -> str:
        return "I am old chair"


class NewChair(Chair):

    def response(self) -> str:
        return "I am new chair"


class ChairCreator(ABC):

    def say_what_i_am(self):
        print(self.create_chair().response())

    @abstractmethod
    def create_chair(self) -> Chair:
        pass


class NewChairCreator(ChairCreator):

    def create_chair(self) -> Chair:
        return NewChair()


class OldChairCreator(ChairCreator):

    def create_chair(self) -> Chair:
        return OldChair()
