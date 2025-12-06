class Mathematics:
    def __init__(self,name, duration):
        self.duration = duration
        self.name = name
    
class ArtificialIntelligence(Mathematics):
    def __init__(self,name,duration):
        super().__init__(name,duration)
        
class Programming(Mathematics):
    def __init__(self,name, duration):
        super().__init__(name,duration)
   

maths = Mathematics("Computation","6 years")
aritificialIntelligence = ArtificialIntelligence("statistics","6 months")
programming = Programming("Logic","6 months")

print(maths.name)
print(aritificialIntelligence.name)
print(programming.name)