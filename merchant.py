import time

def enter_merchant(player):
    print("\nA Wandering Merchant emerges from the shadows with a heavy rucksack. ⚖️")
    time.sleep(0.5)
    print("\nMerchant: 'Greetings, traveller! I swap fresh Health Potions for shiny Gold Coins.'")

    coin_count = player.inventory.count("Gold Coin")

    print("\n[⚖️ TRADE] 2 Gold Coins for 1 Health Potion")
    print(f"\nYour Wallet: {coin_count} x Gold Coin")
    print("What will you do?")
    print("1. Buy Health Potion")
    print("2. Leave Merchant")

    while True:
        action = input("> ").strip()

        if action not in ["1", "2"]:
            print("\033[A\033[K", end="")
            continue

        if action == "1":
            
            if coin_count >= 2:
                for _ in range(2):
                    player.inventory.remove("Gold Coin")
                player.inventory.append("Health Potion")
                print("\n✨ Transaction Complete! A fresh Health Potion has been added to your inventory.")
            
            else:
                print("\nCome back when you have 2 Gold Coins, traveller!")
                time.sleep(1)
                break
        
        elif action == "2":
            print("\nMerchant: 'Watch your back out there.'")
            time.sleep(0.5)
            break
