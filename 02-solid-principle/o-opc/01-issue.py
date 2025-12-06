class PaymentProcessor:
    def __init__(self, payment_type,amount=100):
        self.payment_type = payment_type
        self.amount = amount

    def process_payment(self, payment_method=None):
        if payment_method == "credit_card":
            print(f"Processing: {payment_method}")
        elif payment_method =="debit_card":
            print(f"Processing: {payment_method}")
        elif payment_method == "cash":
            print(f"Processing: {payment_method}")
        else:
            print("No payment provided")

payment_processor = PaymentProcessor("debit", 2000)
payment_processor.process_payment("credit_card")
payment_processor.process_payment("debit_card")
