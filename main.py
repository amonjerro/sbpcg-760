import time

from sbpcg import Population, Simulation, CrossTypeReproduction, BudgetMutationStrategy
from sbpcg import Simulation
from sbpcg import CreatureFactory, CreatureTransformer, GenotypeTransformer, FitnessTransformer
from sbpcg import CSVExporter, ImageExporter
from sbpcg import CreatureTypes
from sbpcg import VectorEvaluator

def main():
    generationsToRun = 20
    useReplacement = False
    
    populationSize = 2000
    survivors = 500

    geneticBudget = 500

    mutationRate = 0.1
    mutationFactor = 10

    phenotypeExporter = CSVExporter('./output')
    genotypeExporter = CSVExporter('./output')
    visualizer = ImageExporter('./output/images', 'jpg')

    AverageTypeA = CreatureFactory.make_average(CreatureTypes.TypeA)
    AverageTypeB = CreatureFactory.make_average(CreatureTypes.TypeB)
    AverageTypeC = CreatureFactory.make_average(CreatureTypes.TypeC)
    AverageTypeD = CreatureFactory.make_average(CreatureTypes.TypeD)

    theLads = [AverageTypeA, AverageTypeB, AverageTypeC, AverageTypeD]
    genotypeExporter.export(map(lambda x: GenotypeTransformer.transform(x), theLads), GenotypeTransformer.get_headers(),'geno_control')
    phenotypeExporter.export(map(lambda x: CreatureTransformer.transform(x), theLads), CreatureTransformer.get_headers(),'pheno_control')

    pop = Population(populationSize, survivors, geneticBudget, CreatureFactory, CreatureTransformer)
    rep = CrossTypeReproduction()
    mut = BudgetMutationStrategy(mutationRate=mutationRate,mutationFactor=mutationFactor)
    
    start_time = time.time()
    for lad in theLads:
        fitness = VectorEvaluator(CreatureTransformer.transform(lad))
        sim = Simulation(generationsToRun, pop, rep, mut, fitness, useReplacement)
        sim.run_simulation()

        #Export last generation
        phenotypeExporter.export(map(lambda x: FitnessTransformer.transform(x), pop.current_population), FitnessTransformer.get_headers(), f"phenotype_population-lad-{lad.type}")
        genotypeExporter.export(map(lambda x: GenotypeTransformer.transform(x), pop.current_population), GenotypeTransformer.get_headers(), f"genotype_population-lad-{lad.type}")
        visualizer.export(sim.get_generation_data(), f'Lad-{lad.type}')
    end_time = time.time()

    
    #print(end_time - start_time)

if __name__ == '__main__':
    main()