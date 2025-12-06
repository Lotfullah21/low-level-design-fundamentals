## Strategy

The core idea of the Strategy Pattern is to define a family of algorithms, encapsulate each one as a separate class, and make them interchangeable at runtime.

Instead of writing complex conditional logic (if type == A: do A, else: do B) inside the main class (the Context), we delegate the execution to a specialized Strategy object.

`Simple analogy`: Travel to work - you can choose car, bus, bike, or walk. Same goal (reach work), different strategies.

### When to use:

- variable business rules (pricing, validation, retries, duplicate-handling), choosing storage backends, formatting/serialization.
- Change behavior without changing code.

### Avoid:

over-engineering when a simple if/elif or a dict of functions is enough; strategies that need tons of context (leaky abstractions).

When to Use Strategy Pattern

## When to Use Strategy Pattern

| Use Case                            | Use Strategy | Don't Use Strategy |
| ----------------------------------- | ------------ | ------------------ |
| Multiple ways to do the same thing  | Yes          | No                 |
| Algorithm chosen at runtime         | Yes          | No                 |
| Avoid large if/elif chains          | Yes          | No                 |
| Payment gateways, storage providers | Yes          | No                 |
| Only one way to do something        | No           | Yes                |
| Algorithm never changes             | No           | Yes                |
| Simple if/else logic                | No           | Yes                |
| Static, predictable logic           | No           | Yes                |

### **Rule:**

If we have **3+ interchangeable ways** to do the same thing, use the **Strategy Pattern**.

## Usage Frequency in Django

| Context            | Frequency   | Why                      |
| ------------------ | ----------- | ------------------------ |
| Payment processing | Very common | Stripe, PayPal, Razorpay |
| File storage       | Very common | Local, S3, Google Cloud  |
| Authentication     | Common      | JWT, OAuth, API Key      |
| Notifications      | Common      | Email, SMS, Push         |

## No strategy

```py
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
```

```py
# Different payment strategies
class StripePayment:
    def pay(self, amount):
        # Stripe logic
        pass

class PayPalPayment:
    def pay(self, amount):
        # PayPal logic
        pass

# Use whichever
payment = StripePayment() if user.prefers_stripe else PayPalPayment()
payment.pay(100)
```
