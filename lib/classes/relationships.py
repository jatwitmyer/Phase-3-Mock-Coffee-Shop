from Customer import Customer
from Coffee import Coffee
from Order import Order


jerry = Customer("Jerry")
rick = Customer("Rick")
pickle_rick = Customer("Pickle Rick")
morty = Customer("Morty")

mocha = Coffee("Mocha")
latte = Coffee("Latte")
iced = Coffee("Iced")

pr_1 = Order(pickle_rick, iced, 6.0)
pr_2 = Order(pickle_rick, iced, 5.0)
m_1 = Order(morty, iced, 5.0)

# print(iced.customers)

# print(pickle_rick)
# print(iced)
# print(pr_1)
# print(iced.customers())
# print(pickle_rick.orders())
# print(morty.orders())
# print(pickle_rick.coffees())
print(iced.average_price())
# print(len(iced._orders))


Coffee(2.0)