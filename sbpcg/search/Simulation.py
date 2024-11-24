from .ReproductionStrat import ReproductionStrategy
from .MutationStrat import MutationStrategy
from .Evaluator import Fitness
from .Population import Population

class Simulation:
    def __init__(self, generations:int, population:Population, repStrat:ReproductionStrategy, mutationStrat: MutationStrategy, fitnessFunction:Fitness, replacement=False):
        self.pop = population
        self.rep = repStrat
        self.useReplacement = replacement
        self.generationsToRun = generations
        self.mut = mutationStrat
        self.fitness = fitnessFunction
        self.currentIteration = 0
    
    def populate(self):
        if (self.currentIteration == 0):
            self.pop.make_population()
        else:
            individualsNeeded = self.pop.get_new_candidate_count()
            individualsCreated = []
            for i in range(individualsNeeded):
                candidates = self.pop.get_random_candidates(self.useReplacement)
                individualsCreated.append(self.rep.reproduce(candidates[0], candidates[1], self.mut))
            self.pop.current_population += individualsCreated
    
    def run_simulation(self):
        self.currentIteration = 0
        for i in range(self.generationsToRun):
            self.run_simulation_step()
            self.currentIteration += 1

    def run_simulation_step(self):
        # Populate
        self.populate()

        # Select
        fitnessValues = [self.fitness.evaluate(self.pop.transform(i)) for i in range(self.pop.population_size)]
        for i in range(len(fitnessValues)):
            self.pop.current_population[i].fitness = fitnessValues[i]
        
        # Cull
        self.pop.cull()