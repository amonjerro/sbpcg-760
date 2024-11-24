import time

from sbpcg import Population, Simulation, CrossTypeReproduction, BudgetMutationStrategy
from sbpcg import Simulation
from sbpcg import CreatureFactory, CreatureTransformer, GenotypeTransformer, FitnessTransformer
from sbpcg import CSVExporter, ImageExporter
from sbpcg import CreatureTypes
from sbpcg import VectorEvaluator

if __name__ == '__main__':
    generationsToRun = 10
    useReplacement = False
    
    populationSize = 2000
    survivors = 500

    geneticBudget = 500

    mutationRate = 0.1
    mutationFactor = 10

    phenotypeExporter = CSVExporter('./output')
    genotypeExporter = CSVExporter('./output')

    AverageTypeA = CreatureFactory.make_average(CreatureTypes.TypeA)
    AverageTypeB = CreatureFactory.make_average(CreatureTypes.TypeB)
    AverageTypeC = CreatureFactory.make_average(CreatureTypes.TypeC)
    AverageTypeD = CreatureFactory.make_average(CreatureTypes.TypeD)
    theLads = [AverageTypeA, AverageTypeB, AverageTypeC, AverageTypeD]

    pop = Population(populationSize, survivors, geneticBudget, CreatureFactory, CreatureTransformer)
    fitness = VectorEvaluator(CreatureTransformer.transform(AverageTypeA))
    rep = CrossTypeReproduction()
    mut = BudgetMutationStrategy(mutationRate=mutationRate,mutationFactor=mutationFactor)
    sim = Simulation(generationsToRun, pop, rep, mut, fitness, useReplacement)

    start_time = time.time()
    sim.run_simulation()
    end_time = time.time()

    #Export for analysis
    genotypeExporter.export(map(lambda x: GenotypeTransformer.transform(x), theLads), GenotypeTransformer.get_headers(),'geno_control')
    phenotypeExporter.export(map(lambda x: CreatureTransformer.transform(x), theLads), CreatureTransformer.get_headers(),'pheno_control')
    phenotypeExporter.export(map(lambda x: FitnessTransformer.transform(x), pop.current_population), FitnessTransformer.get_headers(), "phenotype_population")
    genotypeExporter.export(map(lambda x: GenotypeTransformer.transform(x), pop.current_population), GenotypeTransformer.get_headers(), "genotype_population")

    visualizer = ImageExporter('./output', 'jpg')
    visualizer.export(sim.get_generation_data(), 'test')

    print(end_time - start_time)