# Classificação de Websites de Phishing Usando Algoritmos Baseados em Gramática

Este repositório contém a implementação de vários algoritmos baseados em gramática para a tarefa de classificação de websites de phishing. Os algoritmos implementados incluem:

- **Structured Grammatical Evolution (SGE)**
- **Grammar Swarm (GS)**
- **Context-Free Grammar Genetic Programming (CFG-GP)**

## Estrutura do Repositório

- `/SGE`: Contém a implementação do SGE, incluindo scripts para rodar experimentos e operadores genéticos customizados.
- `/GS`: Contém a implementação do GS, utilizando PSO combinado com gramática livre de contexto.
- `/CFG-GP`: Contém a implementação do CFG-GP utilizando o framework DEAP.
- `/data`: Inclui o conjunto de dados utilizado para avaliar os modelos.
- `/results`: Resultados dos experimentos e um notebook Jupyter para análise comparativa.
- `requirements.txt`: Lista de dependências necessárias para rodar o projeto.
- `README.md`: Este arquivo, contendo a visão geral do projeto.

## Requisitos

Para executar os experimentos, você precisará de um ambiente Python 3.x com as seguintes bibliotecas:

```bash
pip install -r requirements.txt
