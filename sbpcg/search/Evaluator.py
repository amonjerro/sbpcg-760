from typing import List, Union, Tuple
from abc import ABC, abstractmethod
from sbpcg import CreatureTypes

class Fitness(ABC):
    @abstractmethod
    def evaluate(self, creatureType:CreatureTypes, candidate):
        pass

    def is_type_weak(self, this, other):
        if (this == int(CreatureTypes.TypeA)):
            return other == int(CreatureTypes.TypeD)
        elif (this == int(CreatureTypes.TypeB)):
            return other == int(CreatureTypes.TypeA)
        elif (this == int(CreatureTypes.TypeC)):
            return other == int(CreatureTypes.TypeA) or int(other == CreatureTypes.TypeB)
        else:
            return other == int(CreatureTypes.TypeC)
    
    def STAB_bonus(self, monType, powerType):
        if monType == powerType:
            return 1.5
        return 1
    def evaluate_type(self, opp, ply):
        if self.is_type_weak(ply, opp):
            return 0.5
        
        if (self.is_type_weak(opp, ply)):
            return 2
        
        return 1

class VectorEvaluator(Fitness):
    def __init__(self, opponent, verbose=False):
        self.opponent = opponent
        self.powerTupleIndex = 4
        self.monPowerIndex = 2
        self.hpIndex = 1
        self.monSpeedIndex = 3
        self.verbose = verbose
        self.winBonus = 10

    def evaluate(self, candidate:List[Union[int, Tuple[int,...]]]):
        if self.verbose:
            print("====Debugging Math=====")
            print(self.opponent)
            print(candidate)

        # Base fitness of two
        fitness = 2
        debugOutput = ''
        candidateType = candidate[0]
        opp = self.opponent
        candidatePowerDamageValues = list(
            map(lambda x: x[0] * self.evaluate_type(int(opp[0]), x[1]) * self.STAB_bonus(candidateType, x[1]) * candidate[self.monPowerIndex], 
            candidate[self.powerTupleIndex:]))
        mostDamagingPower = max(candidatePowerDamageValues)
        opponentPowerDamageValues = list(
            map(lambda x: x[0] * self.evaluate_type(int(candidateType), x[1]) * self.STAB_bonus(opp[0], x[1]) * opp[self.monPowerIndex], 
            opp[self.powerTupleIndex:]))
        mostDangerousPower = max(opponentPowerDamageValues)
        turnsToWin = 1 + opp[self.hpIndex] // mostDamagingPower
        turnsToLose = 1 + candidate[self.hpIndex] // mostDangerousPower
        
        if self.verbose:
            print(f'Most dangerous power: {mostDangerousPower}, Most damaging power: {mostDamagingPower}')
            print(f'Turns to Lose: {turnsToLose}, Turns to Win: {turnsToWin}')
        
        # Do I win?
        if turnsToWin < turnsToLose:
            # yes
            fitness += self.winBonus
        elif turnsToWin == turnsToLose:
            # Depends on who goes first
            if candidate[self.monSpeedIndex] > opp[self.monSpeedIndex]:
                fitness += self.winBonus
            elif candidate[self.monSpeedIndex] == opp[self.monSpeedIndex]:
                # Speed ties are resolved randomly, so in theory you win half the time
                fitness += self.winBonus * 0.5

        # How close is the match?
        if turnsToLose < turnsToWin:
            damageDealt = turnsToLose * mostDamagingPower
            if candidate[self.monSpeedIndex] > opp[self.monSpeedIndex]:
                damageDealt += mostDamagingPower
            elif candidate[self.monSpeedIndex] < opp[self.monSpeedIndex]:
                damageDealt -= mostDamagingPower
            if self.verbose:
                print(f'Damage dealt: {damageDealt}')
            fitness *= damageDealt / opp[self.hpIndex]
        elif turnsToWin <= turnsToLose:
            damageReceived = turnsToWin * mostDangerousPower
            if candidate[self.monSpeedIndex] < opp[self.monSpeedIndex]:
                damageReceived += mostDangerousPower
            elif candidate[self.monSpeedIndex] > opp[self.monSpeedIndex]:
                damageReceived -= mostDangerousPower
            if damageReceived<0:
                damageReceived = 0
            if self.verbose:
                print(f"Damage received: {damageReceived}")
            fitness *= 1-(damageReceived / candidate[self.hpIndex])

        
        return fitness
