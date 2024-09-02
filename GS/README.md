# Grammar Swarm (GS)

Este diretório contém a implementação do Grammar Swarm (GS), um algoritmo que utiliza Particle Swarm Optimization (PSO) em conjunto com uma gramática livre de contexto para gerar soluções.

## Arquivos

- **gs_pso.py**: Implementação do PSO adaptado para funcionar com a gramática.
- **gs_mapping.py**: Função de mapeamento que utiliza a gramática para gerar soluções a partir das partículas.
- **gs_fitness.py**: Função de avaliação de fitness para as soluções geradas.
- **gs_experiment.py**: Script principal para rodar experimentos usando GS.

## Executando Experimentos

Para executar um experimento com GS, siga os passos abaixo:

1. Certifique-se de que você está no diretório GS:
    ```bash
    cd GS
    ```
2. Execute o script de experimento:
    ```bash
    python gs_experiment.py
    ```

Os resultados serão salvos na pasta `../results/gs_results.csv`.

## Configurações do Experimento

As configurações do PSO, como número de partículas, iterações, e outros parâmetros, podem ser ajustadas diretamente no arquivo `gs_experiment.py`.

