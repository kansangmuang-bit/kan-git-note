# Sets in python are like math sets
# Elements are unique
# Elements have no order

a_set = {1, 1, 1, 1, 2, 3, 100, -100, -200, 78, 6}
print(a_set)

# A common use is removing duplicates
data = [1, 2, 3, 2, 2, 2 ,2, 2, 2]
data = set(data)
data = list(data)
print(data)

# Set operations

a = {1, 2, 3}
b = {3, 4, 5, 6}

# Union (includes everything in each set)
c = a | b # pipe | was previously used for bitwise or
print(c)

# Intersection
d = a & b # & is usually for AND, and previously used for bitwise and
print(d)

# Difference
e = a - b   # for each item in b, remove it from a
print(e)
