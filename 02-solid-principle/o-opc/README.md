## O - Open/Closed Principle (OCP)

Software entities (classes, modules, functions) should be OPEN for extension but CLOSED for modification.

In simple terms:

- `OPEN` for extension: You can add new functionality/behavior
- `CLOSED` for modification: You don't change existing, tested code

### Why OCP Matters?

1. Prevents Breaking Existing Code

- Old, tested code remains untouched
- No risk of introducing bugs in working features
- Changes are isolated to new code

2. Easier to Add Features

   - New requirements don't require editing multiple files
   - Less merge conflicts in teams
   - Faster development

3. Better Testing

   - Existing tests remain valid
   - Only need to test new code
   - Reduces regression testing

4. Supports Plugin Architecture
   - Add features without modifying core system
   - Third-party extensions possible
   - Examples: VS Code extensions, WordPress plugins

#### Real-World Analogy

Think of a USB port:

`CLOSED for modification`: The USB port design doesn't change
`OPEN for extension`: You can plug in mouse, keyboard, webcam, printer, etc.

If USB ports required modification every time we wanted to connect a new device, it would be a nightmare!

### Real examples

Let's consider this example for a payment processor.

```py
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
```

### Problem

Now, a new payment method is famous in the market, Bitcoin; what to do?
Add a new `elif` condition and solve the issue, but it violates the OCP which is do not modify existing code, extend the current code.

HOW CAN WE EXTEND AN EXISTING CODEBASE?

### Solution

In python, we can create a single abstract class with methods and for each method type, create a new class.

#### Benefits:

- No modification: PaymentProcessor never changes
- Easy extension: Just add new PaymentMethod class
- Safe: Existing payment methods untouched
- Testable: Test each payment method independently
- No if/else chains: Polymorphism handles different behaviors
- Plugin-ready: Third parties can add payment methods

##### How OCP Works: The Strategy Pattern

The key to OCP is abstraction and polymorphism:

Without abstraction

```py
# Without abstraction - we CHECK the type
def process_payment(payment_type, amount):
    if payment_type == "credit_card":
        # credit card code
    elif payment_type == "paypal":
        # paypal code
    elif payment_type == "bitcoin":  # NEW - must MODIFY this function!
        # bitcoin code
```

`Problem`: Every new payment type requires MODIFYING this function.

`The Solution: Abstraction + Polymorphism`

##### 1. Abstraction = Define a Common Interface

```py
class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount):
        # every payment method MUST have a process() method"
        pass
```

`Abstraction says: "All payment methods should have this shape/contract"`

##### 2. Polymorphism = Different Implementations, Same Interface

```py
# Each class implements the SAME method differently
class CreditCard(PaymentMethod):
    def process(self, amount):
        print("Processing via Credit Card")

class PayPal(PaymentMethod):
    def process(self, amount):
        print("Processing via PayPal")

 # NEW - just ADD, don't MODIFY
class Bitcoin(PaymentMethod):
    def process(self, amount):
        print("Processing via Bitcoin")
```

`Polymorphism says: "Different classes can respond to the same method call in their own way"`

```py
def process_payment(payment_method: PaymentMethod, amount):
    payment_method.process(amount)

# Usage
credit_card = CreditCard()
paypal = PayPal()
bitcoin = Bitcoin()

process_payment(credit_card, 100)
process_payment(paypal, 50)
process_payment(bitcoin, 200)

```

```py
# Abstract interface defines the contract
class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass

# New behaviors are added as new classes
class StrategyA(Strategy):
    def execute(self):
        # Implementation A
        pass

class StrategyB(Strategy):
    def execute(self):
        # Implementation B
        pass

# Client code works with abstractions
class Context:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def do_something(self):
        self.strategy.execute()
```

#### Real-World Applications

### 1. Web Frameworks

- Django middleware: Add features without modifying core
- Express.js middleware: Chain request handlers

### 2. Payment Gateways

- Stripe, PayPal, Square plugins
- Add new gateway without changing checkout code

### 3. Logging Systems

- Log to console, file, database, cloud
- Add new log destination without changing logger

### 4. Authentication

- OAuth, JWT, API keys, SAML
- Add new auth method without changing auth service

### 5. Cloud Storage

- AWS S3, Google Cloud, Azure, local storage
- Switch storage provider without changing app code
