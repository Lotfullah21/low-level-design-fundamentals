from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def get_name(self) ->None| str:
        pass

class CreditCardProcessor(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing Credit Card...")

    def get_name(self):
        return "Credit card"

    
class NetBankingProcessor(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing Credit Card...")

    def get_name(self):
        return "Credit card"
    
class PayPalPayment(PaymentMethod):
    def __init__(self, email):
        self.email = email
    
    def process(self, amount):
        print(f"Processing ${amount} via PayPal account: {self.email}")
        # PayPal specific logic
        # Redirect to PayPal
        # Handle OAuth
        return {
            "status": "success",
            "transaction_id": "PP456",
            "method": self.get_name()
        }
    
    def get_name(self):
        return "PayPal"
    
class BitcoinPayment(PaymentMethod):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
    
    def process(self, amount):
        print(f"Processing ${amount} via Bitcoin to {self.wallet_address}")
        # Bitcoin specific logic
        # Generate QR code
        # Wait for blockchain confirmation
        return {
            "status": "pending",
            "transaction_id": "BTC789",
            "method": self.get_name()
        }
    
    def get_name(self):
        return "Bitcoin"
class CashProcessor(PaymentMethod):

    def process_payment(self, amount):
        print(f"Processing Credit Card...")

    def get_name(self):
        return "Credit card"

credit_card_processor = CreditCardProcessor()
credit_card_processor.process_payment(1000)
