# Генераторы множеств
# Необходимо с помощью генератора создать множество первых букв каждого слова(в нижнем регистре)
# предложенного списка

words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']

set_words = {i[0].lower() for i in words}

print(*sorted(set_words))
