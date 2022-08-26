from robot import Robot
from dinosaur import Dinosaur

class Battlefield:

    def __init__(self):
        self.dinosaur = Dinosaur("Pierre", 18)
        self.robot = Robot("Francis")

    def run_game(self):
        pass

    def display_welcome(self):
        print(f'Welcome to the battle of Dinosaur {self.dinosaur.name} vs Robot {self.robot.name}')

    def battle_phase(self):
        pass

    def display_winner(self):
        pass