from sbpcg import Population
from sbpcg import CreatureFactory, CreatureTransformer, GenotypeTransformer, FitnessTransformer
from sbpcg import CSVExporter
from sbpcg import CreatureTypes
from sbpcg import VectorEvaluator

if __name__ == '__main__':
    populationSize = 20
    geneticBudget = 500

    phenotypeExporter = CSVExporter('./output', 'phenotype_population')
    genotypeExporter = CSVExporter('./output', 'genotype_population')

    AverageTypeA = CreatureFactory.make_average(CreatureTypes.TypeA)
    AverageTypeB = CreatureFactory.make_average(CreatureTypes.TypeB)
    AverageTypeC = CreatureFactory.make_average(CreatureTypes.TypeC)
    AverageTypeD = CreatureFactory.make_average(CreatureTypes.TypeD)
    theLads = [AverageTypeA, AverageTypeB, AverageTypeC, AverageTypeD]

    pop = Population(populationSize, geneticBudget, CreatureFactory, CreatureTransformer)
    pop.make_population()
    evaluatorTypeA = VectorEvaluator(CreatureTransformer.transform(AverageTypeA))
    fitnessValues = [evaluatorTypeA.evaluate(pop.transform(i)) for i in range(populationSize)]
    for i in range(len(fitnessValues)):
        pop.current_population[i].fitness = fitnessValues[i]

    #Export for analysis
    phenotypeExporter.export(map(lambda x: FitnessTransformer.transform(x), pop.current_population), FitnessTransformer.get_headers())
    genotypeExporter.export(map(lambda x: GenotypeTransformer.transform(x), pop.current_population), GenotypeTransformer.get_headers())
    
