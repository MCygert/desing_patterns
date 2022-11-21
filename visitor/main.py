from __future__ import annotations

from typing import List

from visitor.visitor import Visitor, ConcreteVisitor1, ConcreteVisitor2
from visitor.components import Component, ConcreteComponentA, ConcreteComponentB


def client_code(components: List[Component], visitor: Visitor) -> None:
    for component in components:
        component.accept(visitor)


if __name__ == "__main__":
    components = [ConcreteComponentA(), ConcreteComponentB()]

    print("The client code works with all visitors via the base Visitor interface:")
    visitor1 = ConcreteVisitor1()
    client_code(components, visitor1)

    print("It allows the same client code to work with different types of visitors:")
    visitor2 = ConcreteVisitor2()
    client_code(components, visitor2)