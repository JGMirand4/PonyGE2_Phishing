from sge_population import SGEPopulation
from sge_mapping import SGEMapping
from ponyge.operators.selection import tournament_selection
from ponyge.operators.replacement import generational_replacement
from ponyge.operators.crossover import one_point_crossover
from ponyge.operators.mutation import integer_mutation

# Parâmetros
population_size = 100
max_generations = 50
max_depth = 10
grammar = load_grammar('path_to_your_bnf_file.bnf')

# Inicialização
population = SGEPopulation(grammar, population_size, max_depth)
mapping = SGEMapping(grammar)

# Evolução
for generation in range(max_generations):
    for individual in population.individuals:
        individual.phenotype = mapping.map(individual.genotype)
        individual.fitness = evaluate_fitness(individual.phenotype)
    
    new_population = []
    while len(new_population) < population_size:
        parent1 = tournament_selection(population.individuals)
        parent2 = tournament_selection(population.individuals)
        child1, child2 = one_point_crossover(parent1, parent2)
        child1 = integer_mutation(child1, max_value=len(grammar.non_terminals()) - 1)
        child2 = integer_mutation(child2, max_value=len(grammar.non_terminals()) - 1)
        new_population.extend([child1, child2])

    population.individuals = generational_replacement(population.individuals, new_population)

# Resultados finais
best_individual = max(population.individuals, key=lambda ind: ind.fitness)
print(f"Best phenotype: {best_individual.phenotype}")
