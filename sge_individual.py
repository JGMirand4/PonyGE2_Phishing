import numpy as np
from ponyge.individual import Individual

class SGEIndividual(Individual):
    def __init__(self, grammar, max_depth):
        self.grammar = grammar
        self.max_depth = max_depth
        self.genotype = self._initialize_genotype()
        self.phenotype = None
        self.fitness = None

    def _initialize_genotype(self):
        genotype = {}
        for non_terminal in self.grammar.non_terminals():
            options = len(self.grammar[non_terminal])
            genotype[non_terminal] = np.random.randint(0, options, size=self.max_depth)
        return genotype
