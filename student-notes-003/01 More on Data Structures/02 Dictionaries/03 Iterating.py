

restaurant = {
    "name":     "China Flag",
    "cuisine":  "chinese buffet",
    "address":  "123 China Flag St.",
    "rating":   4.75,
    "phone":    "318-123-4567",
}

# interating over keys
for key in restaurant:
    print(key)
    print(restaurant[key]) # gets the value
    
# also keys
for key in restaurant.keys():
    print(key)
    
# for the values
for val in restaurant.values():
    print(val)
    
# both keys and values
for key, val in restaurant.items():
     print(key, val)
    

keys = restaurant.keys()
print(keys)


