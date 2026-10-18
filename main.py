import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.inventory = ["Rusty Sword", "Health Potion"]

    def is_alive(self):
        return self.hp > 0

def introduction():
    print("\n--- Welcome to the Python Dungeon ---")
    time.sleep(1)
    print("You wake up in a cold, dark room. The air is damp.")
    time.sleep(1)

def main():
    introduction()
    player_name = input("What is your character's name?")
    player = Player(player_name)

    print(f"\nGood luck, {player.name}...")

    while player.is_alive():
        action = input("Do you want to (1) Explore, (2) Check Inventory, or (3) Quit? ")

        if action == "1":
            event = random.choice(["monster", "chest", "empty"])
            if event == "monster":
                damage = random.randint(15, 30)
                player.hp -= damage
                print(f"\nA wild Goblin attacks! You fight it off but lose {damage} HP.")
                time.sleep(1)
                print(f"Your current HP: {player.hp}")
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
        elif action == "3":
                print("Thanks for playing!")
                break
    if not player.is_alive():
        print("\nYou have fallen in battle. Game Over!")
if __name__ == "__main__":
    main()