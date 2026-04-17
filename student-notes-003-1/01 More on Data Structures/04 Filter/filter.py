
# Filter

# Filter takes an iterable (such as a list) 
names = [
    "Logan", "Jadon", "Jayden", 
    "Jared", "Thomas", "Thomas"
]

# Filter also takes in a function that returns True/False
def starts_with_j(name: str) -> bool:
    if name[0] == "J":
        return True
    else:
        return False

# Filter applies the function to each item in the iterable
# For each item, if the result is True, 
# then that item ends up in the resulting list.
j_names = list(filter(starts_with_j, names))
print(j_names)


# with a lambda function
j_names = filter(
    lambda name: name[0] == "J", 
    names
)
print(list(j_names))

# The equivalent for loop
j_names = []
for name in names:
    if starts_with_j(name):
        j_names.append(name)


