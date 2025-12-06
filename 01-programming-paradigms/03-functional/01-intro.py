def mul(a:int) ->int:
    return a*a

print(mul(12))

numbers = [1,2,3,4,5,6]
squared = list(map(mul, numbers))
print(squared)