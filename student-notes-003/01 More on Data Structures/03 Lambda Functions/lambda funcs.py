
# A lambda function is just an anonymous function (no name)

# Typical Way We Create Functions
def add(x, y):
    return x + y

# Same function as a lambda function
lambda x, y: x + y

# Same function as a lambda function with an identifier
addstuff = lambda x, y: x + y
print(addstuff(1, 2))

