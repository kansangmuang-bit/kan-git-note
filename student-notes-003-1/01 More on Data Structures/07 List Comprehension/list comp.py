
# Format
# [ item_in_list     for loop(s)   conditional(s)]
result = [i for i in range(10)]
print(result)

result = [i**2 for i in range(10)]
print(result)

result = [i for i in range(0,10,2)]
print(result)

result = [i for i in range(10) if i % 2 == 0]
print(result)

names = [
    "Logan", "James", "Jared", 
    "Thomas", "Soren", "Reese", 
    "Wani", "Kobe", "Jayden"
]

# Using the names list and list comprehension, create a list that contains only the names that have an even number of characters.
result = [name for name in names if len(name) % 2 == 0]
print(result)

result = [len(name) / 2 for name in names if len(name) % 2 == 0]
print(result)


result = [ (x, y) for x in range(5) for y in range(3)]
print(result)

result = [ (x, y) for x in range(5) for y in range(3) if x%2 == 1 ]
print(result)