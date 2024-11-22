from enum import IntEnum

class CreatureTypes(IntEnum):
    TypeA = 0
    TypeB = 1
    TypeC = 2
    TypeD = 3

class Creature:
    def __init__(self, creatureType:CreatureTypes, hp:int, attack:int, speed:int):
        self.hp = hp
        self.atk = attack
        self.speed = speed
        self.type = creatureType
        self.powers = []
    def __str__(self):
        return f'Creature: {self.hp}, {self.atk}, {self.speed}, {self.type.name}. Powers: [{str(self.powers[0])}, {str(self.powers[1])}, {str(self.powers[2])}, {str(self.powers[3])}]'
    def add_power(self, power):
        self.powers.append(power)
    def get_max_damage_power(self):
        maxPowerValue = -1
        currentPowerValue = 0
        index = 0
        counter = 0
        for power in self.powers:
            currentPowerValue = power.power * self.atk
            if power.type == self.type:
                currentPowerValue *= 1.5
            
            if currentPowerValue > maxPowerValue:
                maxPowerValue = currentPowerValue
                index = counter
            counter += 1
        return self.powers[index]
    
