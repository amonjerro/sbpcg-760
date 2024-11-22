from enum import Enum

class CreatureTypes(Enum):
    TypeA = 0
    TypeB = 1
    TypeC = 2
    TypeD = 3

class Power:
    def __init__(self, power, type):
        self.name = ""
        self.power = power
        self.type = type

class Creature:
    def __init__(self, creatureType):
        self.hp = 0
        self.atk = 0
        self.speed = 0
        self.type = creatureType
        self.powers = []
    def GetMaxDamagePower(self):
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

class Evaluator:
    firstStrikePayoff = 20
    oneHitKOPayoff = 50
    def __init__(self, otherCreature):
        self.playerCreature = otherCreature
    
    def TypeIsWeak(self, this, other):
        if (this.type == CreatureTypes.TypeA):
            return other.type == CreatureTypes.TypeD
        elif (this.type == CreatureTypes.TypeB):
            return other.type == CreatureTypes.TypeA
        elif (this.type == CreatureTypes.C):
            return other.type == CreatureTypes.TypeA or other.type == CreatureTypes.B
        else:
            return other.type == CreatureTypes.C

    def EvaluateType(self, creature):
        if self.TypeIsWeak(creature, self.playerCreature):
            return 0.5
        
        if (self.TypeIsWeak(self.playerCreature, creature)):
            return 2
        
        return 1

    def FirstStrikeBonus(self, creature):
        totalSpeed = self.playerCreature.speed + creature.speed
        return self.firstStrikePayoff * (creature.speed / totalSpeed)
    
    def OHKOBonus(self, creature):
        power = creature.GetMaxDamagePower()
        powVal = power.power
        if self.TypeIsWeak(self.playerCreature, creature):
            powVal *= 2

        if powVal > self.playerCreature.hp:
            return self.oneHitKOPayoff
        else:
            return 0