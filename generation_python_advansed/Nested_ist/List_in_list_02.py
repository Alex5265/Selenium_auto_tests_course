# Тренировка списков.
# Задание вывести вложенные списки построчно по возрастанию до длинны n, состоящий из n строк

# Получаем число n
n = int(input())

# Пустой список
result = []

# С помощью цикла добавляем вложенные списки, зависящие от длины i
for i in range(1, n + 1):
    result.append(list(range(1, i + 1)))

# Выводим результат с разделителем переноса строки
print(*result, sep='\n')
