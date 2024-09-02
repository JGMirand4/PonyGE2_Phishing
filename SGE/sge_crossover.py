import numpy as np

def sge_crossover(parent1, parent2):
    child1, child2 = {}, {}
    for non_terminal in parent1:
        crossover_point = np.random.randint(1, len(parent1[non_terminal]))
        child1[non_terminal] = np.concatenate((parent1[non_terminal][:crossover_point],
                                               parent2[non_terminal][crossover_point:]))
        child2[non_terminal] = np.concatenate((parent2[non_terminal][:crossover_point],
                                               parent1[non_terminal][crossover_point:]))
    return child1, child2

