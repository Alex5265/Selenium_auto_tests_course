# Задачи на модуль рандом и стринг.
# Необходимо написать код, который назначает каждому ученику его тайного друга
# на вход подается число n зачем n строк учеников
# невозможно быть тайным другом самому себе и нескольким ученикам

import random

n = int(input())
name = [input() for _ in range(n)]
seckret = name[:]
random.shuffle(seckret)
answer = {}
ind = 0
while len(seckret) > 0:
    if seckret[ind] != name[ind]:
        answer[name.pop(ind)] = seckret.pop(ind)
    else:
        random.shuffle(seckret)

for k in answer:
    print(f'{k} - {answer[k]}')