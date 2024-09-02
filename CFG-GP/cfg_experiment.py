from deap import tools, algorithms
from cfg_gp import toolbox
from cfg_grammar import cfg_grammar

# Parâmetros do experimento
population_size = 100
generations = 40

# Inicialização
population = toolbox.population(n=population_size)
pset = cfg_grammar()

toolbox.register("evaluate", eval_fitness_function)  # Defina a função de avaliação de fitness
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutUniform, expr=toolbox.expr_mut, pset=pset)
toolbox.register("select", tools.selTournament, tournsize=3)

# Evolução
algorithms.eaSimple(population, toolbox, 0.5, 0.2, generations)

# Resultados finais
best_individual = tools.selBest(population, 1)[0]
print(f"Best individual: {best_individual}")
