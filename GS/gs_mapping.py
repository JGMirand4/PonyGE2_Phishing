class GSMapping:
    def __init__(self, grammar):
        self.grammar = grammar

    def map(self, position):
        phenotype = ""
        for non_terminal in self.grammar.non_terminals():
            rule_choice = int(position[non_terminal] % len(self.grammar[non_terminal]))
            phenotype += self.grammar[non_terminal][rule_choice] + " "
        return phenotype.strip()
