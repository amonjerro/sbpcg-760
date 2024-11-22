#from sbpcg import Population
# from sbpcg import ReproductionStrategy

class Simulation:
    def __init__(self, population, repStrat):
        self.population = population
    
    def populate(self):
        self.population.make_population()