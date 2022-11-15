from composite_abstract import Product


class Apple(Product):
    PRICE = 0.49

    def sum_products(self) -> float:
        return self.PRICE
