from abc import ABC, abstractmethod
import random
from sbpcg import Creature, CreatureGenotype

class MutationStrategy(ABC):
    @abstractmethod
    def mutate(self,creature:Creature):
        pass

class BudgetMutationStrategy(MutationStrategy):
    def __init__(self, mutationRate:float, mutationFactor:int):
        self.mutationRate = mutationRate
        self.mutationFactor = mutationFactor
    def mutate(self, creature):
        chance = random.random()
        if chance > self.mutationRate:
            return creature.genotype
        
        gt = creature.genotype
        newGt = CreatureGenotype(gt)
        positiveRate =  chance() > 0.5
        if positiveRate:
            newGt.rerollStatBudget(newGt.statsBudget + self.mutationFactor)
            newGt.rerollPowerBudget(newGt.powerBudget - self.mutationFactor)
        else:
            newGt.rerollStatBudget(newGt.statsBudget - self.mutationFactor)
            newGt.rerollPowerBudget(newGt.powerBudget + self.mutationFactor)

        return newGt
