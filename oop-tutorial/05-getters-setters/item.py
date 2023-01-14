import csv

# __ makes a private attribute/methods

class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price has to be greater than zero!"
        assert quantity >= 0, f"Quantity has to be greater than zero!"
        self.__name = name
        self.__price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    # makes it read only
    @property
    def name(self):
        print('using getter')
        return self.__name

    # you can reassign a value
    @name.setter
    def name(self, value):
        print('using setter')
        if len(value) > 10:
            raise Exception("The name is too long (should have 10 or less letters)")
        else:
            self.__name = value

    def calculate_value(self):
        return self.__price * self.quantity



    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', '{self.quantity}')"

    def __connect(self, smtp_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello, someone.
        We have {self.quantity}x {self.name}(s)
        Regards, store.com
        """

    def __send(self):
        pass

    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()

    @classmethod
    def instantiate_from_csv(cls):
        with open('/Users/patrik/code/moledoPatrik/projects-dumpster/python-basics/oop-tutorial/05-getters-setters/items.csv', 'r') as f:
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
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
