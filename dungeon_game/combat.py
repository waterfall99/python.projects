import random
import time

def enter_combat(player):
    monster_hp = 30
    print("\nA wild Goblin blocks your path!")
    time.sleep(0.5)

    while monster_hp > 0 and player.is_alive():
        print(f"\n[⚔️ COMBAT] {player.name}: {player.hp}/100 HP | Goblin: [monster.hp] HP")
        print("What will you do?")
        print("1. Attack with Rusty Sword")
        print("2. Flee back to safety")

        action = input("> ").strip()

        if action not in ["1", "2"]:
            print("\033[A\033[K", end="")
            continue

        if action == "1":
            damage = random.randint(5, 10)
            monster_hp -= damage
            print(f"\nYou swing your Rusty Sword and deal {damage} damage to the Goblin!")
            time.sleep(0.8)

            if monster_hp > 0:
                enemy_damage = random.randint(3, 7)
                player.hp -= enemy_damage
                print(f"\nThe Goblin scratches you back for {enemy_damage} damage!")
                time.sleep(0.8)
        
        elif action == "2":
            print("\nYou try to sprint away...")
            time.sleep(1)
            if random.choice([True, False]):
                print("\n💨 You successfully escaped back down the hallway!")
                break
            
            else:
                print("\n❌ You tripped! The Goblin blocks your escape!")
                enemy_damage = random.randint(3, 7)
                player.hp -= enemy_damage
                print(f"\nThe Goblin strikes you while you're down for {enemy_damage} damage!")
                time.sleep(0.8)
    
    if not player.is_alive():
        print("\n💀 You were defeated in battle. Game Over!")
    
    elif monster_hp <= 0:
        print("\n🎉 You defeated the Goblin!")
        player.inventory.append("Gold Coin")
        print("\n💰 You looted 1 Gold Coin from its remains.")
        time.sleep(0.5)


        

