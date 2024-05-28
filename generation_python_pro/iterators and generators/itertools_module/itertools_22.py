# from itertools import permutations, combinations
#
#
# print(len(tuple(combinations(range(26), 2))))







from itertools import permutations, combinations, combinations_with_replacement

numbers = [1, 2, 3]

print(*permutations(numbers, 2))
print(*combinations(numbers, r=2))
print(*combinations_with_replacement(numbers, r=2))