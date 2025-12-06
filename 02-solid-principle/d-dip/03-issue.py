# class Paypal:
#     def process_payment(self):
#         print("Processing paypal payment")

# class Checkout:
#     payment_service = Paypal()
#     def process_checkout(self):
#         self.payment_service.process_payment()


# ch1 = Checkout()
# ch1.process_checkout()

## Now, I want to change the service to credit card, what to do? Change the business logic in Checkout


class Paypal:
    def process_payment(self):
        print("Processing paypal payment")

class CreditCard:
    def process_payment(self):
        print("Processing credit card payment")

class Checkout:
    # payment_service = Paypal()
    payment_service = CreditCard()
    def process_checkout(self):
        self.payment_service.process_payment()

ch1 = Checkout()
ch1.process_checkout()