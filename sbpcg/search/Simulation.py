from .ReproductionStrat import ReproductionStrategy
from .MutationStrat import MutationStrategy
from .Evaluator import Fitness
from .Population import Population


from sbpcg import CreatureTypes

from dataclasses import dataclass

@dataclass
class GenerationData:
    averageFitness:float = 0
    typeACount:int = 0
    averageAFitness:float = 0
    averageAStatsBudget:float = 0
    averageAPowerBudget:float = 0
    typeBCount:int = 0
    averageBFitness:float = 0
    averageBStatsBudget:float = 0
    averageBPowerBudget:float = 0
    typeCCount:int = 0
    averageCFitness:float = 0
    averageCStatsBudget:float = 0
    averageCPowerBudget:float = 0
    typeDCount:int = 0
    averageDFitness:float = 0
    averageDStatsBudget:float = 0
    averageDPowerBudget:float = 0

    def flatten(self):
        return [
            self.averageFitness,        #0
            self.typeACount,            #1
            self.averageAFitness,       #2
            self.averageAStatsBudget,   #3
            self.averageAPowerBudget,   #4
            self.typeBCount,            #5
            self.averageBFitness,       #6
            self.averageBStatsBudget,   #7
            self.averageBPowerBudget,   #8
            self.typeCCount,            #9
            self.averageCFitness,       #10
            self.averageCStatsBudget,   #11
            self.averageCPowerBudget,   #12
            self.typeDCount,            #13
            self.averageDFitness,       #14
            self.averageDStatsBudget,   #15
            self.averageDPowerBudget    #16
        ]
    
    def get_headers(self):
        return [
            'averageFitness',
            'typeACount',
            'averageAFitness',
            'averageAStatsBudget',
            'averageAPowerBudget',
            'typeBCount',
            'averageBFitness',
            'averageBStatsBudget',
            'averageBPowerBudget',
            'typeCCount',
            'averageCFitness',
            'averageCStatsBudget',
            'averageCPowerBudget',
            'typeDCount',
            'averageDFitness',
            'averageDStatsBudget',
            'averageDPowerBudget'
        ]

class Simulation:
    def __init__(self, generations:int, population:Population, repStrat:ReproductionStrategy, mutationStrat: MutationStrategy, fitnessFunction:Fitness, replacement=False):
        self.pop = population
        self.rep = repStrat
        self.useReplacement = replacement
        self.generationsToRun = generations
        self.mut = mutationStrat
        self.fitness = fitnessFunction
        self.currentIteration = 0
        self.dataByGeneration = []
    
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
        self.showFitnessImprovement()
        self.showPopulationDistributionChange()

    def get_generation_data(self, flatten = True):
        if (flatten):
            return [i.flatten() for i in self.dataByGeneration]
        else:
            return self.dataByGeneration

    def make_data_snapshot(self):
        gd = GenerationData()
        popCounter = [0,0,0,0]
        fitnessByType = [0,0,0,0]
        statsBudget = [0,0,0,0]
        powerBudget = [0,0,0,0]
        
        # Get population data by type
        for i in self.pop.current_population:
            popCounter[i.type] += 1
            statsBudget[i.type] += i.genotype.statsBudget
            powerBudget[i.type] += i.genotype.powerBudget
            fitnessByType[i.type] += i.fitness
        
        totalFitness = sum(fitnessByType)
        gd.typeACount = popCounter[CreatureTypes.TypeA]
        gd.typeBCount = popCounter[CreatureTypes.TypeB]
        gd.typeCCount = popCounter[CreatureTypes.TypeC]
        gd.typeDCount = popCounter[CreatureTypes.TypeD]
        
        # Get averages
        for i in CreatureTypes:
            if popCounter[i] == 0:
                continue
            fitnessByType[i] /= popCounter[i]
            statsBudget[i] /= popCounter[i]
            powerBudget[i] /= popCounter[i]
        
        # Apply
        gd.averageFitness = totalFitness / self.pop.population_size
        gd.averageAFitness = fitnessByType[CreatureTypes.TypeA]
        gd.averageAStatsBudget = statsBudget[CreatureTypes.TypeA]
        gd.averageAPowerBudget = powerBudget[CreatureTypes.TypeA]
        
        gd.averageBFitness = fitnessByType[CreatureTypes.TypeB]
        gd.averageBStatsBudget = statsBudget[CreatureTypes.TypeB]
        gd.averageBPowerBudget = powerBudget[CreatureTypes.TypeB]
        
        gd.averageCFitness = fitnessByType[CreatureTypes.TypeC]
        gd.averageCStatsBudget = statsBudget[CreatureTypes.TypeC]
        gd.averageCPowerBudget = powerBudget[CreatureTypes.TypeC]
        
        gd.averageDFitness = fitnessByType[CreatureTypes.TypeD]
        gd.averageDStatsBudget = statsBudget[CreatureTypes.TypeD]
        gd.averageDPowerBudget = powerBudget[CreatureTypes.TypeD]

        self.dataByGeneration.append(gd)

    def run_simulation_step(self):
        # Populate
        self.populate()

        # Select
        fitnessValues = [self.fitness.evaluate(self.pop.transform(i)) for i in range(self.pop.population_size)]
        for i in range(len(fitnessValues)):
            self.pop.current_population[i].fitness = fitnessValues[i]
        
        #Gather data
        self.make_data_snapshot()
        
        # Cull
        self.pop.cull()

    def showFitnessImprovement(self):
        print('==== Fitness Improvement ====')
        print(f'Start Average Fitness: {self.dataByGeneration[0].averageFitness}')
        print(f'Last Gen Fitness: {self.dataByGeneration[-1].averageFitness}')

    def showPopulationDistributionChange(self):
        print('==== Population Distribution Change ====')
        print(f'[{self.dataByGeneration[0].typeACount}, {self.dataByGeneration[0].typeBCount}, {self.dataByGeneration[0].typeCCount}, {self.dataByGeneration[0].typeDCount}]')
        print(f'[{self.dataByGeneration[-1].typeACount}, {self.dataByGeneration[-1].typeBCount}, {self.dataByGeneration[-1].typeCCount}, {self.dataByGeneration[-1].typeDCount}]')