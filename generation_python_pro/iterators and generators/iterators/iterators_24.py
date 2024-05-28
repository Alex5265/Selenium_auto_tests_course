# Реализуйте класс Xrange, порождающий итераторы,
# конструктор которого принимает три аргумента в следующем порядке:
#
# start — целое или вещественное число
# end — целое или вещественное число
# step — целое или вещественное число, по умолчанию имеет значение
# 1
# 1
# Итератор класса Xrange должен генерировать последовательность членов
# арифметической прогрессии от start до end, включая start и не включая end,
# с шагом step, а затем возбуждать исключение StopIteration.
#
# Примечание 1. В тестирующую систему сдайте программу,
# содержащую только необходимый класс Xrange.


class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        try:
            res = range(round(self.start * 100), round(self.end * 100), round(self.step * 100))[self.index] / 100
            if isinstance(self.step, float) or isinstance(self.start, float) or isinstance(self.end, float):
                return res
            return int(res)
        except:
            raise StopIteration



xrange = Xrange(5.9, 44, 3)

print(tuple(xrange))















