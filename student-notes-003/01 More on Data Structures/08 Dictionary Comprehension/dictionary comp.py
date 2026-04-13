

squares = { x: x**2  for x in range(10) }
print(squares)

# Using dictionary comprehension, create a dictionary containing the even numbers 50 through 100 (inclusive on both ends) as keys and their corresponding cube as values.
even_squares = { x: x**3 for x in range(50,101) if x%2 == 1 }
print(even_squares)

# Using dictionary comprehension and the given associative lists (parallel lists), create a dictionary where the names are the keys and their favorite food is the value for each key.

names = ["Loki", "Gabe", "Connor", "Jadon", "Aidan", "JB", "Thomas"] 

favorite_food = ["Sushi", "Spaghetti", "Oyster", "Steak", "Fried Rice", "Chicken", "Ramen"]

result = { names[i]: favorite_food[i] for i in range(len(names))}
print(result)

result = { name: food for name, food in zip(names, favorite_food)}
print(result)
