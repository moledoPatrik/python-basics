class Item:
    # class atribute
    pay_rate = 0.8 # the pay rate after 20% discount

    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # validations
        assert price >= 0, f"Price has to be greater than zero!"
        assert quantity >= 0, f"Quantity has to be greater than zero!"
        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        # actions to execute
        Item.all.append(self)

    def calculate_value(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"

item1 = Item('Phone', 100, 5)
item2 = Item('Laptop', 1000, 3)
item3 = Item('Cable', 10, 5)
item4 = Item('Mouse', 50, 5)
item5 = Item("Keyboard", 75, 5)

# ----------- dealing with class.all -------------------------------
print(Item.all)

# for instance in Item.all:
#     print(instance.name)
# ------------------------------------------------------------------

# -------------- understanding class/instance attributes -----------
# print(Item.pay_rate)
# print(item1.pay_rate)

# print(Item.__dict__) # show attributes for class level
# print(item1.__dict__) # show attributes for instance level

# print(item1.price)
# item1.apply_discount()
# print(item1.price)

# print(item2.price)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)
# -----------------------------------------------------------------
