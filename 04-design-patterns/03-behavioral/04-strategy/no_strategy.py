class Payment:
    def __init__(self, payment_method):
        self.payment_method = payment_method
        
    def pay(self, amount= None):
        if self.payment_method == "paypal":
            print("Processing paypal...")
        elif self.payment_method == "stripe":
            print("Processing stripe...")
        elif self.payment_method == "net_banking":
            print("Processing net banking...")
        else:
            print("Processing unknown payment...")

paypal = Payment("paypal")
stripe = Payment("stripe")
net_banking = Payment("net_banking")
credit_card = Payment("credit_card")


paypal.pay()
stripe.pay()
net_banking.pay()
credit_card.pay()
