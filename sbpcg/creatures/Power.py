from .Creature import CreatureTypes
class Power:
    def __init__(self, powerName, effect, type:CreatureTypes):
        self.name = powerName
        self.effect = effect
        self.type = type
    def __str__(self):
        return f'{self.name}, {self.effect}, {self.type.name}'