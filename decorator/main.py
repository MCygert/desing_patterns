from decorator.components import Component, ConcreteComponent, ConcreteDecoratorA, ConcreteDecoratorB


def client(component: Component) -> None:
    print(f"Result = {component.operation()}", end="")


if __name__ == "__main__":
    simple = ConcreteComponent()
    print("Basic")
    client(simple)

    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("More complicated one")
    client(decorator2)

# Best analogy -> pizza
# ConcreteComponent -> bottom of pizza
# DecoratorComponents would be toppings
# Every topping would give some price and at the end it could count sum
