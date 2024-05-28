# Вам доступен файл data.csv, который содержит информацию об инвестициях в
# различные стартапы. В первом столбце записано название компании (стартапа),
# во втором — инвестируемая сумма в долларах, в третьем — раунд инвестиции:
#
# company,raisedAmt,round
# LifeLock,6850000,b
# LifeLock,6000000,a
# LifeLock,25000000,c
# MyCityFaces,50000,seed
# Flypaper,3000000,a
# ...
# Напишите программу с использованием конвейеров генераторов,
# определяющую общую сумму, которая была инвестирована в раунде а, и выводящую полученный результат.
#
# Примечание 1. Разделителем в файле data.csv является запятая, при этом кавычки не используются.



with open('data.csv', 'r', encoding='utf-8') as file:
    file_lines = (line for line in file)
    line_values = (line.strip().split(',') for line in file_lines)
    file_headers = next(line_values)
    line_dicts = (dict(zip(file_headers, val)) for val in line_values)
    line_filters = (int(line['raisedAmt']) for line in line_dicts if line['round'] == 'a')
    result = sum(line_filters)

print(result)







