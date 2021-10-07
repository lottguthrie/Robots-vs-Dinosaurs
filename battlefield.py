from random import randint
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from robot import Robot


class Battlefield:
    def __init__(self, fleet, herd, dinosaur, robot, damage, die):
        self.fleet = Fleet()
        self.herd = Herd()
        self.dinosaur = Dinosaur[0]
        self.robot = Robot[0]
        self.damage  = damage[0]
        self.die = die()

    def run_game(self):
        pass
   
    def display_welcom(self):
        print(f"Welcome to the  Dinosaurs vs Robots Battlefield!Do You Have What it Takes to survive?")
        
    
    def battle(self):
        self.battle_begins = input("Are you ready for the ultimate game of survival? If so enter yes to begin the war for survival of the fittest!")
        if self.battle_begins == "yes":
            print("Let the battle begin")
            print(f"{self.dinosaur[0]} is your fighter")
            print(f"Your Teams health is {self.dinosaur.health[0]}") 
            while self.battle_begins == "yes":
                self.run_game()
            while(self.show_dino_oponent_options()and self.show_robo_oponent_options()):
                self.dinosaur.attack(self.robot)
                self.robot.health - 10
                self.robot.attack(self.dinosaur)
                self.dinosaur.health - 10
                if self.robot.health == 50:
                    print("Your oponent {robot[0]} is fading fast")
                elif self.robot.health == 50:
                    print("Your oponent {robot[0]} is fading fast")
                elif self.dinosaur.health == 0:
                    print("{dinosaur[0]} has died")
                elif self.robot.health == 0:
                    print("Your oponent {robot[0]} has died") 
                else:
                    print("The battle rages on!")    
        else:
            print("You are not ready!Please start over")
            def start_over(self):
                self.display_welcom()
       





    def dino_turn(self):
        self.dinosaur = input(f"Enter 1 for {Dinosaur.name[0]}, 2 for {Dinosaur.name[1]}, 3 for {Dinosaur.name[2]}, 4 for {Dinosaur.name[3]}")
        if self.dinosaur == "1":
            print(f"Your dinosaur is {Dinosaur.name[0]}")
        elif self.dinosaur == "2":
            print(f"Your dinosaur is {Dinosaur.name[1]}")
        elif self.dinosaur == "3":
            print(f"Your dinosaur is {Dinosaur.name[2]}")
        elif self.dinosaur == "4":
            print(f"Your dinosaur is {Dinosaur.name[3]}")  
        else:
            print("No Dinosaur selected! Please enter a number 1-4 to select your dinosaur for battle!")  


    def robo_turn(self):
        import random
        self.robot = []
        self.robot = input(int(random.randint(0,3)))
        if self.robot == 0:
            print(f"Your oponent is {Robot.name[0]}")            
        elif self.robot == 1:
            print(f"Your oponent is {Robot.name[1]}")
        elif self.robot == 2:
            print(f"Your oponent is {Robot.name[2]}")
        elif self.robot == 3:
            print(f"Your oponent is {Robot.name[3]}") 
        else:
            print("No apponent")

    def show_dino_oponent_options(self):
        dino_picks = Herd
        dino_oponents = 3
        for dinosaur in self.fleet:
            dino_picks +=  dinosaur.pick
            dino_oponents += 1
        print(f"These are your team {dino_picks[0]}")

        
    def show_robo_oponent_options(self):
        robot_picks = Fleet
        robot_oponents = 3
        for robot in self.herd:
            robot_picks +=  robot.pick
            robot_oponents += 1
        print(f"These are your oponents! {robot_picks[0]}  Good Luck!")

    def display_winners(self):
        pass



