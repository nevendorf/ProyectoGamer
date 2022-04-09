from global_import import *
from data import *
from actions import *
from interface import *

if __name__ == "__main__":

    start_game()

    while True:

        log_screen()

        if player.command == "mochila":

            backpack()

        elif player.command == "minar":

            mine()

        elif player.command == "pescar":

            fish()

        elif player.command == "crimen":

            crime()

        elif player.command == "reset":

            reset_stats()

        elif player.command == "salir":

            clear_screen()
            print("\n¡Gracias por jugar!")
            wait_user()
            break

        else:

            clear_screen()
            print("¡Comando inválido!")
            wait_user()
