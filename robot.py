from weapon import Weapon
class Robot:
    
    def __init__(self, name,health, active_weapon):
        self.name = name
        self.health = health
        self.active_weapon = Weapon("Sword", 25)


    def active_weapon(self):
    