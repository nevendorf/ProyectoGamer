class Player:

    command = None

    money = 0
    stone = 0
    iron = 0
    salmon = 0
    shrimp = 0
    shrimp_shiny = 0
    
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Player data:\nName: {name}"

player = Player(None)

chance_values = {
    "shrimp": 40,
    "shrimp_shiny": 1,
    "iron": 1
}

last_use = {
    "mine": None,
    "fish": None,
    "crime": None
}

action_cooldown = {
    "mine": 300,
    "fish": 240,
    "crime": 120
}