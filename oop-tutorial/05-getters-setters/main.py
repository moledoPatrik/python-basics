from item import Item
from phone import Phone

# Item.instantiate_from_csv()
# print(Item.all)

item1 = Item("MyItem", 750)
print(item1.name)

# encapsulation: mechanism to of restricting direct access to some attr of the program
# we encapsulated price and created an method to change it
print(item1.price)
item1.apply_increment(0.2)
print(item1.price)

# abstraction, shows only necessary attr and hide the unnecessary info
# send email uses other methods that are not accessible to the user
item2 = Item("Item", 800, 6)
item2.send_email()

# inheritance allow us to reuse code from across our classes
# send_email is a method from the Item class, but as Phone inherits from Item
# it has access to the Item methods!
item3 = Phone("Iphone", 1200, 10)
item3.send_email()

# polymorphism: use of a single type entity (like a method) to represent different types
# poly == many // morphism == forms
# example: len() handling strings, arrays, multiple data types
print(item3.price)
item3.apply_discount()
print(item3.price)
# apply_discount() is a method of the Item class but knows how
# to handle the Phone class (another example of polymorphism)

# inheritance and polimorphysm sometimes are refered together
# it just makes sense

# --------------------

# SETTING AN ATTRIBUTE
# item1.name = 'Patrik'
# GETTING AN ATTRIBUTE
# print(item1.name)

# --------------------

# doesnt work with __
# item1.__name = 'hi'

# --------------------
