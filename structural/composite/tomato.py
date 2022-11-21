from composite_abstract import Product


class Tomato(Product):
    PRICE = 0.14

    def sum_products(self) -> float:
        return self.PRICE
