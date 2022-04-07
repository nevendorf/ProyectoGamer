import time
from data import *
from actions import *

if __name__ == "__main__":

    clear_screen()    

    username = input("Inserte su nombre: ")

    player.name = username

    while True:
        
        call_to_action()

        if player.command == "mochila":

            backpack()

        elif player.command == "minar":

            mine()

        elif player.command == "pesca":

            fish()

        elif player.command == "crimen":

            crime()

        elif player.command == "salir":

            clear_screen()
            print("\n¡Gracias por jugar!")
            wait_user()
            break

        else:

            print(player.command)
            print("¡Comando inválido!")