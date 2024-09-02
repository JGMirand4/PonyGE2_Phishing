Aqui está o README atualizado para o SGE (Structured Grammatical Evolution) no seu repositório GitHub:

---

# **SGE (Structured Grammatical Evolution)**

Este diretório contém uma implementação do **SGE (Structured Grammatical Evolution)**, uma variação do Grammatical Evolution (GE) que organiza os genótipos em subgenótipos, onde cada não-terminal possui seu próprio conjunto de genes. Esta abordagem busca melhorar a eficiência do processo de busca evolutiva ao estruturar o genótipo de maneira mais explícita.

## **Arquivos Principais**

- **`sge.py`**: Script principal que executa o processo evolutivo utilizando SGE. Este script configura a população, realiza as operações genéticas (seleção, cruzamento, mutação) e executa o loop de gerações até atingir o critério de parada.
  
- **`sge_individual.py`**: Define a classe `SGEIndividual`, que representa um indivíduo na população de SGE. Cada indivíduo possui um genótipo estruturado em subgenótipos para cada não-terminal da gramática.

- **`sge_population.py`**: Implementa a classe `SGEPopulation`, responsável por inicializar e gerenciar a população de indivíduos no algoritmo SGE.

- **`sge_mapping.py`**: Contém a classe `SGEMapping`, que mapeia o genótipo estruturado de um indivíduo para um fenótipo, baseado nas regras de produção definidas na gramática.

## **Como Executar**

1. **Instale os requisitos**:
   Certifique-se de ter os pacotes necessários instalados. Use o seguinte comando para instalar as dependências:

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure a Gramática**:
   Modifique o caminho para o arquivo BNF da sua gramática no script `sge.py` na função `load_grammar`. Este arquivo BNF deve definir as regras de produção que serão usadas para gerar os fenótipos.

3. **Execute o Script**:
   Após configurar a gramática, execute o script `sge.py` para iniciar a evolução.

   ```bash
   python SGE/sge.py
   ```

4. **Resultados**:
   Ao final da execução, o melhor indivíduo será exibido, mostrando seu fenótipo e o valor de fitness associado.

## **Estrutura de Diretórios**

```
SGE/
│
├── sge.py               # Script principal para rodar o SGE
├── sge_individual.py    # Definição do indivíduo SGE
├── sge_population.py    # Gerenciamento da população SGE
└── sge_mapping.py       # Mapeamento do genótipo para fenótipo no SGE
```

## **Considerações**

- **Fitness Function**: A função de fitness usada para avaliar os indivíduos deve ser personalizada de acordo com o problema específico (por exemplo, detecção de phishing).
- **Operadores Genéticos**: As funções de seleção, cruzamento e mutação podem ser ajustadas para melhor se adequar ao seu problema.

Se precisar de mais informações ou orientações, sinta-se à vontade para consultar a documentação ou entrar em contato.

---

Esse README fornece uma visão geral detalhada do que o SGE faz, como ele está estruturado, e como executar o algoritmo no seu ambiente.
