# Class

Class is a moulds for the kind of object we intend to create.

whenever the class is called, we are creating an object of that class, in fact a class also called data type, where we are having the freedom to add features, types and methods to that data type.

class is definition of the new data type and the object is representation or instantiation of that data type.

## Attributes:

- The variables used inside a class is called attributes (instance variable).
- In object-oriented programming, an attribute is a piece of information or a characteristic associated with an object.
- Objects are instances of classes, and classes defines the blueprint for objects.

## Methods:

Functions inside a class is known as methods.

## `__init__` (instance method):

It is used to initialize the contents of an object inside a class.

Using `__init__` method, we are laying the foundation of the variables that are going to be allowed inside a class (mould), Otherwise others can add their own variables inside a class (blueprint).

By doing so, we have more control on the intended object's creation, just as we add keys to dictionaries or values to arrays, here we are adding variables to our class.
In other words we are defining what those attributes can be and cannot be inside our class.

```py

class Details:
    def __init__(self,name, duration):
        self.name = name
        self.duration = duration

def main():
    details = get_info()
    print(f"{details.name} will take {details.duration} months to master. ")

def get_info():
    details = Details()
    name = input("Name: ")
    duration = input("Duration: ")
    details = Details(name, duration)
    return details

if __name__ == "__main__":
    main()
```

### Two major steps

#### 1. Initialization:

initializes the contents of the object.

```py
 def __init__(self,name, duration):
        self.name = name
        self.duration = duration

# fill the just created empty object with name and duration and save in computer memory.
# self.name and self.duration can be any name, but the naming should be self explanatory.

```

#### 2. Constructor call:

it construct an object out of the mould we have made under the class name.
it uses our class as template so that every object have the same structure, but we can customize the contents of the object.

```py
new_object_name = class_name(instance_variables)
```

as the execution starts, when it reaches to instance construction, it will create an empty object inside the computer memory.
when it calls that instance, it will directly move upward and calls **init** method, and in there using self, the values saved inside the object in computer memory.
we can use any thing instead of self, but it is the convention to use this name. the reason behind having that extra variable(self) is to point to the current object variables that we just created and use it in other place inside the class.

## self:

self acts as a reference to the instance, allowing you to access its attributes and methods.

### **str**(self)

if we can an object directly in a function like print, we will see only the address of that object.
if we want see the string representation of our object we can use **str** instance method.
using self, we are having access to the current object and we can call that object, whenever print(object) is called, it will trigger the **str**(self) method.

### Property

properties are a way to access and manipulate attributes through methods (getter, setter, and deleter methods).

a property is a special kind of attribute that is accessed like a normal attribute but is implemented using methods known as getter, setter, and deleter.
Properties allow you to define custom behavior for getting, setting, and deleting an attribute.

the main reason behind using property is to have controlled access to the property of an object.

#### Decorators:

functions that modify or extend the behavior of other functions.
Decorators are commonly used for tasks like logging, authentication, measuring execution time, and more.

#### Components of property

Usually, we use from three components

1. #### Getter:
   it is responsible for getting value of an attribute
   use py`@property` decorator to create a read-only property

```py
@property
def subject(self):
    return self._subject
```

2. ### Setter:
   a setter method is responsible for setting value of an attribute
   decorate a method by `py method_name.setter` to create a setter for a specific property

```py
@subject.setter
def subject(self, value):
    self._subject = value
```

3. ### Deleter:

   a deleter method is responsible for an attribute (a specific information about an object present in the class)
   Decorate a method with py`@<property_name>.deleter` to create a deleter for a specific property.

   ```py
   @property
   def subject(self):
       del self._subject
   ```

   it is a naming convention that the attribute name and its properties be the same.

## Class Variables and Class methods

1. ### Class Variables:
   class variables are shared among all instance of a class and can be accessed directly.
   `py className.classMethod`
   even if we have different objects, but this value will be shared among all of them.

```py

   class Subjects:
    ai_core = "mathematics"  # Class variable

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

# Accessing class variable
print(Subjects.ai_core)  # Output: 0

# Creating instances
obj1 = Subjects(1)
obj2 = Subjects(2)

# Modifying class variable
Subjects.ai_core = "statistics"
print(obj1.ai_core) ## statistics
print(obj2.ai_core) ## statistics

```

