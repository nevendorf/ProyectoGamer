from global_import import *
from data import *
from utils import *

def start_game():

    clear_screen()

    try:

        input("Presioná ENTER para jugar o CTRL+C para salir\n\n")

    except KeyboardInterrupt:

        clear_screen()
        quit()

    clear_screen()

    player.load_data()

    if player.name == "": 

        username = input("Inserte su nombre: ")

        with open('player_data.json', 'r') as data_file:
            player_data = json.load(data_file)

        player.name = username
        player_data["name"] = username

        with open('player_data.json', 'w') as data_file:
            json.dump(player_data, data_file, indent = 4)

def log_screen():

    clear_screen()

    print(f"* Partida de {player.name} *\n")

    with open("console.log", 'r') as log_file:
        log_messages = log_file.readlines()

    if 10 - len(log_messages) > 0:

        for iterator in range(0, 10 - len(log_messages)):
            print("|")

    for message in log_messages:
            print(f"| {message}", end="")

    player.command = input("\n\n> ")
    player.command = player.command.lower()


def save_message(message_to_save):
    
    with open('console.log', 'r') as log_file:

        log_messages = log_file.readlines()
        
        if len(log_messages) > 9:
            log_file.seek(0)
            log_messages = log_file.readlines()[1:]
        
    with open('console.log', 'w') as log_file:

        for message in log_messages:

            message = message.strip() # Deletes empty lines (idk why the code makes empty lines, tbh)
            log_file.write(str(message) + "\n")

        log_file.write(str(message_to_save))

