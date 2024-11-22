from abc import ABC, abstractmethod
from sbpcg import Creature, Power

class Transformer(ABC):
    @staticmethod
    @abstractmethod
    def transform(target):
        pass

    @staticmethod
    @abstractmethod
    def get_headers():
        pass

class PowerTransformer(Transformer):
    @staticmethod
    def transform(target:Power):
        return [(target.effect, int(target.type))]
    
    @staticmethod
    def get_headers():
        return ['(effect/type)']

class CreatureTransformer(Transformer):
    @staticmethod
    def transform(target:Creature):
        ## Transform the creature
        output = [int(target.type), target.hp, target.atk, target.speed]
        ## Append the powers
        for power in target.powers:
            output += PowerTransformer.transform(power)
        return output
    
    @staticmethod
    def get_headers():
        return ['type', 'hp', 'attack', 'speed', 'power_1', 'power_2', 'power_3', 'power_4']


class GenotypeTransformer(Transformer):
    @staticmethod
    def get_headers():
        return ['stats', 'powers', 'hp', 'atk', 'speed']
    
    @staticmethod
    def transform(target:Creature):
        gt = target.genotype
        return [gt.statsBudget, gt.powerBudget, gt.hpGeneValue, gt.attackGeneValue, gt.speedGeneValue]