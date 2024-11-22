from sbpcg import Population, CreatureTransformer
from sbpcg import CreatureFactory

if __name__ == '__main__':
    pop = Population(1500, CreatureFactory, CreatureTransformer)
    pop.make_population()
    print(pop.current_population[0])
    print(pop.transform())