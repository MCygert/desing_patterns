from creational.abstract_factory.factories import AbstractFactory, VictorianFactory, ArtDecoFactory


def client(factory: AbstractFactory) -> str:
    return f"Chair style: {factory.create_chair().style} \n" \
           f"ArmChair style: {factory.create_armchair().style} \n" \
           f"Table style: {factory.create_table().style} \n"


if __name__ == "__main__":
    print(client(VictorianFactory()))
    print("-------------------")
    print(client(ArtDecoFactory()))
