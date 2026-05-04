# Análise de Eficiência: Recursão Dinâmica e Memoization em Python

Este repositório apresenta um estudo técnico-científico sobre a otimização de algoritmos recursivos utilizando **Memoization**. O foco é analisar a transição de complexidade de tempo de **O(2^n)** para **O(n)**.

## Fundamentação Teórica
A recursão simples para problemas como a Sequência de Fibonacci gera uma árvore de chamadas redundante. A Memoization atua como um mediador de estado que armazena resultados de subproblemas já resolvidos, garantindo que cada entrada seja processada apenas uma vez.

## Metodologia de Teste
Comparamos três abordagens:
1. **Recursão Pura:** Sem persistência de estado.
2. **LRU Cache (Functools):** Implementação nativa do Python.
3. **Manual Dict-Cache:** Implementação customizada para controle granular.

## Resultados Esperados
- **Redução de tempo:** De segundos para microssegundos em entradas $n > 30$[cite: 3].
- **Complexidade Espacial:** Troca de memória por velocidade (Trade-off).
