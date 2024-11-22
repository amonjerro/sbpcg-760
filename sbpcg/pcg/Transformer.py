from abc import ABC, abstractmethod
from sbpcg import Creature, Power

class Transformer(ABC):
    @staticmethod
    @abstractmethod
    def transform(target):
        pass

class PowerTransformer(Transformer):
    @staticmethod
    def transform(target:Power):
        return [target.effect, int(target.type)]

class CreatureTransformer(Transformer):
    @staticmethod
    def transform(target:Creature):
        ## Transform the creature
        output = [int(target.type), target.hp, target.atk, target.speed]
        ## Append the powers
        for power in target.powers:
            output += PowerTransformer.transform(power)
        return output
