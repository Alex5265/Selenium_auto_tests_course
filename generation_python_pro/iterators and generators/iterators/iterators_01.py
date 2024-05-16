from sys import getsizeof


sentence = 'In the face of ambiguity refuse the temptation to guess'

filter_iterator = filter(lambda word: len(word) > 4, sentence.split())   # фильтруем
print(getsizeof(filter_iterator))
map_iterator = map(lambda word: word.upper(), filter_iterator)           # преобразовываем
print(getsizeof(map_iterator))
enumerate_iterator = enumerate(map_iterator, 1)                          # нумеруем
print(getsizeof(enumerate_iterator))

for index, value in enumerate_iterator:                                  # выводим
    print(f'{index}. {value}')



print(getsizeof(filter_iterator))
print(getsizeof(map_iterator))
print(getsizeof(enumerate_iterator))
print()


nums = iter([1, 2, 3, 4])

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums, -1))
print(next(nums, -1))








