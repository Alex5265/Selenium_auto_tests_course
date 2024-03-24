# На вход программе в первой строке подается целое неотрицательное число n — количество выданных ящиков.
# В следующих n строках перечислены сами ящики в порядке выдачи, по одному на строке.
# На следующей строке задано целое неотрицательное число m — количество новых сотрудников,
# которым нужно раздать корпоративные ящики.
# Каждая из последующих m строк представляет собой имя и фамилию сотрудника в подготовленном к использованию формате.
#
# Формат выходных данных
# Программа должна вывести почтовые ящики ( m строк) для новых сотрудников
# в том порядке, в котором они раздавались.



n_box = [input().split('@')[0] for _ in range(int(input()))]
m_box = [input() for _ in range(int(input()))]

def create_employees_mail(has_employees, new_employees):
    new_mail = []
    for employ in new_employees:
        if employ in has_employees or employ in new_mail:
            count = 1
            mail = employ + str(count)
            while True:
                if mail in has_employees or mail in new_mail:
                    count += 1
                    mail = employ + str(count)
                else:
                    break
            new_mail.append(mail)
        else:
            new_mail.append(employ)

    return [i + '@beegeek.bzz' for i in new_mail]

print(*create_employees_mail(n_box, m_box), sep='\n')


print(create_employees_mail(['ivan-petrov', 'petr-ivanov', 'ivan-petrov1', 'ivan-ivanov',
                             'ivan-ivanov1', 'ivan-ivanov2'],['ivan-ivanov', 'petr-petrov', 'petr-ivanov']))

print(create_employees_mail(['timyr-guev2', 'anri-tabuev'],['timyr-guev', 'timyr-guev', 'anri-tabuev']))


print(create_employees_mail(['timyr-guev2', 'ruslan-chaniev1', 'ruslan-chaniev'],
                            ['timyr-guev', 'timyr-guev', 'timyr-guev', 'ruslan-chaniev', 'ruslan-chaniev']))






