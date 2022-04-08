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

def get_data():

    player.item["money"] = return_value("money")
    player.item["stone"] = return_value("stone")
    player.item["iron"] = return_value("iron")
    player.item["salmon"] = return_value("salmon")
    player.item["shrimp"] = return_value("shrimp")
    player.item["shrimp_shiny"] = return_value("shrimp_shiny")

def call_to_action():

    clear_screen()

    print("Inserte acción:\n")

    print(" Minar")
    print(" Crimen")
    print(" Mochila")
    print(" Pesca")
    print(" Salir")

    player.command = input("\n> ")
    player.command = player.command.lower()

def backpack():

    clear_screen()

    print(f"\nMochila de {player.name}:\n")

    for item, quantity in player.item.items():
        if quantity > 0: print(f"> {item_translate[item]}: {quantity}")

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

        if(random.randint(0, 100) <= chance_values["iron_ore"]):

            player.item["iron_ore"] = return_value("iron_ore")

            quantity = random.randint(1, 3)
            player.item["iron_ore"] += quantity

            save_changes("iron_ore", player.item["iron_ore"])

            print(f"\n{player.name} consiguió {quantity} menas de hierro")

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
