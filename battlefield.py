from robot import Robot
from dinosaur import Dinosaur

class Battlefield:

    def __init__(self):
        self.dinosaur = Dinosaur("Pierre", 100)
        self.robot = Robot("Francis", 100)