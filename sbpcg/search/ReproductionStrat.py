from abc import ABC, abstractmethod
import random
from sbpcg import Creature, CreatureGenotype
# from sbpcg import MutationStrategy
from sbpcg import CreatureFactory

class ReproductionStrategy(ABC):
    @staticmethod
    @abstractmethod
    def reproduce(candidateA:Creature, candidateB:Creature, mutationStrategy):
        pass

class CrossTypeReproduction(ReproductionStrategy):
    @staticmethod
    @abstractmethod
    def reproduce(candidateA, candidateB, mutationStrategy):
        targetGenotype = None
        type = None
        bSide = random.random() > 0.5
        if (bSide):
            targetGenotype = mutationStrategy.mutate(candidateA)
            type = candidateB.type
        else:
            targetGenotype = mutationStrategy.mutate(candidateB)
            type = candidateA.type
        return CreatureFactory.make_from_genotype(type, targetGenotype)



