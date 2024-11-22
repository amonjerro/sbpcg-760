from sbpcg import Population
from sbpcg import CreatureFactory, CreatureTransformer, GenotypeTransformer
from sbpcg import CSVExporter

if __name__ == '__main__':
    populationSize = 10
    geneticBudget = 500

    phenotypeExporter = CSVExporter('./output', 'phenotype_population')
    genotypeExporter = CSVExporter('./output', 'genotype_population')

    pop = Population(populationSize, geneticBudget, CreatureFactory, CreatureTransformer)
    pop.make_population()
    phenotypeExporter.export([pop.transform(i) for i in range(populationSize)], CreatureTransformer.get_headers())
    genotypeExporter.export(map(lambda x: GenotypeTransformer.transform(x), pop.current_population), GenotypeTransformer.get_headers())
    
