## Builder Pattern

A way to construct complex objects step-by-step, instead of cramming everything into a giant constructor.

Analogy: Ordering a custom pizza

- You don't say: "Pizza(size=large, crust=thin, cheese=mozzarella, toppings=[pepperoni, mushrooms, olives], sauce=tomato, extra_cheese=True, gluten_free=False)"
- Instead: "Large pizza → thin crust → add pepperoni → add mushrooms → extra cheese"

## WHAT, WHY, HOW - Summary

#### WHAT IS IT?

Separates construction from representation. Build complex objects step-by-step.

### WHY DO WE NEED IT?

#### Problem:

```py
# Too many parameters
course = Course(title, desc, id, 49.99, "USD", 6, "Beginner",
True, True, True, False, True, "English", ...)
```

#### Solution:

```py
# Clear and readable
course = Course(CourseBuilder().set_title("Python").set_duration("2 months").set_level("Beginner"))
print(course)
```

## HOW DOES IT WORK?

- Builder class - Has methods to set properties
- Method chaining - Each method returns self
- Build method - Returns final object
- Optional: Director - Pre-configured templates

Real Coursera Clone Uses
FeatureBuilder UsageCourse CreationCourseBuilder() with 15+ optional fieldsSearch QueriesSearchBuilder().filter().sort().paginate()Email TemplatesEmailBuilder().to().subject().body()API ResponsesResponseBuilder().data().status().headers()Test DataEasy to create test courses with specific features

## What is self?

self = The current object/instance

## Why return self enables chaining:

```py
builder = CourseBuilder()
builder.set_title("Python")  # Returns builder
       .set_price(49.99)     # Called on returned builder
       .build()               # Called on returned builder

# Same as:
temp1 = builder.set_title("Python")  # temp1 = builder
temp2 = temp1.set_price(49.99)       # temp2 = builder
course = temp2.build()                # course = Course object
```

return self = give back the same object so you can call another method
