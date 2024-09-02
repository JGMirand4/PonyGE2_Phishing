import numpy as np

class SGEGenotype:
    def __init__(self, grammar, population_size, max_depth):
        self.grammar = grammar
        self.population_size = population_size
        self.max_depth = max_depth
        self.genotypes = self._initialize_population()

    def _initialize_population(self):
        population = []
        for _ in range(self.population_size):
            genotype = {}
            for non_terminal in self.grammar.non_terminals():
                options = len(self.grammar[non_terminal])
                genotype[non_terminal] = np.random.randint(0, options, size=self.max_depth)
            population.append(genotype)
        return population
