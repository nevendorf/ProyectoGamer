from global_import import *
from data import *

def clear_screen():
    os.system("cls")

def wait_user():
    input("\nPresioná ENTER para continuar...")

def save_changes(item_name, new_value):

    with open('player_data.json', 'r') as data_file:
        player_data = json.load(data_file)
        player_data["items"][item_name] = new_value

    with open('player_data.json', 'w') as data_file:
        json.dump(player_data, data_file, indent=4)

def return_value(item_name):

    with open('player_data.json', 'r') as data_file:
        player_data = json.load(data_file)

    current_value = player_data["items"][item_name]

    return int(current_value)
