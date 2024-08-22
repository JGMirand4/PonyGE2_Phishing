
## GE vs SGE

### Grammatical Evolution (GE)

**1. Representação Genética:**

-   No GE, um indivíduo é representado por um único genoma, que é uma sequência de inteiros. Cada inteiro no genoma é um índice que corresponde a uma regra gramatical específica a ser aplicada durante o processo de derivação.
-   A gramática é definida usando uma _Gramática Livre de Contexto (CFG)_, onde as regras da gramática definem as possíveis produções de um símbolo não-terminal.

**2. Mapeamento Genótipo-Fenótipo:**

-   O mapeamento do genótipo para o fenótipo (a solução ou programa final) é realizado pela aplicação sequencial de regras gramaticais.
-   A sequência de genes (números inteiros) no genoma determina qual produção será escolhida para expandir cada não-terminal durante o processo de derivação.
-   Como o mapeamento é sequencial e linear, o genoma é consumido em uma única passagem, e o mesmo conjunto de genes pode ser usado para expandir diferentes não-terminais.

**3. Operadores Genéticos:**

-   GE usa operadores genéticos tradicionais, como cruzamento e mutação, diretamente sobre o genoma linear.
-   As operações genéticas não levam em consideração a estrutura da gramática, o que pode resultar em soluções válidas ou inválidas, dependendo de como os genes são mapeados para as regras gramaticais.

**4. Flexibilidade e Complexidade:**

-   GE é flexível e pode ser aplicado a uma ampla gama de problemas que podem ser modelados usando uma gramática.
-   No entanto, a simplicidade de usar um único genoma para todas as partes da derivação pode limitar o controle sobre como diferentes partes da gramática são exploradas, o que pode levar a uma exploração ineficiente do espaço de soluções.

### Structured Grammatical Evolution (SGE)

**1. Representação Genética:**

-   No SGE, a principal diferença é que cada não-terminal na gramática tem seu próprio genoma separado. Isso significa que, em vez de um único genoma linear, cada indivíduo em SGE possui múltiplos genomas, com um genoma associado a cada não-terminal da gramática.
-   Cada genoma separado corresponde a um conjunto específico de regras para um não-terminal específico, permitindo maior controle e precisão sobre como as regras são aplicadas.

**2. Mapeamento Genótipo-Fenótipo:**

-   O mapeamento no SGE é mais estruturado. Cada não-terminal é expandido usando apenas os genes do genoma associado a ele. Isso significa que o mapeamento é mais modular, e diferentes partes da gramática são tratadas de maneira independente.
-   Essa separação permite uma exploração mais focada e eficiente do espaço de busca, pois as partes da solução que correspondem a diferentes não-terminais não competem pelos mesmos genes.

**3. Operadores Genéticos:**

-   Operadores genéticos em SGE são aplicados separadamente a cada genoma associado a um não-terminal. Isso pode resultar em mutações e cruzamentos mais controlados e localizados, mantendo a coerência estrutural das soluções.
-   A aplicação separada dos operadores genéticos a cada parte da gramática pode reduzir a chance de gerar soluções inválidas, uma vez que cada genoma é específico para um conjunto de regras.

**4. Flexibilidade e Complexidade:**

-   SGE oferece maior controle e flexibilidade na exploração do espaço de soluções, pois cada parte da gramática pode evoluir de maneira mais independente.
-   No entanto, essa estrutura mais complexa também pode tornar o SGE mais difícil de implementar e ajustar em comparação ao GE tradicional.

### Resumo das Principais Diferenças

1.  **Representação Genética:**
    
    -   **GE:** Um único genoma linear é usado para todos os não-terminais.
    -   **SGE:** Cada não-terminal tem seu próprio genoma separado.
2.  **Mapeamento Genótipo-Fenótipo:**
    
    -   **GE:** O mapeamento é linear e sequencial, usando um único genoma para expandir diferentes não-terminais.
    -   **SGE:** O mapeamento é modular, com cada não-terminal sendo expandido usando seu próprio genoma.
3.  **Operadores Genéticos:**
    
    -   **GE:** Operadores genéticos são aplicados a um único genoma, o que pode resultar em menos controle sobre a estrutura da solução.
    -   **SGE:** Operadores são aplicados separadamente a cada genoma, permitindo mais controle sobre a evolução de diferentes partes da gramática.
4.  **Flexibilidade e Complexidade:**
    
    -   **GE:** Mais simples de implementar, mas com menos controle sobre a evolução de diferentes partes da gramática.
    -   **SGE:** Mais complexo, mas com maior controle e potencial para uma exploração mais eficiente do espaço de busca.
```
