# Search-Based Procedural Content Generation based on Genetic Algorithms

This Python module creates procedurally generates creatures for a very simplified version of a Pokemon-like game. Through the use of an implementation of evolutionary strategies and the cross-over reproduction of genetic algorithms, it searches through the possibility space of content fitness to improve the fighting capabilities of created creatures in response to a specific chosen type.

## Game Rules

Combat in this game is mediated by four stats in total.

- **HP**: How much damage it can take before fainting.

- **Attack**: How much power is behind every action chosen

- **Speed**: How quickly it can set off its intended action. If higher than the enemy's speed, this creature goes first. Ties are decided by a coin toss.

- **Type**: The type of this creature with regards to the weakness system.

The creatures have access to powers that are composed of the following information:
- **Name** - The name of the power
- **Effect** - The effect value of the power, that is, how strong it is.
- **Type** - The type of this power.

Damage calculation is as follows:

```
Damage = Attack * Effect * STAB * Resistance/Weakness
```

Where STAB is defined as Same-Type-Attack-Bonus, a modifier that is applied to the calculation when there is a match between the power type and the type of the creature executing the attack.

Creatures can't be changed mid battle.

## Genetics and Phenotypes

The stats presented in the above section can be translated into a phenotype vector.

```
Power = (Effect, Type)
Creature = [Type, HP Value, Attack Value, Speed Value, Power1, Power2, Power3, Power4]

[0, 90, 14, 4, (17, 1), (10, 1), (14, 3), (17, 0)]
```

To create these phenotypes, we start by setting a genetic budget. This budget is then split between a `StatsBudget` and a `PowersBudget`. The `StatsBudget` is then distributed between the three stats and the `PowerBudget` is distributed between the four power slots.

Therefore, a genotype vector would look like this
```
[StatsBudget, PowerBudget, Hp, Attack, Speed, Effect1, Effect2, Effect3, Effect4]
[298, 202, 9, 206, 46, 73, 4, 46, 70]
```

## Fitness
In order to calculate fitness, a high-level simplified simulation of the combat is run. Each side chooses to pick their most effective power against the opposition and solely rely on that move for the entire fight. The amount of turns to win for each side is calculated based on this.

If a candidate in the population is calculated to win before the creature that acts as the selection criteria, then fitness is added based on how little damage they take to be victorious. Likewise, if they are calculated to lose, then their fitness is reduced by how much life left the opposition has. Ideally, losers go down fighting and winners win unscathed.

## Reproduction and Mutation