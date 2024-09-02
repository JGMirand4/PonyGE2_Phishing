class SGEMapping:
    def __init__(self, grammar):
        self.grammar = grammar

    def map(self, genotype):
        phenotype = ""
        for non_terminal in genotype:
            production_rules = self.grammar[non_terminal]
            for rule_choice in genotype[non_terminal]:
                phenotype += production_rules[rule_choice] + " "
        return phenotype.strip()
