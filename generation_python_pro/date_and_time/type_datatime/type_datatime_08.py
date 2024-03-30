# Во время визита очередного гостя сотрудникам отеля приходится проверять,
# доступна ли та или иная дата для бронирования номера.
# Реализуйте функцию is_available_date(),
# которая принимает два аргумента в следующем порядке:
# booked_dates — список строковых дат, недоступных для бронирования.
# Элементом списка является либо одиночная дата, либо период (две даты через дефис).
# Например: ['04.11.2021', '05.11.2021-09.11.2021']
# date_for_booking — одиночная строковая дата или период (две даты через дефис),
# на которую гость желает забронировать номер.
# Например: '01.11.2021' или '01.11.2021-04.11.2021'
#
# Функция is_available_date() должна возвращать True,
# если дата или период date_for_booking полностью доступна для бронирования.
# В противном случае функция должна возвращать False.
# Примечание 1. Гарантируется, что в периоде левая дата всегда меньше правой.
# Примечание 2. В периоде (две даты через дефис) граничные даты включены.

from datetime import datetime

# сторонее решение которое транфомирует моё решение в более короткий и красивый код
def is_available_date(booked_dates, date_for_booking):
    # создаем список
    ord_booked_dates = []
    # поэлементно достаем из списка дат данные
    for d in booked_dates:
        # правильная мысть - какая разница есть "-" или нет можо рабить через сплит и все данные превратить  в инты
        dates = [datetime.strptime(i, '%d.%m.%Y').toordinal() for i in d.split('-')]
        # первый и -1 если элементы добавляем в список орд очень красиво
        ord_booked_dates.extend(range(dates[0], dates[-1] + 1))
     # требуемую дату так же сплитуем через - и не важно естьоно или нет и превращаем в инт
    dt = [datetime.strptime(i, '%d.%m.%Y').toordinal() for i in date_for_booking.split('-')]
    # помещаем искомую дату в рэндж из 0 и -1 элемента
    date_f_b = range(dt[0], dt[-1] + 1)
    # возвращаем сравнение всех элментов если они не в диапазоне date_f_b
    return(all([i not in ord_booked_dates for i in date_f_b]))






dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '10.11.2021-14.11.2021'
print(is_available_date(dates, some_date)) # False








# моё первое самостоятельное решение на память много строчек можно сократить

# from datetime import datetime
#
#
# def righting_interval(dates):
#     ret = []
#     if '-' in dates:
#         one, two = dates.split('-')
#         one = datetime.strptime(one, '%d.%m.%Y').timestamp()
#         two = datetime.strptime(two, '%d.%m.%Y').timestamp()
#         ret.extend((one, two))
#     else:
#         one = two = datetime.strptime(dates, '%d.%m.%Y').timestamp()
#         ret.extend((one, two))
#     return ret
#
#
#
# def is_available_date(booked_dates, date_for_booking):
#     flag = True
#     need_dates_st, need_dates_en = righting_interval(date_for_booking)
#
#     for el in booked_dates:
#         bisy_st, bisy_en = righting_interval(el)
#         if bisy_st <= need_dates_st <= bisy_en or bisy_st <= need_dates_en <= bisy_en:
#             flag = False
#         if need_dates_st <= bisy_st <= need_dates_en or need_dates_st <= bisy_en <= need_dates_en:
#             flag = False
#
#     return flag



