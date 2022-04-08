class Player:

    command = None

    item = {
        "money": 0,
        "stone": 0,
        "iron_ore": 0,
        "coal_ore": 0,
        "copper_ore": 0,
        "salmon": 0,
        "shrimp": 0,
        "shrimp_shiny": 0
    }

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Player data:\nName: {name}"

player = Player(None)

chance_values = {
    "shrimp": 40,
    "shrimp_shiny": 1,
    "coal_ore": 50,
    "copper_ore": 25,
    "iron_ore": 15
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

item_translate = {
    "money": "Dinero",
    "stone": "Piedra",
    "iron_ore": "Mena de Hierro",
    "copper_ore": "Mena de Cobre",
    "coal_ore": "Mena de Carbón",
    "salmon": "Salmón",
    "shrimp": "Camarón",
    "shrimp_shiny": "Camarón Shiny"
}
