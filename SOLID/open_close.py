from abc import ABC, abstractmethod
# TODO OPEN/CLOSE Principle
"""
OPEN/CLOSE Principle - open for extension close for modification
"""

# class Order:
#
#     def __init__(self):
#         self.items = []
#         self.quantities = []
#         self.prices = []
#         self.status = "open"
#
#     def add_item(self, name, quantity, price):
#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
#
#     def total_price(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total
#
#
# class PaymentProcessor:
#     def pay_debit(self, order, security_code):
#         print("Processing debit payment type")
#         print(f"Verifying security code: {security_code}")
#         order.status = "paid"
#
#     def pay_credit(self, order, security_code):
#         print("Processing credit payment type")
#         print(f"Verifying security code: {security_code}")
#         order.status = "paid"
#
#
# order = Order()
# order.add_item("Keyboard", 1, 50)
# order.add_item("SSD", 1, 150)
# order.add_item("USB cable", 2, 5)
#
# print(order.total_price())
# processor = PaymentProcessor()
# processor.pay_debit(order, "0372846")

class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentBase(ABC):

    @abstractmethod
    def pay(self, order, security_code):
        pass


class DebitPeyment(PaymentBase):

    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


class CreditPeyment(PaymentBase):

    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = DebitPeyment()
processor.pay(order, "0372846")
