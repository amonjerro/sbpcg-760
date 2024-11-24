from abc import ABC, abstractmethod
import random

from sbpcg import Creature
from sbpcg import CreatureTypes
from sbpcg import CreatureGenotype
from sbpcg import Power


class Factory(ABC):
    @staticmethod
    @abstractmethod
    def make(parameter:int):
        pass

    @staticmethod
    @abstractmethod
    def make_average(creatureType:CreatureTypes, parameter:int):
        pass

class PowerFactory(Factory):
    minPowerValue = 10
    powerIncreaseCost = 10
    adjectives = set([
        "able", "adorable", "adventurous", "aggressive", "agreeable", "alert", "alive", "amazing", "ambitious", 
        "angry", "annoyed", "anxious", "arrogant", "ashamed", "attractive", "average", "awesome", "awful",
        "bad", "beautiful", "better", "bewildered", "bitter", "bizarre", "black", "blue", "bold", 
        "boring", "brave", "bright", "broad", "broken", "bumpy", "busy", "calm", "careful",
        "careless", "cautious", "charming", "cheap", "cheerful", "chilly", "clean", "clever", "clumsy",
        "cold", "colorful", "comfortable", "confident", "confused", "cool", "cooperative", "courageous", "crazy",
        "creepy", "cruel", "curious", "cute", "dangerous", "dark", "dazzling", "dead", "deep",
        "delightful", "dependent", "different", "difficult", "dirty", "dizzy", "doubtful", "dramatic", "dry",
        "dull", "eager", "early", "easy", "elegant", "embarrassed", "empty", "energetic", "enthusiastic",
        "evil", "excited", "expensive", "fabulous", "fair", "faithful", "famous", "fancy", "fantastic",
        "fast", "fat", "fearful", "fierce", "filthy", "fine", "flat", "fluffy", "foolish",
        "fragile", "free", "friendly", "frightened", "funny", "gentle", "giant", "gigantic", "glamorous",
        "gloomy", "glorious", "good", "gorgeous", "graceful", "grateful", "great", "greedy", "green",
        "happy", "hard", "harsh", "healthy", "heavy", "helpful", "helpless", "hilarious", "hollow",
        "honest", "horrible", "hot", "huge", "hungry", "hurt", "important", "impossible", "innocent",
        "intelligent", "interesting", "jealous", "jolly", "joyful", "juicy", "kind", "large", "lazy",
        "light", "lively", "lonely", "long", "loud", "lovely", "lucky", "mad", "magnificent",
        "massive", "melodic", "messy", "modern", "moody", "mysterious", "narrow", "naughty", "nervous",
        "nice", "noisy", "obedient", "obnoxious", "odd", "old", "open", "outgoing", "outrageous",
        "perfect", "pleasant", "plump", "polite", "poor", "powerful", "precious", "prickly", "proud",
        "punctual", "quick", "quiet", "rainy", "rare", "red", "relaxed", "reliable", "rich",
        "ridiculous", "round", "rude", "sad", "safe", "salty", "scary", "selfish", "serene",
        "sharp", "shiny", "short", "shy", "silly", "simple", "skinny", "slimy", "slow",
        "small", "smart", "smooth", "soft", "sour", "sparkling", "spicy", "splendid", "spoiled",
        "strong", "successful", "sweet", "swift", "tall", "tasty", "tense", "terrible", "thick",
        "thin", "thirsty", "thoughtful", "tiny", "tired", "tough", "ugly", "unusual", "vague",
        "vast", "victorious", "warm", "weak", "wet", "white", "wide", "wild", "wise",
        "witty", "wonderful", "worried", "yellow", "young", "yummy", "zealous"
    ])

    battle_words = set([
    "attack", "ambush", "assault", "barrage", "bash", "batter", "block", "blow", "bombard", 
    "break", "breach", "charge", "clash", "cleave", "conquer", "counter", "crack", "crash",
    "crush", "cut", "defend", "destroy", "dodge", "dominate", "duel", "engage", "evade",
    "execute", "explode", "fight", "flank", "fire", "grab", "guard", "hack", "halt",
    "hamstring", "harm", "harpoon", "hit", "hold", "hunt", "impale", "incinerate", "intercept",
    "invade", "jab", "jump", "kick", "kill", "lance", "lunge", "maim", "march",
    "maul", "mow", "neutralize", "overpower", "overrun", "parry", "pelt", "pierce", "plunge",
    "protect", "pummel", "pursue", "push", "quell", "raid", "ram", "repel", "retaliate",
    "retreat", "rush", "sabotage", "sack", "savage", "scout", "seize", "shield", "shoot",
    "siege", "skewer", "slash", "slice", "smash", "snap", "snipe", "soar", "stab",
    "stagger", "stalk", "stand", "storm", "strike", "struggle", "subdue", "sweep", "swing",
    "tackle", "target", "tear", "thrust", "topple", "track", "trap", "traverse", "trample",
    "trap", "trigger", "unleash", "upend", "vanquish", "vault", "vaporize", "wage", "ward",
    "whirl", "wreck", "yank", "ambush", "arrest", "ascend", "assail", "assemble", "backstab",
    "barrage", "befriend", "bind", "blitz", "brandish", "capture", "catapult", "chase", "circle",
    "command", "confine", "confront", "control", "corner", "cripple", "crush", "damage", "deceive",
    "demolish", "deploy", "devastate", "disarm", "disrupt", "distract", "dominate", "eliminate", "embush",
    "engulf", "entangle", "entrap", "envelop", "erupt", "escape", "feint", "flank", "focus",
    "fortify", "gather", "grapple", "harass", "heave", "impair", "inflict", "infiltrate", "intervene",
    "interrupt", "intimidate", "invade", "lacerate", "lay", "lead", "levitate", "lock", "maneuver",
    "march", "marshal", "maul", "obliterate", "outmaneuver", "outwit", "overthrow", "overwhelm", "paralyze",
    "patrol", "pin", "plunder", "polarize", "position", "predict", "prey", "provoke", "puncture",
    "raid", "ram", "ravage", "rally", "recon", "regroup", "reinforce", "relocate", "resist",
    "retreat", "rout", "sabotage", "scatter", "scorch", "secure", "sever", "shatter", "shelter",
    "shove", "snipe", "soar", "stagger", "stomp", "subjugate", "suppress", "surge", "surround",
    "swing", "target", "tear", "torment", "unleash", "uphold", "vanquish", "vault", "vex"
    ])

    @staticmethod
    def make_power_name():
        adjective = random.choice(list(PowerFactory.adjectives)).title()
        action = random.choice(list(PowerFactory.battle_words)).title()
        return f'{adjective} {action}'

    @staticmethod
    def make(parameter:int):
        powerValue = PowerFactory.minPowerValue + (parameter // PowerFactory.powerIncreaseCost)
        return Power(PowerFactory.make_power_name(), powerValue, random.choice(list(CreatureTypes)))
    
    @staticmethod
    def make_average(creatureType, parameter):
        powerValue = PowerFactory.minPowerValue + (parameter // PowerFactory.powerIncreaseCost)
        return Power(PowerFactory.make_power_name(), powerValue, creatureType)
    

class CreatureFactory(Factory):
    @staticmethod
    def make(parameter:int):
        randomType = random.choice(list(CreatureTypes))
        match randomType:
            case CreatureTypes.TypeA:
                creature = CreatureFactory.make_creature_A(parameter)
                return CreatureFactory.add_powers(creature)
            case CreatureTypes.TypeB:
                creature = CreatureFactory.make_creature_B(parameter)
                return CreatureFactory.add_powers(creature)
            case CreatureTypes.TypeC:
                creature = CreatureFactory.make_creature_C(parameter)
                return CreatureFactory.add_powers(creature)
            case CreatureTypes.TypeD:
                creature = CreatureFactory.make_creature_D(parameter)
                return CreatureFactory.add_powers(creature)
            case _:
                print("Something fucky happened")
                

    
    @staticmethod
    def make_average(type:CreatureTypes):
        match type:
            case CreatureTypes.TypeA:
                creature = CreatureFactory.make_average_A()
                return CreatureFactory.add_powers(creature, average=True)
            case CreatureTypes.TypeB:
                creature = CreatureFactory.make_average_B()
                return CreatureFactory.add_powers(creature, average=True)
            case CreatureTypes.TypeC:
                creature = CreatureFactory.make_average_C()
                return CreatureFactory.add_powers(creature, average=True)
            case CreatureTypes.TypeD:
                creature = CreatureFactory.make_average_D()
                return CreatureFactory.add_powers(creature, average=True)
            case _:
                print("Something fucky happened")
    
    @staticmethod
    def make_from_genotype(type:CreatureTypes, gt:CreatureGenotype):
        match type:
            case CreatureTypes.TypeA:
                creature = CreatureFactory.make_creature_A(gt.statsBudget + gt.powerBudget, gt)
                return CreatureFactory.add_powers(creature)
            case CreatureTypes.TypeB:
                creature = CreatureFactory.make_creature_B(gt.statsBudget + gt.powerBudget,gt)
                return CreatureFactory.add_powers(creature)
            case CreatureTypes.TypeC:
                creature = CreatureFactory.make_creature_C(gt.statsBudget + gt.powerBudget,gt)
                return CreatureFactory.add_powers(creature)
            case CreatureTypes.TypeD:
                creature = CreatureFactory.make_creature_D(gt.statsBudget + gt.powerBudget,gt)
                return CreatureFactory.add_powers(creature)
            case _:
                print("Something fucky happened")

    @staticmethod
    def add_powers(creature:Creature, average = False):
        if average:
            creature.add_power(PowerFactory.make_average(CreatureTypes.TypeA, creature.genotype.power1Budget))
            creature.add_power(PowerFactory.make_average(CreatureTypes.TypeB, creature.genotype.power2Budget))
            creature.add_power(PowerFactory.make_average(CreatureTypes.TypeC, creature.genotype.power3Budget))
            creature.add_power(PowerFactory.make_average(CreatureTypes.TypeD, creature.genotype.power4Budget))
        else:
            creature.add_power(PowerFactory.make(creature.genotype.power1Budget))
            creature.add_power(PowerFactory.make(creature.genotype.power2Budget))
            creature.add_power(PowerFactory.make(creature.genotype.power3Budget))
            creature.add_power(PowerFactory.make(creature.genotype.power4Budget))
        return creature

    @staticmethod
    def make_creature_A(totalBudget:int, genotype=None):
        if genotype is None:
            gt = CreatureGenotype(totalBudget)
        else:
            gt = genotype
        #HP conditions
        minHp = 50
        hpGeneCost = 2
        #Attack conditions
        minAttack = 4
        attackGeneCost = 20
        #Speed conditions
        minSpeed = 3
        speedGeneCost = 30

        createdCreature = Creature(
            gt, CreatureTypes.TypeA, 
            minHp + (gt.hpGeneValue // hpGeneCost)*10,
            minAttack + (gt.attackGeneValue // attackGeneCost),
            minSpeed + (gt.speedGeneValue // speedGeneCost)
            )
        return createdCreature


    
    @staticmethod
    def make_average_A():
        gt = CreatureGenotype(0)
        gt.rerollPowerBudget(250)
        return Creature(gt, CreatureTypes.TypeA, 650, 7, 4)
    

    @staticmethod
    def make_creature_B(totalBudget:int, genotype=None):
        if genotype is None:
            gt = CreatureGenotype(totalBudget)
        else:
            gt = genotype
        minHp = 70
        hpGeneCost = 4
        minAttack = 7
        attackGeneCost = 15
        minSpeed = 2
        speedGeneCost = 25
        
        createdCreature = Creature(
            gt, CreatureTypes.TypeB, 
            minHp + (gt.hpGeneValue // hpGeneCost)*10,
            minAttack + (gt.attackGeneValue // attackGeneCost),
            minSpeed + (gt.speedGeneValue // speedGeneCost)
            )
        return createdCreature
    
    @staticmethod
    def make_average_B():
        gt = CreatureGenotype(0)
        gt.rerollPowerBudget(250)
        return Creature(gt, CreatureTypes.TypeB, 390, 11, 3)

    @staticmethod
    def make_creature_C(totalBudget:int, genotype = None):
        if genotype is None:
            gt = CreatureGenotype(totalBudget)
        else:
            gt = genotype
        minHp = 85
        hpGeneCost = 2
        minAttack = 7
        attackGeneCost = 10
        minSpeed = 2
        speedGeneCost = 35

        createdCreature = Creature(
            gt, CreatureTypes.TypeC, 
            minHp + (gt.hpGeneValue // hpGeneCost)*10,
            minAttack + (gt.attackGeneValue // attackGeneCost),
            minSpeed + (gt.speedGeneValue // speedGeneCost)
            )
        return createdCreature

    @staticmethod
    def make_average_C():
        gt = CreatureGenotype(0)
        gt.rerollPowerBudget(250)
        return Creature(gt, CreatureTypes.TypeC, 700, 12, 3)

    @staticmethod
    def make_creature_D(totalBudget:int, genotype = None):
        if genotype is None:
            gt = CreatureGenotype(totalBudget)
        else:
            gt = genotype
        minHp = 70
        hpGeneCost = 4

        minAttack = 3
        attackGeneCost = 25

        minSpeed = 6
        speedGeneCost = 15


        return Creature(
            gt, CreatureTypes.TypeD,
            minHp + (gt.hpGeneValue // hpGeneCost)*10,
            minAttack + (gt.attackGeneValue // attackGeneCost),
            minSpeed + (gt.speedGeneValue // speedGeneCost)
        )
    
    @staticmethod
    def make_average_D():
        gt = CreatureGenotype(0)
        gt.rerollPowerBudget(250)
        return Creature(gt,CreatureTypes.TypeD, 380, 5, 8)