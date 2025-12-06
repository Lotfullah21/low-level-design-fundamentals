from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def payment(self):
        pass

class CreditCardService(PaymentGateway):
    def payment(self):
        print("Processing credit card payment...")

class PaypalService(PaymentGateway):
    def payment(self):
        print("Processing paypal payment...")

class CheckoutManager:
    def __init__(self, payment_service:PaymentGateway):
        self.payment_service = payment_service

    def process_checkout(self):
        self.payment_service.payment()

credit_card_service = CreditCardService()
checkout_manager = CheckoutManager(credit_card_service)
checkout_manager.process_checkout()

## Now, I want to change the service to credit card, what to do? Just change the gateway

paypal_card_service = PaypalService()
checkout_manager = CheckoutManager(paypal_card_service)
checkout_manager.process_checkout()
