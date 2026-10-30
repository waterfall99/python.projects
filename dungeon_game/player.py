class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.inventory = ["Rusty Sword", "Health Potion"]

    def is_alive(self):
        return self.hp > 0

    def use_potion(self):
        
        if "Health Potion" not in self.inventory:
            print("You check your inventory... No Health Potions Left!")
            return 
        
        if self.hp >= 100:
            print(f"\n{self.name} is already at full health (100 HP)!")
            return 
        
        self.inventory.remove("Health Potion")
        self.hp = min(100, self.hp + 30)
        print(f"\nYou drink a Health Potion and restore 30 HP! Current HP: {self.hp}/100")