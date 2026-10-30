import random
import time
import combat
import merchant
from player import Player

def introduction():
    print("\n--- Welcome to the Python Dungeon ---")
    time.sleep(1)
    print("You wake up in a cold, dark room. The air is damp.")
    time.sleep(1)

def main():
    introduction()
    player_name = input("What is your character's name? ")
    player = Player(player_name)

    print(f"\nGood luck, {player.name}...")

    while player.is_alive():
        action = input("Do you want to (1) Explore, (2) Check Inventory, or (3) Quit? ")

        if action not in ["1", "2", "3"]:
            print("\033[A\033[K", end="")
            continue
        
        if action == "1":
            event = random.choice(["monster", "merchant", "chest", "empty"])
            
            if event == "monster":
                combat.enter_combat(player)

            elif event == "merchant":
                merchant.enter_merchant(player)
           
            elif event == "chest":
                player.inventory.append("Gold Coin")
                print("\nYou found a chest! Added a Gold Coin to your inventory.\n")
            
            else:
                print("\nYou walk down a long hallway. Nothing happens.\n")
        
        elif action == "2":
                print(f"\n--- Inventory ---")
                for item in player.inventory:
                    print(f"- {item}")
                print(f"HP: {player.hp}")
                if "Health Potion" in player.inventory:
                    use_item = input("Do you want to use a Health Potion? (y/n): ").strip().lower()
                    if use_item == "y":
                        player.use_potion()
        
        elif action == "3":
                print("Thanks for playing!")
                break
    
    if not player.is_alive():
        print("\nYou have fallen in battle. Game Over!")

if __name__ == "__main__":
    main()