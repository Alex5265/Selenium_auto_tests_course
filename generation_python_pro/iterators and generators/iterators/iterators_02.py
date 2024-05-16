from sys import getsizeof


some_list = [chr(i) for i in range(ord('a'), ord('z'))]
print(some_list)
print(getsizeof(some_list))
some_iter = iter(some_list)
print(some_iter)
print(getsizeof(some_iter))
del some_list
print(next(some_iter))
print(next(some_iter))
print(next(some_iter))
print(next(some_iter))
print(next(some_iter))
print(getsizeof(some_iter))
