import csv

class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price has to be greater than zero!"
        assert quantity >= 0, f"Quantity has to be greater than zero!"
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_value(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # I think this changes the representation of an instance
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"

    # our first class method // cls == class
    @classmethod
    def instantiate_from_csv(cls):
        with open('/Users/patrik/code/moledoPatrik/projects-dumpster/python-basics/oop-tutorial/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero
        if isinstance(num, float):
            # count out floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

Item.instantiate_from_csv()
print(Item.all)

# using static method
# print(Item.is_integer(5.2))
# print(Item.is_integer(5.0))
# print(Item.is_integer(5))
