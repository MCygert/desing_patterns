from abc import ABC, abstractmethod


class Product(ABC):

    def add_product(self, product):
        raise Exception("Cannot add product")

    def remove_products(self):
        raise Exception("Cannot remove product")

    @abstractmethod
    def sum_products(self) -> float:
        pass
