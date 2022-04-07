import os
import random
import time
from data import *

def clear_screen():
    os.system("clear")

def wait_user():
    input("\nPresioná ENTER para continuar...")

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
        if quantity > 0: print(f"> {quantity} x", item_translate[item])

    wait_user()

def mine():

    clear_screen()

    if last_use["mine"] == None or time.time() - last_use["mine"] >= action_cooldown["mine"]:

        quantity = random.randint(50, 500)
        player.item["money"] += quantity

        print(f"\n{player.name} consiguió {quantity} pesos")

        quantity = random.randint(2,20)
        player.item["stone"] += quantity

        print(f"\n{player.name} consiguió {quantity} piedras")

        if(random.randint(0, 100) <= chance_values["iron"]):
            quantity = random.randint(1, 3)
            player.item["iron"] += quantity
            print(f"\n{player.name} consiguió {quantity} menas de hierro")

        last_use["mine"] = time.time()

    else:
        
        remaining = int(action_cooldown["mine"] - (time.time() - last_use["mine"]))

        if remaining > 59:
            remaining = remaining // 60
            print(f"\n¡No podés hacer esto ahora! Restan {remaining} minutos")

        else:
            print(f"\n¡No podés hacer esto ahora! Restan {remaining} segundos")

    wait_user()

def fish():

    clear_screen()

    if last_use["fish"] == None or time.time() - last_use["fish"] >= action_cooldown["fish"]:

        quantity = random.randint(1,5)
        player.item["salmon"] += 1

        print(f"\n{player.name} consiguió {quantity} salmón")

        if (random.randint(0, 100) <= chance_values["shrimp"]):
            quantity = random.randint(1,3)
            player.item["shrimp"] += 1
            print(f"\n{player.name} consiguió {quantity} camarón")

        aleatorio = random.randint(0,100)

        if (aleatorio <= chance_values["shrimp_shiny"]):
            player.item["shrimp_shiny"] += 1
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

        quantity = random.randint(50, 500)
        player.item["money"] += quantity

        print(f"\n{player.name} consiguió {quantity} pesos")

        last_use["crime"] = time.time()

    else:

        remaining = int(action_cooldown["crime"] - (time.time() - last_use["crime"]))

        if remaining > 59:
            remaining = remaining // 60
            print(f"\n¡No podés hacer esto ahora! Restan {remaining} minutos")

        else:
            print(f"\n¡No podés hacer esto ahora! Restan {remaining} segundos")

    wait_user()

