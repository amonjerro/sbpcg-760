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
        newGt = CreatureGenotype(gt.powerBudget + gt.statsBudget)
        positiveRate =  random.random() > 0.5
        if positiveRate:
            newGt.rerollStatBudget(gt.statsBudget + self.mutationFactor)
            newGt.rerollPowerBudget(gt.powerBudget - self.mutationFactor)
        else:
            newGt.rerollStatBudget(gt.statsBudget - self.mutationFactor)
            newGt.rerollPowerBudget(gt.powerBudget + self.mutationFactor)

        return newGt
