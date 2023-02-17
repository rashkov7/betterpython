from abc import ABC, abstractmethod

# TODO Liskov substitution  Principle
"""
Liskov substitution - Subtypes must be substitutable for their base types
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
# class PaymentProcessor(ABC):
#
#     @abstractmethod
#     def pay(self, order, security_code):
#         pass
#
#
# class DebitPaymentProcessor(PaymentProcessor):
#     def pay(self, order, security_code):
#         print("Processing debit payment type")
#         print(f"Verifying security code: {security_code}")
#         order.status = "paid"
#
#
# class CreditPaymentProcessor(PaymentProcessor):
#     def pay(self, order, security_code):
#         print("Processing credit payment type")
#         print(f"Verifying security code: {security_code}")
#         order.status = "paid"
#
#
# class PaypalPaymentProcessor(PaymentProcessor):
#     def pay(self, order, security_code):
#         print("Processing paypal payment type")
#         print(f"Using email address: {security_code}")
#         order.status = "paid"
#
#
# order = Order()
# order.add_item("Keyboard", 1, 50)
# order.add_item("SSD", 1, 150)
# order.add_item("USB cable", 2, 5)
#
# print(order.total_price())
# processor = PaypalPaymentProcessor()
# processor.pay(order, "hi@arjancodes.com")


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


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email):
        self.email = email

    def pay(self, order):
        print("Processing paypal payment type")
        print(f"Using email address: {self.email}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
# processor = PaypalPaymentProcessor("hi@arjancodes.com")

processor = DebitPaymentProcessor('Ab136G123')
processor.pay(order)
