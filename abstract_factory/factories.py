from abc import ABC


class Chair:
    def __init__(self, style: str):
        self.style = style


class ArmChair:
    def __init__(self, style: str):
        self.style = style


class Table:
    def __init__(self, style: str):
        self.style = style


class AbstractFactory(ABC):

    def create_chair(self) -> Chair:
        pass

    def create_armchair(self) -> ArmChair:
        pass

    def create_table(self) -> ArmChair:
        pass


class VictorianFactory(AbstractFactory):
    _style = "Victorian"

    def create_chair(self) -> Chair:
        return Chair(self._style)

    def create_armchair(self) -> ArmChair:
        return ArmChair(self._style)

    def create_table(self) -> Table:
        return Table(self._style)


class ArtDecoFactory(AbstractFactory):
    _style = "Art-Deco"

    def create_chair(self) -> Chair:
        return Chair(self._style)

    def create_armchair(self) -> ArmChair:
        return ArmChair(self._style)

    def create_table(self) -> Table:
        return Table(self._style)

# Every product should inherit from abstract chair table etc.
# So it should be VictorianTable instead
