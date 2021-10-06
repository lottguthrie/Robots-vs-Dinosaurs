from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = ""
        self.health = 100
        self.weapon = Weapon
        

    def attack(self, dinosaur):
        self.name = dinosaur
        self.attack_power = 100
        self.weapon = Weapon