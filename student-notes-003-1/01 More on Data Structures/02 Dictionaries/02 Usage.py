
# Creating a dictionary
user = {
    "username": "xXTwoFiveXx", 
    "password": "123456",
    "last_login": "2026.04.01",
    "age": 98765,
    10 : 100, 
    "favorite_foods": [
        "tacos", "sushi", "pizza", "burrito"
    ]
}

user2 = dict()
user3 = {}

# Accessing Contents of Dictionary
passwd = user["password"]
print(passwd)

first = user.get("firstname", None) 
print(first)


# Changing and Adding Contents
user["password"] = "qwerty"  
user["firstname"] = "John"
print(user)
