https://theses.liacs.nl/pdf/2019-2020-LouYitan.pdf
Vamos abordar os algoritmos Structured Grammatical Evolution (SGE), Grammar-based Genetic Programming (GS), e Context-Free Grammar Genetic Programming (CFG-GP) de uma maneira bem detalhada, para que você possa entender claramente cada um deles, mesmo que esteja começando agora.

### 1. **Structured Grammatical Evolution (SGE)**

#### **O que é?**
SGE é uma variação do Grammatical Evolution (GE), que é uma técnica de programação genética onde soluções (ou indivíduos) são geradas através de regras definidas em uma Gramática Livre de Contexto (CFG). A grande diferença do SGE para o GE tradicional é que o SGE organiza os genes de forma que cada não-terminal da gramática tenha uma sequência específica de genes. Isso melhora o controle sobre como as regras da gramática são aplicadas, tornando o processo evolutivo mais eficiente.

#### **Componentes Principais:**
1. **Gramática Livre de Contexto (CFG):** Conjunto de regras que define as possíveis soluções para um problema.
2. **População Inicial:** Conjunto de soluções iniciais (indivíduos), onde cada solução tem vários genomas, cada um associado a um não-terminal na gramática.
3. **Operadores Genéticos:** Mecanismos de cruzamento e mutação aplicados aos genomas.
4. **Fitness Function:** Uma função que avalia a qualidade de cada solução.

#### **Como Funciona?**

1. **Definir a Gramática (CFG):** Começa-se definindo a gramática que descreve as possíveis soluções para o problema. A gramática consiste em regras que são usadas para construir sentenças válidas na linguagem do problema.
   
   Exemplo de CFG para expressões aritméticas simples:
   ```
   <expr> ::= <term> + <term> | <term> - <term> | <term>
   <term> ::= <factor> * <factor> | <factor> / <factor> | <factor>
   <factor> ::= ( <expr> ) | number
   ```

2. **Inicializar a População:** Cria-se uma população inicial de indivíduos. No SGE, cada indivíduo possui múltiplos genomas, cada um associado a um não-terminal na gramática. Isso significa que, por exemplo, o não-terminal `<expr>` terá uma sequência de genes específica, o `<term>` outra, e assim por diante.

3. **Avaliação:** Para cada indivíduo, os genes são mapeados para regras na gramática e usados para gerar uma solução. Essa solução é então avaliada usando a função de fitness.

4. **Aplicar Operadores Genéticos:** Os operadores de cruzamento e mutação são aplicados em cada genoma (ou seja, em cada não-terminal). Isso permite a recombinação e variação das soluções.

5. **Seleção e Substituição:** Os melhores indivíduos são selecionados para a próxima geração, substituindo os menos aptos.

#### **Implementando com PonyGE2**

Para implementar SGE usando PonyGE2, que é um framework em Python para Grammatical Evolution, você seguiria os seguintes passos:

1. **Instalar PonyGE2:**
   ```bash
   git clone https://github.com/PonyGE/PonyGE2.git
   cd PonyGE2
   pip install -r requirements.txt
   ```

2. **Configurar a Gramática:** Defina a gramática no formato BNF (Backus-Naur Form) em um arquivo `.bnf`.

3. **Configurar o SGE:** A configuração do SGE pode ser feita ajustando os parâmetros no arquivo `parameters.py` do PonyGE2, ou criando uma configuração personalizada.

4. **Rodar o SGE:**
   ```bash
   python ponyge.py --parameters your_parameters.txt
   ```
   Aqui, você deve modificar o código do PonyGE2 para separar os genes por não-terminal, implementando a estrutura de SGE.

### 2. **Grammar-based Genetic Programming (GS)**

#### **O que é?**
GS é uma abordagem em que a evolução de programas é guiada por uma gramática. A gramática define as regras que governam como os programas válidos devem ser estruturados. Em GS, cada indivíduo é uma árvore de derivação que segue as regras dessa gramática, e a evolução ocorre através da modificação dessas árvores.

#### **Componentes Principais:**
1. **Gramática Livre de Contexto (CFG):** Define a linguagem dos programas válidos.
2. **Representação da População:** Cada indivíduo é uma árvore de derivação, onde os nós representam não-terminais ou terminais da gramática.
3. **Operadores Genéticos:** Modificam as árvores de derivação mantendo-as válidas.
4. **Fitness Function:** Avalia o quão bem um programa executa a tarefa.

#### **Como Funciona?**

1. **Definir a Gramática:** A gramática é definida para o problema específico, especificando as regras que os programas devem seguir.

2. **Inicializar a População:** A população inicial é gerada criando árvores de derivação válidas a partir da gramática.

3. **Avaliação:** Cada árvore é avaliada executando o programa que ela representa e medindo o desempenho com a função de fitness.

