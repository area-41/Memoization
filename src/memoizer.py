import time
from functools import lru_cache
from typing import Dict, Callable

class MemoizationStudy:
    """
    Contém diferentes implementações para análise comparativa.
    """
    
    @staticmethod
    def fib_recursive(n: int) -> int:
        """Implementação recursiva padrão - O(2^n)."""
        if n < 2: return n
        return MemoizationStudy.fib_recursive(n-1) + MemoizationStudy.fib_recursive(n-2)

    @staticmethod
    @lru_cache(maxsize=None)
    def fib_lru(n: int) -> int:
        """Implementação com cache nativo - O(n)[cite: 3]."""
        if n < 2: return n
        return MemoizationStudy.fib_lru(n-1) + MemoizationStudy.fib_lru(n-2)

    def __init__(self):
        self._cache: Dict[int, int] = {}

    def fib_manual(self, n: int) -> int:
        """Implementação manual para demonstrar o funcionamento interno do cache."""
        if n in self._cache:
            return self._cache[n]
        if n < 2:
            return n
        
        self._cache[n] = self.fib_manual(n-1) + self.fib_manual(n-2)
        return self._cache[n]
