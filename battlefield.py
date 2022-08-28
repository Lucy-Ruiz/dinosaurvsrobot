from robot import Robot
from dinosaur import Dinosaur

class Battlefield:

    def __init__(self):
        self.dinosaur = Dinosaur("Pierre", 20)
        self.robot = Robot("Francis")

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print(f'Welcome to the battle of Dinosaur {self.dinosaur.name} vs Robot {self.robot.name}')

    def battle_phase(self):
        while self.dinosaur.health > 0 and self.robot.health > 0:
            self.dinosaur.attack(self.robot)
            print(f'''Dinosaur attacked Robot
            Robot health: {self.robot.health}
            Dinosaur health: {self.dinosaur.health}''')
            if self.robot.health > 0:
                self.robot.attack(self.dinosaur)
                print(f'''Robot attacked Dinosaur
                Dinosaur health: {self.dinosaur.health}
                Robot health: {self.robot.health}''')

    def display_winner(self):
        if self.robot.health > 0:
            print('Robot wins')
        else:
            print('Dinosaur wins')