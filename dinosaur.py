class Dinosaur:
    def __init__(self, name, attack_power, health):
        self.name = name
        self.attack_power = 0
        self.health = 0
        

    def attack(self, robot):
        self.name = robot
        self.attack_power = 10
        self.health = 100
    