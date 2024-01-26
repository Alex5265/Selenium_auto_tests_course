# Методы словарей
# На вход подается строка текста со знаками препинания.
# Необходимо вывести слово, которое встречается реже всего без учета регистра



s = [word.strip('.,:;!?-') for word in input().lower().split()]

result = {word: s.count(word) for word in s}

print(sorted(word for word in result if result[word] == min(result.values()))[0])


#
#How are you? how Are?
# На выходе
# you
#
#
#