from sbpcg import Factory
from sbpcg import Transformer

class Population:
    def __init__(self, population_size:int, individualFactory:Factory, transformer:Transformer):
        self.population_size = population_size
        self.factory = individualFactory
        self.current_population = []
        self.transformer = transformer
    def make_population(self):
        for i in range(self.population_size):
            self.current_population.append(self.factory.make())
    def transform(self):
        return self.transformer.transform(self.current_population[0])