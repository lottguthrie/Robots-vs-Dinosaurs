from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robot_name = ['R2-D2', 'C-3PO', 'BB-8', 'Luke Skywalker']
        self.create_fleet.append(input("Pick your team"))

    def create_fleet(self):
        robot_one = Robot()
        robot_one.__setattr__(f"{self.robot_name[0]} R2-D2", 10, Weapon)
        robot_two = Robot()
        robot_one.__setattr__(f"{self.robot_name[1]} C-3PO", 10, Weapon)
        robot_three = Robot()
        robot_three. __setattr__(f"{self.robot_name[2]} BB-8", 10, Weapon)
        robot_four = Robot()
        robot_four.__setattr__(f"{self.robot_name[3]} Luke Skywalker", 10, Weapon)
