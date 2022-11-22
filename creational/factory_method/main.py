from creational.factory_method.factory_method import OldChairCreator


def client_code(type_of_house: str):
    if type_of_house == "old":
        OldChairCreator().create_chair()