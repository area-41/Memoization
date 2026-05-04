# Análise de Eficiência: Recursão Dinâmica e Memoization em Python

Este repositório apresenta um estudo técnico-científico sobre a otimização de algoritmos recursivos utilizando **Memoization**. O foco é analisar a transição de complexidade de tempo de **O(2^n)** para **O(n)**.

## Fundamentação Teórica
A recursão simples para problemas como a Sequência de Fibonacci gera uma árvore de chamadas redundante. A Memoization atua como um mediador de estado que armazena resultados de subproblemas já resolvidos, garantindo que cada entrada seja processada apenas uma vez.

Memoization (memoização) é uma técnica de otimização usada para acelerar programas de computador. 
Ela evita que uma função recalcule valores que já foram processados anteriormente.

### Como funciona
Armazenamento: O programa guarda o resultado de uma função em um cache (geralmente uma tabela hash ou objeto).

#### Consulta: 
Quando a função é chamada novamente com os mesmos parâmetros, o programa não refaz o cálculo. 
Ele busca o resultado direto do cache.
#### Troca: 
Você gasta um pouco mais de memória para ganhar muito mais velocidade.

#### Quando usar
- Funções Puras: Onde a mesma entrada sempre gera exatamente a mesma saída.
- Cálculos Repetitivos: Algoritmos que chamam a si mesmos com os mesmos dados várias vezes (como a sequência de Fibonacci).

#### Exemplo Prático (Fibonacci em Python)

- Sem memoization, calcular o 40º número de Fibonacci leva milhões de operações repetidas. 
- Com memoization, o tempo cai para milissegundos.

      
      # Dicionário que serve como cache
      cache = {}
    
      def fibonacci(n):
          if n in cache:
              return cache[n] # Retorna do cache se já existir
        
          if n <= 1:
              resultado = n
          else:
              resultado = fibonacci(n-1) + fibonacci(n-2)
            
          cache[n] = resultado # Salva no cache antes de retornar
          return resultado


## Metodologia de Teste
Comparamos três abordagens:
1. **Recursão Pura:** Sem persistência de estado.
2. **LRU Cache (Functools):** Implementação nativa do Python.
3. **Manual Dict-Cache:** Implementação customizada para controle granular.

## Resultados Esperados
- **Redução de tempo:** De segundos para microssegundos em entradas $n > 30$[cite: 3].
- **Complexidade Espacial:** Troca de memória por velocidade (Trade-off).

@area-41