4. **Aplicar Operadores Genéticos:** Cruzamento e mutação são aplicados às árvores de derivação, respeitando sempre a gramática.

5. **Seleção e Substituição:** Indivíduos melhores substituem os menos aptos na população.

#### **Implementando com DEAP**

Para implementar GS usando a biblioteca DEAP (Distributed Evolutionary Algorithms in Python):

1. **Instalar DEAP:**
   ```bash
   pip install deap
   ```

2. **Definir a Gramática:** Use a classe `gp.PrimitiveTree` para definir as regras da gramática.

3. **Configurar a População e Avaliação:**
   ```python
   import deap.gp as gp
   from deap import base, creator, tools

   # Definir os operadores primitivos
   pset = gp.PrimitiveSet("MAIN", arity=2)
   pset.addPrimitive(operator.add, 2)
   pset.addPrimitive(operator.sub, 2)
   pset.addPrimitive(operator.mul, 2)
   pset.addPrimitive(operator.truediv, 2)
   pset.addTerminal(1)
   pset.addTerminal(0)

   # Criar os tipos de indivíduos e fitness
   creator.create("FitnessMax", base.Fitness, weights=(1.0,))
   creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)

   # Definir a população
   toolbox = base.Toolbox()
   toolbox.register("expr", gp.genFull, pset=pset, min_=1, max_=2)
   toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
   toolbox.register("population", tools.initRepeat, list, toolbox.individual)

   # Definir a função de avaliação
   def evalSymbReg(individual):
       # Compilar e executar o programa representado pela árvore
       func = toolbox.compile(expr=individual)
       # Definir o fitness
       return (some_fitness_calculation(func),)
   
   toolbox.register("evaluate", evalSymbReg)
   ```

4. **Rodar o GS:**
   ```python
   population = toolbox.population(n=300)
   for gen in range(50):
       offspring = toolbox.select(population, len(population))
       offspring = list(map(toolbox.clone, offspring))

       for child1, child2 in zip(offspring[::2], offspring[1::2]):
           if random.random() < CXPB:
               toolbox.mate(child1, child2)
               del child1.fitness.values
               del child2.fitness.values

       for mutant in offspring:
           if random.random() < MUTPB:
               toolbox.mutate(mutant)
               del mutant.fitness.values

       fitnesses = map(toolbox.evaluate, offspring)
       for ind, fit in zip(offspring, fitnesses):
           ind.fitness.values = fit

       population[:] = offspring
   ```

### 3. **Context-Free Grammar Genetic Programming (CFG-GP)**

#### **O que é?**
CFG-GP é uma técnica onde a evolução de programas é guiada por uma Gramática Livre de Contexto, similar ao GS. A principal diferença é que no CFG-GP, a gramática é usada de maneira mais direta para garantir que todas as soluções (programas) geradas sejam sintaticamente corretas.

#### **Componentes Principais:**
1. **Gramática Livre de Contexto (CFG):** Define as estruturas dos programas.
2. **População:** Indivíduos representados por árvores de derivação.
3. **Operadores Genéticos:** Operadores que modificam as árvores, respeitando a CFG.
4. **Fitness Function:** Avalia o desempenho dos programas.

#### **Como Funciona?**

1. **Definir a Gramática:** Defina a CFG que expressa todas as soluções válidas.

2. **Inicializar a População:** Gere a população inicial usando a gramática para criar árvores de derivação.

3. **Avaliação:** Cada árvore é avaliada executando o programa e calculando o fitness.

4. **Aplicar Operadores Genéticos:** Cruzamento e mutação são aplicados diretamente nas árvores de derivação, garantindo que as árvores resultantes sejam válidas de acordo com a CFG.

5. **Seleção e Substituição:** Os melhores indivíduos são selecionados para formar a próxima geração.

#### **Implementando com DEAP**

Para implementar

 CFG-GP com DEAP, você pode seguir uma abordagem semelhante à usada para GS, mas com maior foco na manipulação direta da árvore de derivação, garantindo que todos os operadores respeitem a CFG.

```python
import deap.gp as gp

# Definir a CFG como um conjunto de primitivos
pset = gp.PrimitiveSet("MAIN", arity=1)
# Adicionar seus operadores e terminais aqui

# Criar a população, fitness e toolbox como no GS
```

### **Conclusão**

Esses três algoritmos são poderosos para a programação genética, e cada um tem suas particularidades. O SGE oferece maior controle sobre a derivação, o GS usa uma abordagem baseada em árvores com garantias de validade sintática, e o CFG-GP é uma versão direta do GS, focada em manter a correção sintática através de uma gramática.

Para aplicar essas técnicas, PonyGE2 e DEAP são ferramentas úteis, onde PonyGE2 é mais voltado para SGE e DEAP pode ser adaptado para GS e CFG-GP.

Se precisar de ajuda com exemplos específicos ou algum outro detalhe, estou à disposição para ajudar!
