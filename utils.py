# app/utils.py
from functools import lru_cache
from fastapi import HTTPException

@lru_cache(maxsize=1000)
def fibonacci(n: int) -> int:
    if n < 0:
        raise HTTPException(status_code=400, detail="Input must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr