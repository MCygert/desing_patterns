from apple import Apple
from box import Box
from tomato import Tomato

if __name__ == '__main__':
    box1 = Box()
    box1.add_product(Tomato())
    box1.add_product(Apple())
    box1.add_product(Tomato().add_product(Tomato()))
    print(box1.sum_products())
