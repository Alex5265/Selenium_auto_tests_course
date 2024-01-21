# Генераторы множеств
# Необходимо с помощью генератора создать множество так тобы он выбрал уникальные файлы с расширение
# .png независимо от регистра имен. Имена файлов вывести с расширением все на одной строке в нижнем регистре

files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt',
         'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg',
         'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko',
         'github.git']

set_files = {i.lower() for i in files if i.lower().endswith('.png')}

print(*sorted(set_files))