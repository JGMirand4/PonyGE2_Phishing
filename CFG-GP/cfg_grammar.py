from deap import gp

def cfg_grammar():
    pset = gp.PrimitiveSetTyped("MAIN", [], int)
    pset.addPrimitive(operator.add, [int, int], int)
    pset.addPrimitive(operator.sub, [int, int], int)
    pset.addPrimitive(operator.mul, [int, int], int)
    pset.addPrimitive(protected_div, [int, int], int)
    pset.addTerminal(1, int)
    pset.addTerminal(0, int)
    return pset
