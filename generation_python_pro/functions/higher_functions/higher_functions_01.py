from time import perf_counter
import operator

n = 10 ** 6

start_gen = perf_counter()
my_list = [abs(i) for i in range(n)]
end_gen = perf_counter() - start_gen


start_map = perf_counter()
my_list_map = list(map(abs, range(n)))
end_map = perf_counter() - start_map

print('Time list_comprehension: {} seconds'.format(round(end_gen, 3)))  # Time list_comprehension: 0.09 seconds
print('Time map: {} seconds'.format(round(end_map, 3)))  # Time map: 0.05 seconds

start_oper_gen = perf_counter()
my_list = [operator.add(i, 1) for i in range(n)]
end_oper_gen = perf_counter() - start_gen


start_oper_map = perf_counter()
my_list_map = list(map(lambda x: operator.add(x, 1), range(n)))
end_oper_map = perf_counter() - start_map

print('Time list_comprehension operator: {} seconds'.format(round(end_oper_gen, 3)))  # Time list_comprehension: 0.09 seconds
print('Time map operator: {} seconds'.format(round(end_oper_map, 3)))  # Time map: 0.05 seconds