def fib(n):
    cache = {1: 1, 2: 1}
    def fib_rec(n):
        result = cache.get(n)
        if result is None:
            result = fib_rec(n - 2) + fib_rec(n - 1)
            cache[n] = result
        return result
    return fib_rec(n)


print(fib(20))










from time import perf_counter
from functools import lru_cache

@lru_cache
def factorial_cached(n: int) -> int:
    if n == 0:
        return 1
    return factorial(n - 1) * n

def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

def factorial_common(n):
    res = 1
    for i in range(1, n + 1):
        res *= i

    return res


start = perf_counter()
for _ in range(1_000):
    factorial_cached(995)
end = perf_counter()
fc = end-start
print(f'Время подсчета функции с мемоизацией: {round((fc), 3)}')

start = perf_counter()
for _ in range(1_000):
    factorial(995)
end = perf_counter()
f = end-start
print(f'Время подсчета функции без мемоизации: {round((f), 3)}')

start = perf_counter()
for _ in range(1_000):
    factorial_common(995)
end = perf_counter()
fs = end-start
print(f'Время подсчета функции с обычным циклом: {round((fs), 3)}')

print()

print(f'Функция с мемоизацией работает быстрее обычной рекурсивной в {round(f/fc)} раз(-а)')
print(f'Функция с мемоизацией работает быстрее функции с обычным циклом в {round(fs/fc)} раз(-а)')