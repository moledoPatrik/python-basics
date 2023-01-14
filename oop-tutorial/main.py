class Item:
    def calculate_value(self, price, quantity):
        return price * quantity

item1 = Item()
item1.name = "Phone"
item1.price = 500
item1.quantity = 5
print(item1.calculate_value(item1.price, item1.quantity))

item2 = Item()
item2.name = "Laptop"
item2.price = 1500
item2.quantity = 3
print(item2.calculate_value(item2.price, item2.quantity))
