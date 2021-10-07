from random import randint
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from robot import Robot


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        
    
    def run_game(self):
        pass
   
    def display_welcom(self):
        print(f"Welcome to the  Dinosaurs vs Robots Battlefield!Do You Have What it Takes to survive?")
        
    
    def battle(self):
        self.dino

    def dino_turn(self, dinosaur):
        self.dino_picks[0]

    def robo_turn(self, robot):
        pass

    def show_dino_oponent_options(self):
        import random
        self.dino_picks = Dinosaur[0]
        for i in range(3):
            input = int(input(random.randint(0,3)))
            self.dino_picks.append(self.dino_picks)
        print(f"{self.dino_picks[0]} This is your team")

        
    def show_robo_oponent_options(self):
        import random
        self.robot_picks = Robot[0]
        for i in range(3):
            input = int(input(random.randint(0,3)))
            self.robot_picks.append(self.robot_picks)
        
        print(f"{self.robot_picks[0]} This is your oponent! Good Luck!")

    def display_winners(self):
        pass



