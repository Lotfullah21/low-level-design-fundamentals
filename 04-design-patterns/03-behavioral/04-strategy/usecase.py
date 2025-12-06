from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount) -> None | dict:
        pass

class PaypalStrategy(PaymentStrategy):

    def pay(self, amount):
        return {
            "payment_id":"paypal_001",
            "payment_method":"paypal",
            "amount":amount
        }
    
    def __repr__(self) -> str:
        return f"Paypal"

class NetBankingStrategy(PaymentStrategy):
    def pay(self, amount):
        return {
            "payment_id":"netbanking_001",
            "payment_method":"netbanking",
            "amount":amount
        }
    
    def __repr__(self) -> str:
        return f"Net banking"
    
class PaymentService:
    def __init__(self, strategy:PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def checkout(self, amount):
        strategy = self.strategy
        if amount<0:
            raise ValueError(F"amount {amount} cannot be zero")
        result = strategy.pay(amount)
        print(f"payment is done using {strategy} strategy")
        return result
    def send_result(self):
        print("Successful payment!")
    
def payment_view(request):
    payment_method = request.get("payment_method")
    amount = request.get("amount")
    if payment_method == "paypal":
        strategy = PaypalStrategy()
    elif payment_method == "net_banking":
        strategy = NetBankingStrategy()
    else:
        print("Invalid payment method")
        return 
    service = PaymentService(strategy)
    try:
        service.checkout(amount)
        service.send_result()
    except:
        print("Unsuccessful payment")

payment_view(request={"payment_method":"paypal","amount":1000})

    