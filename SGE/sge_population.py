from ponyge.population import Population
from sge_individual import SGEIndividual

class SGEPopulation(Population):
    def __init__(self, grammar, population_size, max_depth):
        self.grammar = grammar
        self.population_size = population_size
        self.max_depth = max_depth
        self.individuals = self._initialize_population()

    def _initialize_population(self):
        return [SGEIndividual(self.grammar, self.max_depth) for _ in range(self.population_size)]
