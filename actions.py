from global_import import *
from data import *
from utils import *

def reset_stats():

    user_input = None

    while user_input == None or (user_input != "aceptar" and user_input != "cancelar"):

        clear_screen()

        print("\nTodo tu progreso está a punto de ser eliminado.")
        print("\n- Aceptar\n- Cancelar")
        user_input = input("\n> ").lower()

    if user_input == "aceptar":

        with open('player_data.json', 'r') as data_file:
            player_stats = json.load(data_file)

        for stat in player_stats["items"]:
            player_stats["items"][stat] = 0

        with open('player_data.json', 'w') as data_file:
            json.dump(player_stats, data_file, indent=4)

        clear_screen()

        print("\n¡Tu progreso fue eliminado!")
        input()

def start_game():

    clear_screen()

    username = input("Inserte su nombre: ")
    player.name = username

    player.load_data()

def call_to_action():

    clear_screen()

    print("Inserte acción:\n")

    print("- Minar")
    print("- Crimen")
    print("- Mochila")
    print("- Pescar")
    print("- Reset")
    print("- Salir")

    player.command = input("\n> ")
    player.command = player.command.lower()

def backpack():

    is_empty = True

    player.load_data()

    clear_screen()

    print(f"\nMochila de {player.name}:\n")

    for item, quantity in player.item.items():
        if quantity > 0:
            print(f"> {item_translate[item]}: {quantity}")
            is_empty = False

    if is_empty: print(f"¡La mochila de {player.name} está vacía!")

    wait_user()

def mine():

    clear_screen()

    if last_use["mine"] == None or time.time() - last_use["mine"] >= action_cooldown["mine"]:

        player.item["money"] = return_value("money")

        quantity = random.randint(50, 500)
        player.item["money"] += quantity

        save_changes("money", player.item["money"])

        print(f"\n{player.name} consiguió {quantity} pesos")

        player.item["stone"] = return_value("stone")

        quantity = random.randint(2,20)
        player.item["stone"] += quantity

        save_changes("stone", player.item["stone"])

        print(f"\n{player.name} consiguió {quantity} piedras")

        random_ore = random.randint(1,3)

        if (random_ore == 1):

            if random.randint(0, 100) <= chance_values["iron_ore"]:

                player.item["iron_ore"] = return_value("iron_ore")

                quantity = random.randint(1, 3)
                player.item["iron_ore"] += quantity

                save_changes("iron_ore", player.item["iron_ore"])

                print(f"\n{player.name} consiguió {quantity} menas de hierro")

        elif random_ore == 2:

            if random.randint(0, 100) <= chance_values["coal_ore"]:

                player.item["coal_ore"] = return_value("coal_ore")

                quantity = random.randint(10, 20)
                player.item["coal_ore"] += quantity

                save_changes("coal_ore", player.item["coal_ore"])

                print(f"\n{player.name} consiguió {quantity} menas de carbón")

        elif random_ore == 3:

            if random.randint(0, 100) <= chance_values["copper_ore"]:

                player.item["copper_ore"] = return_value("copper_ore")

                quantity = random.randint(4, 7)
                player.item["copper_ore"] += quantity

                save_changes("copper_ore", player.item["copper_ore"])

                print(f"\n{player.name} consiguió {quantity} menas de cobre")

        last_use["mine"] = time.time()

    else:

        remaining = int(action_cooldown["mine"] - (time.time() - last_use["mine"]))

        if remaining > 59:
            remaining = remaining // 60
            print(f"\n¡No podés hacer esto ahora! Faltan {remaining} minutos")

        else:
            print(f"\n¡No podés hacer esto ahora! Faltan {remaining} segundos")

    wait_user()

def fish():

    clear_screen()

    if last_use["fish"] == None or time.time() - last_use["fish"] >= action_cooldown["fish"]:

        player.item["salmon"] = return_value("salmon")

        quantity = random.randint(1,5)
        player.item["salmon"] += 1

        save_changes("salmon", player.item["salmon"])

        print(f"\n{player.name} consiguió {quantity} salmón")

        if (random.randint(0, 100) <= chance_values["shrimp"]):

            player.item["shrimp"] = return_value("shrimp")

            quantity = random.randint(1,3)
            player.item["shrimp"] += 1

            save_changes("shrimp", player.item["shrimp"])

            print(f"\n{player.name} consiguió {quantity} camarón")

        aleatorio = random.randint(0,100)

        if (aleatorio <= chance_values["shrimp_shiny"]):

            player.item["shrimp_shiny"] = return_value("shrimp_shiny")

            player.item["shrimp_shiny"] += 1

            save_changes("shrimp_shiny", player.item["shrimp_shiny"])

            print(f"\n{player.name} consiguió un camarón shiny")

        last_use["fish"] = time.time()

    else:

        remaining = int(action_cooldown["fish"] - (time.time() - last_use["fish"]))

        if remaining > 59:
            remaining = remaining // 60
            print(f"\n¡No podés hacer esto ahora! Restan {remaining} minutos")

        else:
            print(f"\n¡No podés hacer esto ahora! Restan {remaining} segundos")

    wait_user()

def crime():

    clear_screen()

    if last_use["crime"] == None or time.time() - last_use["crime"] >= action_cooldown["crime"]:

        player.item["money"] = return_value("money")

        quantity = random.randint(-300, 500)
        player.item["money"] += quantity

        if quantity > 0:
            print(f"\n{player.name} consiguió {quantity} pesos")

        elif quantity < 0:
            print(f"\nPerdiste {quantity+quantity*2} pesos")

        else:
            print("\nParece que no hubo suerte")

        if player.item["money"] < 0:
            player.item["money"] = 0

        save_changes("money", player.item["money"])

        last_use["crime"] = time.time()

    else:

        remaining = int(action_cooldown["crime"] - (time.time() - last_use["crime"]))

        if remaining > 59:
            remaining = remaining // 60
            print(f"\n¡No podés hacer esto ahora! Restan {remaining} minutos")

        else:
            print(f"\n¡No podés hacer esto ahora! Restan {remaining} segundos")

    wait_user()
