from abc import ABC, abstractmethod
import random

from sbpcg import Creature
from sbpcg import CreatureTypes
from sbpcg import Power


class Factory(ABC):
    @staticmethod
    @abstractmethod
    def make():
        pass

class PowerFactory(Factory):
    minPowerValue = 10
    maxPowerValue = 50
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
    def make():
        adjective = random.choice(list(PowerFactory.adjectives)).title()
        action = random.choice(list(PowerFactory.battle_words)).title()
        return Power(f'{adjective} {action}', random.randint(PowerFactory.minPowerValue, PowerFactory.maxPowerValue), random.choice(list(CreatureTypes)))
    

class CreatureFactory(Factory):
    @staticmethod
    def make():
        randomType = random.choice(list(CreatureTypes))
        match randomType:
            case CreatureTypes.TypeA:
                creature = CreatureFactory.make_creature_A()
                return CreatureFactory.add_powers(creature)
            case CreatureTypes.TypeB:
                creature = CreatureFactory.make_creature_B()
                return CreatureFactory.add_powers(creature)
            case CreatureTypes.TypeC:
                creature = CreatureFactory.make_creature_C()
                return CreatureFactory.add_powers(creature)
            case CreatureTypes.TypeD:
                creature = CreatureFactory.make_creature_D()
                return CreatureFactory.add_powers(creature)
            case _:
                print("Something fucky happened")

    @staticmethod
    def add_powers(creature:Creature):
        creature.add_power(PowerFactory.make())
        creature.add_power(PowerFactory.make())
        creature.add_power(PowerFactory.make())
        creature.add_power(PowerFactory.make())

        return creature

    @staticmethod
    def make_creature_A():
        minHp = 50
        maxHp = 70

        minAttack = 4
        maxAttack = 6

        minSpeed = 3
        maxSpeed = 7

        newCreature = Creature(CreatureTypes.TypeA, random.randint(minHp, maxHp), random.randint(minAttack, maxAttack), random.randint(minSpeed, maxSpeed))
        return newCreature
    

    @staticmethod
    def make_creature_B():
        minHp = 75
        maxHp = 85

        minAttack = 8
        maxAttack = 10

        minSpeed = 4
        maxSpeed = 6

        newCreature = Creature(CreatureTypes.TypeB, random.randint(minHp, maxHp), random.randint(minAttack, maxAttack), random.randint(minSpeed, maxSpeed))
        return newCreature
    
    @staticmethod
    def make_creature_C():
        minHp = 85
        maxHp = 115

        minAttack = 7
        maxAttack = 12

        minSpeed = 3
        maxSpeed = 5

        newCreature = Creature(CreatureTypes.TypeC, random.randint(minHp, maxHp), random.randint(minAttack, maxAttack), random.randint(minSpeed, maxSpeed))
        return newCreature

    @staticmethod
    def make_creature_D():
        minHp = 70
        maxHp = 90

        minAttack = 5
        maxAttack = 7

        minSpeed = 7
        maxSpeed = 10

        newCreature = Creature(CreatureTypes.TypeD, random.randint(minHp, maxHp), random.randint(minAttack, maxAttack), random.randint(minSpeed, maxSpeed))
        return newCreature