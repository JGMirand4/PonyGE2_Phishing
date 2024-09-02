# Structured Grammatical Evolution (SGE)

Este diretório contém a implementação do Structured Grammatical Evolution (SGE), uma variação do Grammatical Evolution (GE) que estrutura o genótipo em uma lista de listas, cada uma correspondendo a um não-terminal da gramática.

## Arquivos

- **sge_genotype.py**: Define a estrutura do genótipo utilizado no SGE.
- **sge_mapping.py**: Função de mapeamento que converte o genótipo em uma árvore sintática.
- **sge_crossover.py**: Implementação dos operadores genéticos de crossover e mutação para SGE.
- **sge_experiment.py**: Script principal para rodar experimentos usando SGE.

## Executando Experimentos

Para executar um experimento com SGE, siga os passos abaixo:

1. Certifique-se de que você está no diretório SGE:
    ```bash
    cd SGE
    ```
2. Execute o script de experimento:
    ```bash
    python sge_experiment.py
    ```

Os resultados serão salvos na pasta `../results/sge_results.csv`.

## Configurações do Experimento

As configurações do experimento podem ser ajustadas diretamente no arquivo `sge_experiment.py`, onde você pode modificar parâmetros como população, número de gerações, e função de fitness.


