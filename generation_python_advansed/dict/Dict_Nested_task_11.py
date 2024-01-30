# Вложенные словари и генераторы
# Необходимо дополнить код, что бы получить список вложенных словарей
# Даны три списка(инфо о студентах) student_ids должен стать ключем,
# student_names должен стать вложеным ключем, а student_grades вложенным значением сложенного словаря
# для понимания-образец:
# [{'S001': {'Camila Rodriguez': 86}}, {'S002': {'Juan Cruz': 98}},...]
# желательно написать генератор



student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

result = [{k: {k_v: v}} for k, k_v, v in zip(student_ids,student_names, student_grades)]


print(result)




# задачка сложная сначала решил через цикл
# for i in range(len(student_ids)):
#     result.append({student_ids[i]: {student_names[i]: student_grades[i]}})
