from abc import ABC, abstractmethod

# Strategy interface
class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount, user):
        pass

# Concrete strategies
class StripeStrategy(PaymentStrategy):
    def process_payment(self, amount, user):
        # Stripe-specific logic
        return {
            'status': 'success',
            'gateway': 'Stripe',
            'transaction_id': 'stripe_12345',
            'amount': amount
        }

class PayPalStrategy(PaymentStrategy):
    def process_payment(self, amount, user):
        # PayPal-specific logic
        return {
            'status': 'success',
            'gateway': 'PayPal',
            'transaction_id': 'paypal_67890',
            'amount': amount
        }

# Context
class PaymentService:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: PaymentStrategy):
        """Change strategy at runtime"""
        self.strategy = strategy
    
    def checkout(self, amount, user):
        # Validation
        if amount <= 0:
            raise ValueError("Invalid amount")
        
        # Process using strategy
        result = self.strategy.process_payment(amount, user)
        
        # Post-processing
        self._send_receipt(user, result)
        return result
    
    def _send_receipt(self, user, result):
        # Send receipt email
        pass

# Usage in views
class CheckoutView(APIView):
    def post(self, request):
        payment_method = request.data.get('payment_method')
        amount = request.data.get('amount')
        
        # Select strategy based on user choice
        if payment_method == 'stripe':
            strategy = StripeStrategy()
        elif payment_method == 'paypal':
            strategy = PayPalStrategy()
        else:
            return Response({'error': 'Invalid payment method'}, status=400)
        
        # Process payment
        service = PaymentService(strategy)
        result = service.checkout(amount, request.user)
        
        return Response(result)