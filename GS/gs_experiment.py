from gs_pso import Particle
from gs_mapping import GSMapping
from gs_fitness import evaluate_fitness

# Parâmetros do experimento
num_particles = 30
max_iterations = 100
dimensions = len(grammar.non_terminals())
bounds = (0, 10)

# Inicialização
particles = [Particle(dimensions, bounds) for _ in range(num_particles)]
mapping = GSMapping(grammar)
global_best_position = np.zeros(dimensions)
global_best_fitness = float('inf')

# PSO
for iteration in range(max_iterations):
    for particle in particles:
        phenotype = mapping.map(particle.position)
        fitness = evaluate_fitness(phenotype)

        if fitness < particle.best_fitness:
            particle.best_fitness = fitness
            particle.best_position = np.copy(particle.position)

        if fitness < global_best_fitness:
            global_best_fitness = fitness
            global_best_position = np.copy(particle.position)

    for particle in particles:
        particle.update_velocity(global_best_position)
        particle.update_position(bounds)

# Resultados finais
best_phenotype = mapping.map(global_best_position)
print(f"Best phenotype: {best_phenotype}")
