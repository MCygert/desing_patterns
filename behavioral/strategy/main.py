import string
from abc import ABC, abstractmethod

from behavioral.strategy import Strategy


class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def logic(self):
        print(f"I am using {self._strategy.inform()}")


class Strategy(ABC):

    @abstractmethod
    def inform(self) -> string:
        raise Exception("Not implemented method")


class StrategyA(Strategy):

    def inform(self) -> string:
        return "A"


class StrategyB(Strategy):

    def inform(self) -> string:
        return "B"


if __name__ == "__main__":
    c1 = Context(StrategyA())
    c1.logic()
    c1.strategy = StrategyB()
    c1.logic()

