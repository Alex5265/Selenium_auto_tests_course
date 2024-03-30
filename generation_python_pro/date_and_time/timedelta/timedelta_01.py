from datetime import timedelta

delta = timedelta(days=7, hours=20, minutes=7, seconds=17)

print(delta)
print(type(delta))


from datetime import timedelta

delta1 = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000, minutes=5, hours=8, weeks=2)
delta2 = timedelta(weeks=1, hours=23, minutes=61)
delta3 = timedelta(hours=25)
delta4 = timedelta(minutes=300)

print(delta1, delta2, delta3, delta4, sep='\n')


from datetime import timedelta

delta1 = timedelta(minutes=-40)
delta2 = timedelta(seconds=-10, weeks=-2)

print(delta1)
print(delta2)

print()

from datetime import timedelta

delta = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000, minutes=5, hours=8, weeks=2)

print('Количество дней =', delta.days)
print('Количество секунд =', delta.seconds)
print('Количество микросекунд =', delta.microseconds)

print('Общее количество секунд =', delta.total_seconds())

print()


from datetime import timedelta

def hours_minutes(td):
    return td.seconds // 3600, (td.seconds // 60) % 60

delta = timedelta(days=7, seconds=125, minutes=10, hours=8, weeks=2)

hours, minutes = hours_minutes(delta)

print(delta)
print(hours)
print(minutes)
print()

from datetime import timedelta

delta1 = timedelta(days=5) + timedelta(seconds=3600)  # 5 дней + 1 час
delta2 = timedelta(days=5) - timedelta(seconds=3600)  # 5 дней - 1 час

print(delta1)
print(delta2)
print()

from datetime import timedelta

delta1 = 48 * timedelta(hours=1)
delta2 = timedelta(weeks=1) * (3/7)

print(delta1)
print(delta2)
print()

from datetime import timedelta

delta = timedelta(hours=1, minutes=6)
delta1 = delta / 2
delta2 = delta // 5

print(delta1)
print(delta2)

