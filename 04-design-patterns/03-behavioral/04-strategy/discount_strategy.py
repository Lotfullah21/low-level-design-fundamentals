from abc import ABC, abstractmethod

# Strategy interface
class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, amount: float) -> float: ...

# Concrete strategies
class NoDiscount(DiscountStrategy):
    def apply(self, amount: float) -> float: return amount

class PercentDiscount(DiscountStrategy):
    def __init__(self, pct: float): self.pct = pct
    def apply(self, amount: float) -> float: return amount * (1 - self.pct/100)

class TieredDiscount(DiscountStrategy):
    def apply(self, amount: float) -> float:
        if amount >= 1000: return amount * 0.85   # 15% off
        if amount >= 500:  return amount * 0.90   # 10% off
        return amount

# Context uses a Strategy
class Checkout:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy
    def total(self, subtotal: float) -> float:
        return round(self.strategy.apply(subtotal), 2)

# Usage (swap at runtime)
checkout = Checkout(PercentDiscount(12.5))
print(checkout.total(800))       # 700.0
checkout.strategy = TieredDiscount()
print(checkout.total(800))       # 720.0
