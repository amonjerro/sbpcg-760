from enum import IntEnum
import random

class CreatureTypes(IntEnum):
    TypeA = 0
    TypeB = 1
    TypeC = 2
    TypeD = 3

class CreatureGenotype:
    def __init__(self, totalBudget):
        self.statsBudget = random.randint(0, totalBudget)
        self.powerBudget = totalBudget - self.statsBudget

        self.hpGeneValue = random.randint(0, self.statsBudget)
        self.attackGeneValue = random.randint(0, self.statsBudget - self.hpGeneValue)
        self.speedGeneValue = random.randint(0, self.statsBudget - (self.hpGeneValue + self.attackGeneValue))
        assert self.hpGeneValue + self.attackGeneValue + self.speedGeneValue <= self.statsBudget

        self.power1Budget = random.randint(0, self.powerBudget)
        self.power2Budget = random.randint(0, self.powerBudget - self.power1Budget)
        self.power3Budget = random.randint(0, self.powerBudget - (self.power1Budget + self.power2Budget))
        self.power4Budget = random.randint(0, self.powerBudget - (self.power1Budget + self.power2Budget + self.power3Budget))
        assert self.power1Budget + self.power2Budget + self.power3Budget + self.power4Budget <= self.powerBudget

    def rerollPowerBudget(self,newPowerBudget:int):
        self.powerBudget = newPowerBudget
        self.power1Budget = random.randint(0, self.powerBudget)
        self.power2Budget = random.randint(0, self.powerBudget - self.power1Budget)
        self.power3Budget = random.randint(0, self.powerBudget - (self.power1Budget + self.power2Budget))
        self.power4Budget = random.randint(0, self.powerBudget - (self.power1Budget + self.power2Budget + self.power3Budget))

    def rerollStatBudget(self,statBudget:int):
        self.statsBudget = statBudget
        self.hpGeneValue = random.randint(0, self.statsBudget)
        self.attackGeneValue = random.randint(0, self.statsBudget - self.hpGeneValue)
        self.speedGeneValue = random.randint(0, self.statsBudget - (self.hpGeneValue + self.attackGeneValue))

class Creature:
    def __init__(self, genotype:CreatureGenotype, creatureType:CreatureTypes, hp:int, attack:int, speed:int):
        self.genotype = genotype
        self.hp = hp
        self.atk = attack
        self.speed = speed
        self.type = creatureType
        self.powers = []
        self.fitness = 0
    def __str__(self):
        return f'Creature: {self.hp}, {self.atk}, {self.speed}, {self.type.name}. Powers: [{str(self.powers[0])}, {str(self.powers[1])}, {str(self.powers[2])}, {str(self.powers[3])}]'
    def add_power(self, power):
        self.powers.append(power)
        return power.effect
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
    
