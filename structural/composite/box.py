from composite_abstract import Product


class Box(Product):
    PRICE = 0.15
    items_inside = []

    def add_product(self, product: Product):
        self.items_inside.append(product)

    def remove_products(self):
        del self.items_inside[-1]

    def sum_products(self) -> float:
        sum_of_products = self.PRICE
        for product in self.items_inside:
            sum_of_products += product.sum_products()
        return sum_of_products
