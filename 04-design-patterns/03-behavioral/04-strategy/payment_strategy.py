from abc import ABC, abstractmethod

# Abstract Strategy
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self):
        pass

# Concrete Strategies
class Paypal(PaymentStrategy):
    def pay(self):
        print("Processing paypal...")

class CreditCard(PaymentStrategy):
    def pay(self):
        print("Processing credit card...")
    
class NetBanking(PaymentStrategy):
    def pay(self):
        print("Processing net banking")

# Service
class PaymentService:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy
    
    def pay(self):
        self.strategy.pay()


# Usage
service = PaymentService(Paypal())
service.pay()