from global_import import *

class Player():

    def __init__(self):

        self.name = None

        self.command = None

        self.item = {
            "money": 0,
            "stone": 0,
            "iron_ore": 0,
            "coal_ore": 0,
            "copper_ore": 0,
            "salmon": 0,
            "shrimp": 0,
            "shrimp_shiny": 0
        }

    def __str__(self):
        return f"Player data:\nName: {name}"

    def load_data(self):

        with open('player_data.json', 'r') as data_file:
            player_stats = json.load(data_file)

        for stat, value in player_stats["items"].items():
            self.item[stat] = player_stats["items"][stat]

player = Player()

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
