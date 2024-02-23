


with open('languages_work_file_00.txt', 'rt', encoding='utf-8') as file:
    print(file.tell())
    line_1 = file.readline()
    print(line_1)
    print(file.tell())
    file.seek(0)
    print(file.tell())
    line_2 = file.readline()
    print(line_2)




