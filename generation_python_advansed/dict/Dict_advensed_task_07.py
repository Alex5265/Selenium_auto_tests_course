# Задачи на словари
# На вход приходить засекреченное слово в виде символов второй
# строкой приходит число n - количество букв в словаре, а затем
# сколько раз конкретная буква алфавита встречается в зашифрованном слове

sekret_word = input()
sekret = {}

for i in sekret_word:
    sekret[i] = sekret.get(i, 0) + 1

char_dict = {int(v): k for _ in range(int(input())) for k, v in [input().split(':')]}

print(char_dict)
print(sekret)

for ch in sekret_word:
    print(char_dict[sekret[ch]], end='')



