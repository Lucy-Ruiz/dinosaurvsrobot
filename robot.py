from weapon import Weapon
class Robot:
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Wrist rocket", 15)


    def attack(self, dinosaur):
    