from sbpcg import Factory
from sbpcg import Transformer

class Population:
    def __init__(self, population_size:int, survivors:int, makeTuningParameter:int, individualFactory:Factory, transformer:Transformer):
        self.population_size = population_size
        self.makeTuningParameter = makeTuningParameter
        self.factory = individualFactory
        self.current_population = []
        self.transformer = transformer
        self.survivors = survivors
    def make_population(self):
        if len(self.current_population):
            # Create random children for first iteration
            for i in range(self.population_size):
                self.current_population.append(self.factory.make(self.makeTuningParameter))
    def add_individual(self, individual):
        self.current_population.append(individual)
    def transform(self, index):
        return self.transformer.transform(self.current_population[index])
    def cull(self):
        self.current_population = sorted(self.current_population, key=lambda x: x.fitness)
        self.current_population = self.current_population[:self.survivors]