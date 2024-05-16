from functools import lru_cache

@lru_cache(typed=False)
def concat(text, num):
    return text + ' ' + str(num)

print(concat('beegeek', 1))
print(concat('beegeek', 1.0))
print(concat('beegeek', True))
print(concat('beegeek', 4))
print(concat('beegeek', 4.0))
print(concat('beegeek', 4.0))
print(concat('beegeek', 4.0))
print(concat('beegeek', 4))

print(concat('beegeek', 5))

print(concat.cache_info())


print()
print('cache_clear')
concat.cache_clear()
print(concat.cache_info())


