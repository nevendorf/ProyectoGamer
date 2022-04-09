from global_import import *
from data import *

def start_game():

    clear_screen()

    player.load_data()

    if player.name == "": 

        username = input("Inserte su nombre: ")

        with open('player_data.json', 'r') as data_file:
            player_data = json.load(data_file)

        player_data["name"] = username

        with open('player_data.json', 'w') as data_file:
            json.dump(player_data, data_file, indent = 4)

def log_screen():

    print("Partida de {player.name}\n")

    with open("console.log", 'r') as log_file:
        log_messages = log_file.read()

    if file_content == "NODATA":
        print("|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n\n")

    else:
        
        log_mesagges = log_file.readlines()

        for iterator in 10 - len(log_messages):
            print("|\n")

        for message in log_messages:
            print(f"| {message}")

    player.command = input("\n>")
    player.command = player.command.lowe()
