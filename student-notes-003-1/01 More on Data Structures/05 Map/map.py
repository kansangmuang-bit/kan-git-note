
fave_games = [
    "Factorio", 
    "Satisfactory", 
    "Fortnite", 
    "Half-life",
    "Rim World",
    "Portal",
    "Minecraft",
    "kjshkfjg",
]

def uppercase_it(game: str):
    return game.upper()

uppercase_games = map(uppercase_it, fave_games)
print(list(uppercase_games))
