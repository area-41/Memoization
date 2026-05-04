import time
import pandas as pd
from memoizer import MemoizationStudy

def run_experiment(limit: int = 35):
    study = MemoizationStudy()
    data = []

    for i in range(limit):
        # Medindo LRU (Eficiente)
        start = time.perf_counter()
        study.fib_lru(i)
        lru_time = time.perf_counter() - start

        # Medindo Normal (Lento) - Limitamos para não travar o PC
        normal_time = None
        if i < 33: 
            start = time.perf_counter()
            study.fib_recursive(i)
            normal_time = time.perf_counter() - start

        data.append({
            "input_n": i,
            "lru_seconds": lru_time,
            "normal_seconds": normal_time
        })
    
    df = pd.DataFrame(data)
    df.to_csv("results/benchmark_data.csv", index=False)
    print("Experimento concluído. Dados salvos em results/")

if __name__ == "__main__":
    run_experiment()