2. ### Class Methods:
   Class methods are methods that are related to the class only and not the instance of the class. They are defined using the @classmethod decorator.

## Inheritance

```py
class Mathematics:
    def __init__(self,name, duration):
        self.duration = duration
        self.name = name
        ...



class ArtificialIntelligence:
    def __init__(self,name, duration):
        self.duration = duration
        self.name = name
        ...

class Programming:
    def __init__(self,name, duration):
        self.duration = duration
        self.name = name
        ...


maths = Mathematics("Computation","6 years")
aritificialIntelligence = ArtificialIntelligence("statistics","4 years")
programming = Programming("Logic","6 months")

```

in the above code, Mathematics is the parent class and the other classes are known as child class.
we add in parenthesis the name of the class that the child class is going to inherit and inside the child's init method, we call the parent's init method.
the super() refers to the super or parent class of child class.
we say call the init method of child class.

one thing should be noted is that all the parameters or attributes of the parent class should be present in child class and vice versa, other wise the TypeError will be triggered.

## Operator OverLoading

```py

class Course:
    def __init__(self, name,prerequisite, duration):
        self.name = name
        self.prerequisite = prerequisite
        self.duration = duration


    def __str__(self):
        return f"{self.name} requires {self.prerequisite} as its prerequisite and it takes {self.duration} months to complete. "

machineLearning = Course("Machine learning","Statistics",6)
deepLearning = Course("Deep learning","Calculus",4)

duration = machineLearning.duration + deepLearning.duration
prerequisites = machineLearning.prerequisite + " and " + deepLearning.prerequisite
name = machineLearning.name + " and " + deepLearning.name

print(name)
print(prerequisites)
print(duration)


```

Using operator overloading allowed us to define on common instance method and we can use as many times as we want.

```py
class Course:
    def __init__(self, name,prerequisite, duration):
        self.name = name
        self.prerequisite = prerequisite
        self.duration = duration


    def __str__(self):
        return f"{self.name} requires {self.prerequisite} as its prerequisite and it takes {self.duration} months to complete. "

    # self refers whatever object on the left and other refers to the object on the right side of + operator.
    def __add__(self, other):
        duration = self.duration + other.duration
        prerequisites = self.prerequisite + " and " + other.prerequisite
        name = self.name + " and " + other.name
        # after object on the left and object on the right together, return one new object with the resulted operations.
        return Course(name,prerequisites,duration)

machineLearning = Course("Machine learning","Statistics",6)
deepLearning = Course("Deep learning","Calculus",3)

new_course = machineLearning + deepLearning
print(new_course)

```

### Compile Time Polymorphism(Method Overloading):

Python does not support method overloading in the same way as statically typed languages like Java or C++, where the compiler selects the appropriate method based on the types and number of arguments. However, Python offers a more flexible approach using default parameter values and variable-length argument lists.

### Run Time Polymorphism(method overloading):

when a sub-class has the same structure, same name and same parameters as its super class, it will override the method in its super class.

```py
class Physics:
    def at_your_core(self):
        return "Explaining Universe"

class Maths(Physics):
    def at_your_core(self):
        return "Universe Language"

class Programming(Maths):
    def at_your_core(self):
        return "Logic"

# Creating instances of Physics, Maths, and Programming.
physics = Physics()
maths = Maths()
programming = Programming()
# Calling overridden methods
print(physics.at_your_core())  # Output: Explaining Universe
print(maths.at_your_core())  # Output: Universe Language
print(programming.at_your_core())  # Output: Logic

```

From above block of code, we can see all of them are having same method name, but the later ones are overriding the earlier ones methods.

##### How Objects are stored in memory?

The heap and the stack are both regions of memory used for different purposes, and they are physically located in the computer's RAM (Random Access Memory).

## Heap

heap is a region of memory where dynamic allocation of memory happens;
functions,classes, objects, lists, dictionaries and data structure types are stored in heap.
when a class is created, a particular memory location will be assigned to that object in heap.

## Stack

This is a region of memory where function calls and local variables related to that function will be stored.
it also contains the information about a particular function's location where it was called.
If a function is called by another function, for that function a new window or scope will be opened where all the variables are local to that function. Once the execution is done, that scope will be removed from stack and the controls goes back to the caller of that function.
stack is mainly responsible for managing function calls and local variables.

Variables are just references to the objects, and objects are stored on the heap.
