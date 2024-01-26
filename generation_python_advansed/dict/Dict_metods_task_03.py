# Методы словарей
# необходимо написать/дополнить код, так чтобы результ хранил словать каждого символа и количество вхождений,,,,


text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'


result = {}
for word in text:
    result[word] = result.get(word, 0) + 1

print(result)