import random
from typing import List, Any

from sbpcg import Factory
from sbpcg import Transformer

class Population:
    def __init__(self, population_size:int, survivors:int, make_tuning_param:int, individualFactory:Factory, transformer:Transformer):
        self.population_size = population_size
        self.make_tuning_param = make_tuning_param
        self.factory = individualFactory
        self.current_population = []
        self.transformer = transformer
        self.survivors = survivors
    def is_underpopulated(self):
        return self.population_size > len(self.current_population)
    def get_new_candidate_count(self):
        return self.population_size - len(self.current_population)
    def make_population(self):
        self.current_population = self.current_population[:0]
        for i in range(self.population_size):
            self.current_population.append(self.factory.make(self.make_tuning_param))
    def get_random_candidates(self, withReplacement:bool = False):
        individuals = []
        firstChoice = random.randint(0, len(self.current_population)-1)
        secondChoice = random.randint(0, len(self.current_population)-1)
        if not withReplacement:
            while firstChoice == secondChoice:
                secondChoice = random.randint(0, len(self.current_population)-1)
        individuals.append(self.current_population[firstChoice])
        individuals.append(self.current_population[secondChoice])
        return individuals
        
    def add_individuals(self, individuals:List[Any]):
        self.current_population += individuals
    def transform(self, index):
        return self.transformer.transform(self.current_population[index])
    def cull(self):
        self.current_population = sorted(self.current_population, key=lambda x: -x.fitness)
        self.current_population = self.current_population[:self.survivors]