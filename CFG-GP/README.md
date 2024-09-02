# Context-Free Grammar Genetic Programming (CFG-GP)

Este diretório contém a implementação do Context-Free Grammar Genetic Programming (CFG-GP) utilizando a biblioteca DEAP, que permite a criação de programas com base em uma gramática livre de contexto.

## Arquivos

- **cfg_gp.py**: Implementação principal do CFG-GP utilizando DEAP.
- **cfg_grammar.py**: Definição da gramática usada para gerar os programas.
- **cfg_experiment.py**: Script principal para rodar experimentos usando CFG-GP.

## Executando Experimentos

Para executar um experimento com CFG-GP, siga os passos abaixo:

1. Certifique-se de que você está no diretório CFG-GP:
    ```bash
    cd CFG-GP
    ```
2. Execute o script de experimento:
    ```bash
    python cfg_experiment.py
    ```

Os resultados serão salvos na pasta `../results/cfg_gp_results.csv`.

## Configurações do Experimento

Você pode ajustar as configurações do experimento, como tamanho da população, número de gerações, e operadores genéticos, diretamente no arquivo `cfg_experiment.py`.


